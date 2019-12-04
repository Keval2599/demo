from collections import defaultdict
grammar = {'E': ['Ted'],
           'Ed': ['+TEd', '#'],
           'T': ['FTd'],
           'Td': ['*FTd', '#'],
           'F': ['(E)', 'a']}

##grammar = input('Enter grammar as "E": ["TEd"]: ')
first = defaultdict(set)

def first_set(f):
    for j in grammar[f]:
        if j[0] == '#':
            first[i].add('#')
        elif j[0].islower():
            first[i].add(j[0])
        elif j[0].isupper():
            first[i].add(first_set(j[0]))
        else:
            first[i].add(j[0])

for i in grammar.keys():
    first_set(i)
print("First Set:")
for i in first.keys():
    print(i, end=' -> ')
    for j in first[i]:
        if not j==None:
            print(j, end='  ')
    print('hello keval')
