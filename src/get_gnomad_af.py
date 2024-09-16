import sys

for line in sys.stdin:
    if not line.startswith('>>>'):
        continue
    A = line.rstrip().split()
    leftq = A[0][3:]
    rightq = A[1]
    svtype = A[3]
    AF = A[4].split(';')[-1].split('=')[-1]

    chrm = leftq.split(':')[0]
    left = leftq.split(':')[1].split('-')[0]
    right = rightq.split(':')[1].split('-')[0]

    print('\t'.join([chrm, left, right, svtype, AF]))

