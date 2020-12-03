'''
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

- Right 1, down 1.
- Right 3, down 1. (This is the slope you already checked.)
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''

# get input
with open("input_day3.txt") as f:
    inputs = f.read().splitlines()

# max length of a row before it ropes back to the beginning
maxLength = 31

# tuples contain steps to the right R and steps to go down D, (R, D)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

treeMultiplier = 1
for slope in slopes:

    # counters
    trees = 0
    column = slope[0]
    line = 0
    nextLine = 1 + slope[1]

    for row in inputs:
        line += 1
        if(line == nextLine):
            nextLine += slope[1]

            # column correction
            if(column >= maxLength):
                column -= maxLength
    
            # check if tree is encountered
            if(row[column] == "#"):
                trees += 1
            
            column += slope[0]

    treeMultiplier *= trees
    print(trees)

print(treeMultiplier)
