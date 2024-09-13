import matplotlib.pyplot as plt
import argparse
import sys
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description="Plot a histogram and save it to a file.")
    parser.add_argument('--out_file', type=str, help="The file name to save the plot")
    parser.add_argument('--log', action='store_true', help="Use a log scale for the y-axis")
    parser.add_argument('--bins', 
                        nargs='+',
                        type=float,
                        help="Histogram bin edges (e.g., 0 10 20)")
    parser.add_argument('--bin_names',
                        nargs='+',
                        type=str,
                        help="Names for the bins (e.g., '0' '1-10' '11-20')")
    parser.add_argument('--height', type=int, help="The height of the histogram", default=4)
    parser.add_argument('--width', type=int, help="The width of the histogram", default=4)
    parser.add_argument('--title', type=str, help="The title of the histogram")
    parser.add_argument('--xlabel', type=str, help="The x-axis label")
    parser.add_argument('--ylabel', type=str, help="The y-axis label")

    return parser.parse_args()


def main():
    args = get_args()

    data = []
    for line in sys.stdin:
        data.append(float(line))

    fig, ax = plt.subplots(figsize=(args.width, args.height))

    couts, bins = np.histogram(data, bins=args.bins)

    ax.bar(args.bin_names, couts, width=0.8, align='center')

    if args.title:
        ax.set_title(args.title)

    if args.xlabel:
        ax.set_xlabel(args.xlabel)

    if args.ylabel:
        ax.set_ylabel(args.ylabel)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    fig.tight_layout()
    fig.savefig(args.out_file)

if __name__ == '__main__':
    main()

