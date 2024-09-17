import argparse
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
from upsetplot import from_memberships, plot
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_file", required=True, help="Output png file")
    parser.add_argument('--height', type=int, help="The height of the histogram", default=4)
    parser.add_argument('--width', type=int, help="The width of the histogram", default=4)
    parser.add_argument('--title', type=str, help="Plot title")
   
    parser.add_argument("--tick_line_length",
                        type=float,
                        default=2,
                        help="Tick line width")
    
    parser.add_argument("--tick_line_width",
                        type=float,
                        default=0.5,
                        help="Tick line width")
    
    parser.add_argument("--axis_line_width",
                        type=float,
                        default=0.5,
                        help="Axis line width")
    
    parser.add_argument("--axis_label_size",
                        type=int,
                        default=8,
                        help="Axis label font size")
    
    parser.add_argument("--tick_label_size",
                        type=int,
                        default=8,
                        help="Axis tick label font size")
    parser.add_argument("--fignum", type=str, help="Figure number")
 
    return parser.parse_args()


def main():
    args = get_args()


    #techs = 'hprc', 'ont', 'vienna'
    platforms = ('PacBio HiFi', 'Oxford Nanopore', 'Oxford Nanopore')

    F = {'PacBio': 0,
         'Nanopore': 0,
         'PacBio Nanopore': 0}

    data = []
    for line in sys.stdin:
        chrom, start, end, svtype, hprc, ont, vienna = line.rstrip().split()
        hprc = int(hprc)
        ont = int(ont)
        vienna = int(vienna)

        if hprc >= 1:
            F['PacBio'] += 1
        if ont >= 1:
            F['Nanopore'] += 1
        if vienna >= 1:
            F['Nanopore'] += 1
        if hprc >= 1 and (ont >= 1 or vienna >= 1):
            F['PacBio Nanopore'] += 1

    example = from_memberships(
            [['PacBio'],
             ['Nanopore'],
             ['PacBio', 'Nanopore']],
            data = [F['PacBio'], F['Nanopore'], F['PacBio Nanopore']])

    fig, ax = plt.subplots(figsize=(args.width, args.height))
    plot(example)
    fig.tight_layout()
    plt.savefig(args.out_file)

if __name__ == '__main__':
    main()

