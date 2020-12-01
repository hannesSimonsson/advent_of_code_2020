'''
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''

# get input
with open("input_day1.txt") as f:
    inputList = f.read().splitlines()

# test each inputs remainder for sums where each part is an input
checkList = inputList.copy()
done = False
for i in inputList:
    targetValue = 2020 - int(i)

    checkList.pop(0)
    for j in checkList:
        remainder = targetValue - int(j)

        if (str(remainder) in checkList):
            print (i)
            print(j)
            print(remainder)
            print(int(i) * int(j) * remainder)

            done = True
            break

    if (done):
        break
