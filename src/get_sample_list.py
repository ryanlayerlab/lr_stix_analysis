import argparse
import glob

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sr', type=str, help='Short read file or files')
    parser.add_argument('--lr', type=str, help='Long read file or files')
    return parser.parse_args()

def parse_lr_file(lr_file):
    samples = set()
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
                ditch_line = f.readline()
                while not ditch_line.startswith('Giggle_File_Id'):
                    ditch_line = f.readline()
            else:
                A = line.rstrip().split()
                sample = A[1].split('.')[0]
                samples.add(sample)

    return samples

def parse_sr_file(sr_file):
    samples = set()
    with open(sr_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            for s in A[4:]:
                sample,count = s.split(':')
                samples.add(sample)
    return samples

def main():
    args = parse_args()

    samples = set()
    if args.lr is not None:
        LR = {}
        for file in glob.glob(args.lr):
            new_samples = parse_lr_file(file)
            samples = samples.union(new_samples)

    if args.sr is not None:
        SR = {}
        for file in glob.glob(args.sr):
            new_samples = parse_sr_file(file)
            samples = samples.union(new_samples)

    for sample in samples:
        print(sample)

if __name__ == '__main__':
    main()
