import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser()
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

def main():
    args = parse_args()

    if args.lr is not None:
        LR = {}

        for file in glob.glob(args.lr):
            LR = parse_lr_file(file, LR, args.t)

        for sv in LR:
            print('\t'.join(list(sv) + [str(LR[sv])]))

if __name__ == '__main__':
    main()
