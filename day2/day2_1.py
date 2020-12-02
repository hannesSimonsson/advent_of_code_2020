'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

# get input
with open("input_day2.txt") as f:
    inputs = f.read().splitlines()

passCounter = 0
for i in inputs:
    # convert input to list by splitting at spaces
    inputList = i.split()
    
    # filter input to seperate variables
    password = inputList.pop()
    character = inputList.pop()[0]
    tmp = inputList.pop().split('-')
    high = int(tmp.pop())
    low = int(tmp.pop())

    # count the amount of times a character is found in the password
    characterCount = 0
    for c in password:
        if(c == character):
            characterCount += 1

    # check if the character count is within bounds
    if(characterCount >= low and characterCount <= high:
        passCounter += 1

print(passCounter)
