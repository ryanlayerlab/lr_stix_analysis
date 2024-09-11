import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sr', type=str, help='Short read file or files')
    parser.add_argument('--lr', type=str, help='Long read file or files')
    parser.add_argument('--t',
                        type=int,
                        help='Depth threshold (default = 1)',
                        default=1,
                        required=True)
    return parser.parse_args()

def parse_lr_file(lr_file, LR, t):
    with open(lr_file, 'r') as f:
        sv = None
        for line in f:
            if line.startswith('>>>'):
                l,r = line[3:].rstrip().split()[:2]
                lchr,lpos = l.split(':')
                rchr,rpos = r.split(':')
                lstart,lend= lpos.split('-')
                rstart,rend= rpos.split('-')
                sv = (lchr,lstart,rstart)
                if sv not in LR:
                    LR[sv] = 0
                depth = 0
                ditch_line = f.readline()
                while not ditch_line.startswith('Giggle_File_Id'):
                    ditch_line = f.readline()
            else:
                paired,split = [int(x) for x in line.rstrip().split()[-2:]]
                LR[sv] = LR[sv] + (paired + split >= t )
    return LR

def parse_sr_file(sr_file, SR, t):
    with open(sr_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            sv = (A[0], A[1], A[2])

            if sv not in SR:
                SR[sv] = 0

            for s in A[4:]:
                sample,count = s.split(':')
                count = int(count)

                if count >= t:
                    SR[sv] = SR[sv] + 1
    return SR

def main():
    args = parse_args()

    if args.lr is not None:
        LR = {}
        for file in glob.glob(args.lr):
            LR = parse_lr_file(file, LR, args.t)

        for sv in LR:
            print('\t'.join(list(sv) + [str(LR[sv])]))
    elif args.sr is not None:
        SR = {}
        for file in glob.glob(args.sr):
            SR = parse_sr_file(file, SR, args.t)

        for sv in SR:
            print('\t'.join(list(sv) + [str(SR[sv])]))

if __name__ == '__main__':
    main()
