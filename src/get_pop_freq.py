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
    parser.add_argument('--adj', action='store_true', help="Adjust start end by 10bp")

    return parser.parse_args()

def get_sv_from_header(header, adj):
    l,r = line[3:].rstrip().split()[:2]
    lchr,lpos = l.split(':')
    rchr,rpos = r.split(':')
    lstart,lend= lpos.split('-')
    rstart,rend= rpos.split('-')
    sv_type = line.rstrip().split()[3]
    sv = None
    if adj:
        sv = (lchr,str(int(lstart)+10),str(int(rstart)+10),sv_type)
    else:
        sv = (lchr,lstart,rstart,sv_type)
    return sv


def parse_lr_file(lr_file, LR, t, adj):
    with open(lr_file, 'r') as f:
        sv = None
        for line in f:
            if line.startswith('>>>'):
                key = line.rstrip()
                #l,r = line[3:].rstrip().split()[:2]
                #lchr,lpos = l.split(':')
                #rchr,rpos = r.split(':')
                #lstart,lend= lpos.split('-')
                #rstart,rend= rpos.split('-')
                #sv_type = line.rstrip().split()[3]
                #sv = None
                #if adj:
                #    sv = (lchr,str(int(lstart)+10),str(int(rstart)+10),sv_type)
                #else:
                #    sv = (lchr,lstart,rstart,sv_type)
                if key not in LR:
                    LR[key] = 0
                ditch_line = f.readline()
                while not ditch_line.startswith('Giggle_File_Id'):
                    ditch_line = f.readline()
            else:
                paired,split = [int(x) for x in line.rstrip().split()[-2:]]
                LR[key] = LR[key] + (paired + split >= t )
    return LR

def parse_sr_file(sr_file, SR, t):
    with open(sr_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            sv = (A[0], A[1], A[2], A[3])

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

    SV = {}

    if args.lr is not None:
        for file in glob.glob(args.lr):
            SV = parse_lr_file(file, SV, args.t, args.adj)

        for sv in SV:
            pretty_sv = get_sv_from_header(sv, args.adj)
            print('\t'.join(list(pretty_sv) + [str(SV[sv])]))

    elif args.sr is not None:
        for file in glob.glob(args.sr):
            SV = parse_sr_file(file, SV, args.t)
        for sv in SV:
            print('\t'.join(list(sv) + [str(SV[sv])]))

if __name__ == '__main__':
    main()
