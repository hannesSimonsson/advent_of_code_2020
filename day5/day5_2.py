'''
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''
from day5_1 import binaryConversion

# get input
with open("input_day5.txt") as f:
    inputs = f.read().splitlines()

# calculate seat ID and remove it from the full list of possible IDs
seatIDs = list(range(0, 1023))
for seat in inputs:
    seatID = binaryConversion(seat[:7]) * 8 + binaryConversion(seat[-3:])
    if seatID in seatIDs:
        seatIDs.remove(seatID)

# check all remaining IDs in order, if break in list -> next ID should be the one we want
noID = 0
for ID in seatIDs:
    if noID != ID:
        print(ID)
        break

    noID += 1


