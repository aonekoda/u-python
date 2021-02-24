import json

import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!
    prizes = data['prizes']
    
    for prize in prizes:
        if 'laureates' not in prize:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue
        print(f"YEAR:{prize['year']}, CATEGORY:{prize['category']}")
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            motivation = laureate['motivation']
            print(f'{firstname} {surname}, {motivation}')

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)

