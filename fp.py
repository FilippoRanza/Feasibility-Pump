#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from argparse import ArgumentParser
from fp_engine import feasibility_pump, load_instance


def arg_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--instance", required=True, help="specify the instance to solve"
    )

    return parser.parse_args()


def main():
    args = arg_parser()
    c, A, b = load_instance(args.instance)
    sol, stat = feasibility_pump(c, A, b)
    if stat:
        print("Solution Found:")
        print(sol)
    else:
        print("Unable to find a feasible solution")


if __name__ == "__main__":
    main()
