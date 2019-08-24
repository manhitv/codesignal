'''
The master launch sequence consists of several independent sequences for different systems. Your goal is to verify that all the individual system sequences are in strictly increasing order. In other words, for any two elements i and j (i < j) of the master launch sequence that belong to the same system (having systemNames[i] = systemNames[j]), their values should be in strictly increasing order (i.e. stepNumbers[i] < stepNumbers[j]).
*Example:
For systemNames = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"] and stepNumbers = [1, 10, 11, 2, 12, 111], the output should be launchSequenceChecker(systemNames, stepNumbers) = true.
There are three independent sequences for systems "stage_1", "stage_2", and "dragon". These sequences are [1, 2], [10, 12], and [11, 111], respectively. The elements are in strictly increasing order for all three.
For systemNames = ["stage_1", "stage_1", "stage_2", "dragon"] and stepNumbers = [2, 1, 12, 111], the output should be launchSequenceChecker(systemNames, stepNumbers) = false.
There are three independent sequences for systems "stage_1", "stage_2", and "dragon". These sequences are [2, 1], [12], and [111], respectively. In the first sequence, the elements are not ordered properly.
'''
def launchSequenceChecker(systemNames, stepNumbers):
    d = {}
    for i in range(len(systemNames)):
        cur_sys = systemNames[i]
        cur_step = stepNumbers[i]
        if cur_sys not in d:
            d[cur_sys] = [cur_step]
        else:
            d[cur_sys].append(cur_step)
    
    for k in d.keys():
        if len(d[k])>1:
            for i in range(1,len(d[k])):
                if d[k][i]<=d[k][i-1]:
                    return False
    return True

'''
SpaceX is testing flight software subroutines (i.e., programs that consist of sequences of instructions) for a custom rocket CPU. To ensure that the software runs correctly before it's loaded into the rocket, you need to create a CPU simulator.
The CPU has 43 32-bit unsigned integer registers, which are named R00..R42. At the start of the program, all the registers contain 0. The CPU supports the following instructions:
MOV Rxx,Ryy - copies the value from register Rxx to register Ryy;
MOV d,Rxx - copies the numeric constant d (specified as a decimal) to register Rxx;
ADD Rxx,Ryy - calculates (Rxx + Ryy) MOD 232 and stores the result in Rxx;
DEC Rxx - decrements Rxx by one. Decrementing 0 causes an overflow and results in 232-1;
INC Rxx - increments Rxx by one. Incrementing 232-1 causes an overflow and results in 0;
INV Rxx - performs a bitwise inversion of register Rxx;
JMP d - unconditionally jumps to instruction number d (1-based). d is guaranteed to be a valid instruction number;
JZ d - jumps to instruction d (1-based) only if R00 contains 0;
NOP - does nothing.
After the last instruction has been executed, the contents of R42 are considered to be the result of the subroutine.
Write a software emulator for this CPU that executes the subroutines and returns the resulting value from R42.
All the commands in the subroutine are guaranteed to be syntactically correct and have valid register numbers, numeric constants, and jump addresses. The maximum program length is 1024 instructions. The maximum total number of instructions that will be executed until the value is returned is 5 · 104. (Keep in mind that the same instruction will be counted as many times as it will be executed.)
*Example:
For
subroutine = [
  "MOV 5,R00",
  "MOV 10,R01",
  "JZ 7",
  "ADD R02,R01",
  "DEC R00",
  "JMP 3",
  "MOV R02,R42"
]
the output should be cpuEmulator(subroutine) = "50".
'''
def cpuEmulator(subroutine):

    regs = ["R" + str(r).zfill(2) for r in range(0, 43)]
    registers = {r: 0 for r in regs}
    
    i = 0
    while i < len(subroutine):
        
        try:
            del(a);del(b0);del(b1)
        except:
            burn = ""
        
        if subroutine[i] == "NOP":
            i += 1
            continue
        
        a,b0 = subroutine[i].split()
        
        if len(b0.split(',')) > 1:
            
            b0, b1 = b0.split(',')
        
        #### Program start here

        if a == "MOV":
            if b0[0] == "R":
                registers[b1] = int(registers[b0])
                i+=1
            else:
                registers[b1] = int(b0)
                i+=1
        
        elif a == "ADD":
            registers[b0] = int((registers[b0] + registers[b1]) % 2**32)
            i+=1
        
        elif a == "DEC":
            if registers[b0] > 0:
                registers[b0] -= 1
                i+=1
            else:
                registers[b0] = (2**32) -1
                i+=1
    
        elif a == 'INC':
            if registers[b0] < (2**32) -1:
                registers[b0] += 1
                i+=1
            else:
                registers[b0] = 0
                i+=1
        
        elif a == "INV":
            i+=1
            new = []
            for t in bin(registers[b0])[2:].zfill(32):
                if t == '0':
                    new.append('1')
                else:
                    new.append('0')
                    
            registers[b0] = int(''.join(new), 2)
            del(new)
        
        elif a == "JMP":
            i = int(b0) -1
        
        elif a == "JZ":
            if registers['R00'] == 0:
                i = int(b0) -1
            else:
                i += 1

    return str(registers['R42'] % 2**32)
