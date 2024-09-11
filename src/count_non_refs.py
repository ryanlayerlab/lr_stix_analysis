import sys

def main():
    for line in sys.stdin:
        A = line.rstrip().split()
        chrm = A[0]
        start = A[1]
        end = A[2]
        GT = A[3:]
        num_non_ref = 0
        for gt in GT:
            if gt != '0/0' and gt != './.':
                num_non_ref += 1
        print('\t'.join([chrm, start, end, str(num_non_ref)]))

if __name__ == '__main__':
    main()
