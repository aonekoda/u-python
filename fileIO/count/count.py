import collections


def count_unique_words(filename):
    cnt = collections.Counter()
    
    with open(filename, 'r') as f :
        for line in f:
            cnt.update(line.split())
    for word, count in cnt.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')
