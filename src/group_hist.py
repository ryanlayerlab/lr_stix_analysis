import matplotlib.pyplot as plt
import argparse
import sys
import numpy as np

def get_args():
    parser = argparse.ArgumentParser(description="Plot a histogram and save it to a file.")
    parser.add_argument('--in_file', type=str, help="SV sample counts")
    parser.add_argument('--out_file', type=str, help="The file name to save the plot")
    parser.add_argument('--log', action='store_true', help="Use a log scale for the y-axis")
#    parser.add_argument('--bins', 
#                        nargs='+',
#                        type=float,
#                        help="Histogram bin edges (e.g., 0 10 20)")
#    parser.add_argument('--bin_names',
#                        nargs='+',
#                        type=str,
#                        help="Names for the bins (e.g., '0' '1-10' '11-20')")
    parser.add_argument('--height', type=int, help="The height of the histogram", default=4)
    parser.add_argument('--width', type=int, help="The width of the histogram", default=4)
    parser.add_argument('--title', type=str, help="The title of the histogram")
    parser.add_argument('--xlabel', type=str, help="The x-axis label")
    parser.add_argument('--ylabel', type=str, help="The y-axis label")

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

    total = []
    seen  = []

    with open(args.in_file, 'r') as f:
        for line in f:
            A = line.rstrip().split()
            sv = (A[0],int(A[1]),int(A[2]),int(A[4]))
            sv_len = int(A[2]) - int(A[1])
            depth = int(A[4])

            if depth > 0:
                seen.append(sv_len)

            total.append(sv_len)

    bins = [0,
            1000,
            2000,
            3000,
            4000,
            5000,
            10000,
            50000]
    labels = ['0-1kb',
              '1kb-2kb',
              '2kb-3kb',
              '3kb-4kb',
              '4kb-5kb',
              '5kb-10kb',
              '10kb-50kb']
    
    
    total_couts, total_bins = np.histogram(total, bins=bins)
    seen_couts, seen_bins = np.histogram(seen, bins=bins)

    print(total_couts)
    print(seen_couts)

    fig, ax = plt.subplots(figsize=(args.width, args.height))


    ax.bar(np.arange(len(total_couts))-0.2, total_couts, width=0.4, align='center', label='Total')
    ax.bar(np.arange(len(seen_couts))+0.2, seen_couts, width=0.4, align='center', label='Seen')

    if args.title:
        ax.set_title(args.title, fontsize=args.axis_label_size, loc='left')

    if args.xlabel:
        ax.set_xlabel(args.xlabel)

    if args.ylabel:
        ax.set_ylabel(args.ylabel)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(axis='both',
                   which='major',
                   labelsize=args.axis_label_size,
                   width=args.tick_line_width,
                   length=args.tick_line_length)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.tick_params(axis='x', labelrotation=45)

    ax.legend(frameon=False, fontsize=args.axis_label_size)

    if args.fignum:
        ax.annotate(args.fignum,
                    xy=(.025, .975), xycoords='figure fraction',
                    horizontalalignment='left', verticalalignment='top',
                    fontsize=12)

    fig.tight_layout()
    fig.savefig(args.out_file)
    fig.savefig(args.out_file+".svg", format='svg',transparent=True)

if __name__ == '__main__':
    main()

