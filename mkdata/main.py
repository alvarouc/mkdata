from sklearn.datasets import make_classification
import pandas as pd
import argparse


def make_parser():
    parser = argparse.ArgumentParser(description='Generate data')
    parser.add_argument('--nsamples', type=int, default=1000,
                        help='Number of samples')
    parser.add_argument('--nvars_informative', type=int, default=10,
                        help='Number of informative variables')
    parser.add_argument('--nvars_redundant', type=int, default=10,
                        help='Number of redundant variables')

    parser.add_argument('--nclusters', type=int, default=3,
                        help='Number of clusters')
    return parser


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    nvars = args.nvars_informative + args.nvars_redundant
    print('Generating dataset with {} samples, {} variables, and {} clusters ...'.format(
        args.nsamples, args.nvars, args.nclusters))

    X, y = make_classification(n_samples=args.nsamples, n_features=nvars,
                               n_informative=args.nvars_informative,
                               n_redundant=args.nvars_redundant,
                               n_repeated=0, n_classes=args.nclusters,
                               n_clusters_per_class=1)
