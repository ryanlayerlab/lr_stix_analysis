import argparse
import glob
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stat', type=str, help='Stat to run (mean, median)')
    parser.add_argument('--sr', type=str, help='Short read file or files')
    parser.add_argument('--lr', type=str, help='Long read file or files')
    parser.add_argument('--coverage', type=str, help='Sample average coverage file')
    parser.add_argument('--adj', action='store_true', help="Adjust start end by 10bp")

    return parser.parse_args()

def get_lr_sample_depths(file_name):
    S = {}
    with open(file_name, 'r') as f:
        for line in f:
            tech, sample, depth = line.rstrip().split()
            if sample not in S:
                S[sample] = {}
            S[sample][tech] = float(depth)
    return S

def get_sr_sample_depths(file_name):
    S = {}
    with open(file_name, 'r') as f:
        for line in f:
            sample, depth = line.rstrip().split()
            S[sample] = float(depth)
    return S

def get_sv_from_header(line, adj):
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

def get_sample_depths_from_line(line):
    A = line.rstrip().split()
    sample = A[1]
    paired, split = [int(x) for x in line.rstrip().split()[-2:]]
    return sample, paired, split

def parse_lr_file(lr_file, LR, adj):
    with open(lr_file, 'r') as f:
        sv = None
        for line in f:
            if line.startswith('>>>'):
                sv = get_sv_from_header(line, adj)
                if sv not in LR:
                    LR[sv] = {}
                ditch_line = f.readline()
                while not ditch_line.startswith('Giggle_File_Id'):
                    ditch_line = f.readline()
            else:
                sample, paired, split = get_sample_depths_from_line(line)
                LR[sv][sample] = paired + split
    return LR

def parse_sr_file(sr_file, SR):
    with open(sr_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            sv = (A[0], A[1], A[2], A[3])

            if sv not in SR:
                SR[sv] = {}

            for s in A[4:]:
                sample,count = s.split(':')
                count = int(count)
                SR[sv][sample] = count
    return SR

def split_sample_tech(sample):
    sid = sample.split('.')[0]
    tech = sample.split('.')[-1]
    if tech == 'hprc':
        return sid, 'hprc'
    elif tech == 'vienna':
        return sid, '1000g_vienna'
    elif tech == 'ont':
        return sid, '1000g_ont'
    else:
        raise ValueError('Unknown tech: {}'.format(tech))

def main():
    args = parse_args()

    SV = {}


    if args.lr is not None:
        sample_depths = get_lr_sample_depths(args.coverage)

        for file in glob.glob(args.lr):
            SV = parse_lr_file(file, SV, args.adj)

        for sv in SV:
            non_zero_depths = []
            for sample in SV[sv]:
                sid, tech = split_sample_tech(sample)
                if sid not in sample_depths:
                    continue
                if tech not in sample_depths[sid]:
                    continue
                depth = sample_depths[sid][tech]

                if SV[sv][sample] > 0:
                    non_zero_depths.append(SV[sv][sample]/depth)

            if args.stat == 'mean':
                print('\t'.join(list(sv) + [str(np.mean(non_zero_depths))]))
            elif args.stat == 'median':
                print('\t'.join(list(sv) + [str(np.median(non_zero_depths))]))

    elif args.sr is not None:
        sample_depths = get_sr_sample_depths(args.coverage)

        for file in glob.glob(args.sr):
            SV = parse_sr_file(file, SV)

        for sv in SV:
            non_zero_depths = []
            for sample in SV[sv]:
                if sample not in sample_depths:
                    continue
                depth = sample_depths[sample]
                if SV[sv][sample] > 0:
                    non_zero_depths.append(SV[sv][sample]/depth)

            if args.stat == 'mean':
                print('\t'.join(list(sv) + [str(np.mean(non_zero_depths))]))
            elif args.stat == 'median':
                print('\t'.join(list(sv) + [str(np.median(non_zero_depths))]))



if __name__ == '__main__':
    main()
