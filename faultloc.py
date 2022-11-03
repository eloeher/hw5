import sys
import math

def main():
    # read input from command line
    fail_files = []
    pass_files = []
    input_files = []
    for i in sys.argv:
        if i != 'faultloc.py':
            if 'fail' in i: 
                fail_files.append(i)
            if 'pass' in i:
                pass_files.append(i)
            input_files.append(i)

    # compute ochiai score --------------------------
    fail_dir = {}
    pass_dir = {}

    # read in data from files
    for input_file in fail_files:
        with open(input_file, 'r') as visiting_file:
            for line in visiting_file:
                line = line.strip()
                num_occurrences = line[0]
                original_line = line.split(':')[1].strip()
                if original_line in fail_dir: 
                    if '-' in num_occurrences or '#' in num_occurrences or '=' in num_occurrences or original_line == 0:
                        num_occurrences = 0
                    else:
                        fail_dir[original_line] += 1
                else:
                    if '-' in num_occurrences or '#' in num_occurrences or '=' in num_occurrences or original_line == 0:
                        num_occurrences = 0
                    else:
                        fail_dir[original_line] = 1

    # get number of passes per file
    for input_file in pass_files:
        with open(input_file, 'r') as visiting_file:
            for line in visiting_file:
                line = line.strip()
                num_occurrences = line[0]
                original_line = line.split(':')[1].strip()
                if original_line in pass_dir: 
                    if '-' in num_occurrences or '#' in num_occurrences or '=' in num_occurrences or original_line == 0:
                        num_occurrences = 0
                    else:
                        pass_dir[original_line] += 1
                else:
                    if '-' in num_occurrences or '#' in num_occurrences or '=' in num_occurrences or original_line == 0:
                        num_occurrences = 0
                    else:
                        pass_dir[original_line] = 1
                if original_line not in fail_dir.keys():
                    fail_dir[original_line] = 0.0


    # get sum of total failed
    sum_fails = len(fail_files)
    # for i in fail_dir: 
    #     sum_fails += int(i)


    # compute suspiciousness scores
    # for each line:
        # failed(num_occurrences for line) / sqrt(sum(num_occurrences in failed) * (num_occurrences for line in fail + num_occurrences for line in pass))

    sus_scores = []
    for i in fail_dir.keys():
        sus_score = 0
        num_fails = float(fail_dir[i])
        num_passes = 0.0
        if i in pass_dir.keys():
            num_passes = pass_dir[i]
        denom_input = sum_fails * (num_fails + num_passes)
        denominator = math.sqrt(denom_input)
        if denominator != 0:
            sus_score = num_fails / denominator
            sus_scores.append((int(i), sus_score))

    sus_scores = sorted(sus_scores, key=lambda x:(x[1], -x[0]), reverse=True)
    if len(sus_scores) > 100:
        sus_scores = sus_scores[0:100]
    print(sus_scores)


    # print output

if __name__ == "__main__":
    main()