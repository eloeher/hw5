# You must write a Python 3 program, delta.py, that implements delta debugging to find a minimal interesting subset of a given set. Your program takes two arguments:

# the size n of the set to be minimized — for example, if n is 5, the program will find an interesting subset of {0,1,2,3,4}
# a command that determines if a given subset is interesting — for example, if the command is is-interesting.sh, you may invoke is-interesting.sh 0 2 4 to probe if the subset 0 2 4 is interesting
# the command returns the exit code 1 if the subset is interesting and 0 otherwise
# note that command may be "bash ./is-interesting.sh" (or something similarly long) on the autograding server for security/permission reasons; your program should correctly handle the case where the single command string passed in contains spaces (for example, students using os.system() should treating it as one command: do not break it up)
# do not try to add your own "bash" or "./" or whatnot with string concatenation — really just simply use the command passed in and append some arguments
# students who are uncertain about how to invoke a shell script from Python are encouraged to check out Python functions such as subprocess.call(), subprocess.run(), or even os.system()
# Your program should print out a minimal interesting subset in standard Python list format in sorted order. 
# (This is the only output your program should produce. Do not do anything more. Do not submit a program with debugging output for a grade.)

# If the interesting subset is empty, you would print the empty Python list.

import itertools
import sys
import subprocess

# def findsubsets(s, n):
#     return list(map(set, itertools.combinations(s, n)))

# def FAIL( cs ):
#     gt = [3, 6]
#     return set(gt).issubset(set(cs))


class DeltaDebug:

    def __init__(self):
        self.min_array_size = 100
        self.final_set = set()

    def DD(self, P, cs, shell_script_name):
        p1 = cs[0:len(cs)//2]
        p2 = cs[len(cs)//2: len(cs)]

        if len(cs) == 1:
            self.final_set.add(cs[0])
            return cs[0]

        # build command for p1 and P
        command_1 = shell_script_name
        for i in P:
            command_1 += ' ' + str(i)
        for i in p1: 
            command_1 += ' ' + str(i)
        
        # run on p1 and p
        result_1 = subprocess.run(command_1, shell=True)

        if result_1.returncode == 1:
            arr_ran = P + p1
            # if len(arr_ran) < self.min_array_size:
            #     self.min_array_size = len(arr_ran)
            #     self.final_array = arr_ran
            #     print("final array is now", self.final_array)
            return self.DD(P, p1, shell_script_name)

        # build command for p2 and P 
        command_2 = shell_script_name
        for i in P:
            command_2 += ' ' + str(i)
        for i in p2: 
            command_2 += ' ' + str(i)

        #run on p2 and p
        result_2 = subprocess.run(command_2, shell=True)

        if result_2.returncode == 1:
            arr_ran = P + p2
            # if len(arr_ran) < self.min_array_size:
            #     self.min_array_size = len(arr_ran)
            #     self.final_array = arr_ran
            #     print("final array is now", self.final_array)
            return self.DD(P, p2, shell_script_name)

        # if both were 0 recur
        self.DD(P + p2, p1, shell_script_name)
        self.DD(P + p1, p2, shell_script_name)
        return self.final_set


def main():
    # read in n 
    subset_size = int(sys.argv[1])

    res = []

    for i in range(subset_size):
        res.append(i)

    # run shell script on each subset until we get one that returns 1
    shell_script_name = sys.argv[2]

    dd = DeltaDebug().DD([], res, shell_script_name)

    if isinstance(dd, int):
        print(dd)
        return dd
    print(sorted(list(dd)))
    return sorted(list(dd))


if __name__ == "__main__":
    main()