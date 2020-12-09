'''
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
'''
from day9_1 import findError

# get input
with open('input_day9.txt') as f:
    inputs = f.read().splitlines()

# get data to match against
goal = findError(inputs)

# loop through all starting positions
exit = False
for start in inputs:    
    # reset the cumulative series
    series = 0
    # cumulative addition of all inputs going from start to >=
    for num in inputs[inputs.index(start):]:
        series += int(num)

        # series found, calculate encryption weakness
        if series == goal:
            #calculate max and min
            minNum = 0
            maxNum = 0
            for num in inputs[inputs.index(start):inputs.index(num)+1]:
                num = int(num)
                if minNum > num or minNum == 0:
                    minNum = num
                if maxNum < num:
                    maxNum = num

            print(minNum + maxNum)

            exit = True
            break
        
        elif series > goal:
            break

    if exit:
        break
