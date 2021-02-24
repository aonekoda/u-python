import csv
import json
import collections

import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = collections.defaultdict(list)
    
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]
            routes[source].append(dest)
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    result = {source:{(source,)}}
    visit = {source}
    
    for steps in range(max_segments):
        next_visit = set()
        for airport in list(result):
            for target in routes.get(airport, ()):
                if target not in result:
                    next_visit.add(target)
                    result[target] = set()
                for path in result[airport]:
                    if len(path) != steps + 1:
                        continue
                    result[target].add(path+(target,))
        visit = next_visit
    return result[dest]

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    # Don't forget to write the output to JSON!
    for path in paths:
        segments = len(path) - 1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))
        
    with open(f"{source}->{dest}(max_{max_segments}).json", 'w') as f:
        json.dump(output, f, indent=2, sort_keys=True)
  

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
