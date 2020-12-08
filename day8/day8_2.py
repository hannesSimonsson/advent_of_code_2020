'''
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
'''

# handle instruction
def comp(instruction, argument, index, accumulator):
    if instruction == 'acc':
        return index+1, accumulator+int(argument)
    elif instruction == 'jmp':
        return index+int(argument), accumulator
    elif instruction == 'nop':
        return index+1, accumulator
    else:
        print('something went wrong')
        return index, accumulator


# get input -> [[str::instruction, str::argument]]
with open('input_day8.txt') as f:
    inputs = [x.strip('\n').split(' ') for x in f]


acc = 0
i = 0
visited = []
changed = []
change = True
while True:
    # reset and start over
    if i in visited:
        i = 0
        visited = []
        acc = 0
        change = True

    # stop if end of instructions is reached
    if i >= len(inputs):
        break
 
    visited.append(i)

    # check if an instruction should be changed or not
    if change and i not in changed and (inputs[i][0] == 'jmp' or inputs[i][0] == 'nop'):
        if inputs[i][0] == 'jmp':
            changed.append(i)
            i, acc = comp('nop', inputs[i][1], i, acc)
        elif inputs[i][0] == 'nop':
            changed.append(i)
            i, acc = comp('jmp', inputs[i][1], i, acc)
        change = False
    else:
       i, acc = comp(inputs[i][0], inputs[i][1], i, acc)

print(acc)
