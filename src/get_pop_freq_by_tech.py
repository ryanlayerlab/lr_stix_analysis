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
    parser.add_argument('--samples', type=str, help="File with list of samples to include")

    return parser.parse_args()

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



def parse_lr_file(lr_file, LR, t, adj):
    with open(lr_file, 'r') as f:
        sv = None
        for line in f:
            if line.startswith('>>>'):
                sv = get_sv_from_header(line, adj)
                if sv not in LR:
                    LR[sv] = set()
                ditch_line = f.readline()
                while not ditch_line.startswith('Giggle_File_Id'):
                    ditch_line = f.readline()
            else:
                sample, paired, split = get_sample_depths_from_line(line)
                if paired + split >= t:
                    LR[sv].add(sample)
    return LR

def parse_sr_file(sr_file, SR, t):
    with open(sr_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            sv = (A[0], A[1], A[2], A[3])

            if sv not in SR:
                SR[sv] = set()

            for s in A[4:]:
                sample,count = s.split(':')
                count = int(count)

                if count >= t:
                    SR[sv].add(sample)
    return SR

def get_sample_list(sample_file):
    samples = set()
    with open(sample_file, 'r') as f:
        for line in f:
            samples.add(line.rstrip())
    return samples

def main():
    args = parse_args()

    samples = get_sample_list(args.samples)

    SV = {}

    if args.lr is not None:
        for file in glob.glob(args.lr):
            SV = parse_lr_file(file, SV, args.t, args.adj)

    if args.sr is not None:
        for file in glob.glob(args.sr):
            SV = parse_sr_file(file, SV, args.t)

    for sv in SV:
        techs = {'hprc' :set(),
                 'ont' :set(),
                 'vienna' :set()}
        for sample in SV[sv]:
            if sample not in samples: continue
            tech = sample.split('.')[-1]
            techs[tech].add(sample)

        tech_srt = []
        for tech in ['hprc', 'ont', 'vienna']:
            tech_srt.append(str(len(techs[tech])))

        print('\t'.join(list(sv) + tech_srt))

if __name__ == '__main__':
    main()
