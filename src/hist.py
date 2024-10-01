import matplotlib.pyplot as plt
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(description="Plot a histogram and save it to a file.")
    parser.add_argument('--out_file', type=str, help="The file name to save the plot")
    parser.add_argument('--log', action='store_true', help="Use a log scale for the y-axis")
    parser.add_argument('--bins', type=int, help="The number of bins to use in the histogram", default=10)
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


    return parser.parse_args()


def main():
    args = get_args()

    data = []
    for line in sys.stdin:
        data.append(float(line))

    fig, ax = plt.subplots(figsize=(args.width, args.height))

    ax.hist(data, bins=args.bins)

    if args.log:
        ax.set_yscale('log')

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

    fig.tight_layout()
    fig.savefig(args.out_file)
    fig.savefig(args.out_file+".svg", format='svg',transparent=True)

if __name__ == '__main__':
    main()

