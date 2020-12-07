'''
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

- faded blue bags contain 0 other bags.
- dotted black bags contain 0 other bags.
- vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
- dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
'''
import re
from collections import defaultdict

# count amount of bags recursivly
def countBags(bagColor, graph, count=0):
    inBag = graph[bagColor]
    for bag in inBag:
        if bag[0].isdigit():
            count += int(bag[0]) + int(bag[0]) * countBags(bag[1],graph)
        else:
            return 0
        
    return count

# get input with horrible regex implementation -> [[str::(num)bagColor]]
with open('input_day7.txt') as f:
    inputs = [re.sub('\s\s+', ',', re.sub('\.|\n|bag(s?)|contain', '', x)).replace(' ', '').split(',') for x in f.read().split('\n')]
inputs.pop()

# put input in dictionary where number and color is split into tuples -> [key:[(int,str)]]
graph = defaultdict(list)
nodes =[]
for rule in inputs:
    nodes.append(rule[0])

for node in nodes:
    graph[node] = []

for line in inputs:
    edge = line.pop(0)
    for vertex in line:
        graph[edge].append((vertex[0],vertex[1:]))


print(countBags('shinygold', graph))


    
