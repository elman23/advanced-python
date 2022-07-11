import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-v",
        "--verbose",
        help="Verbose output.",
        action="store_true"
    )
    group.add_argument(
        "-q",
        "--quiet",
        help="Quiet output.",
        action="store_true"
    )
    parser.add_argument(
        "num",
        help="The Fibonacci number you wish to calculate.",
        type=int
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output result to a file.",
        action="store_true"
    )

    args = parser.parse_args()

    result = fib(args.num)
    
    if args.verbose:
        print("The {}th Fibonacci number is {}.".format(args.num, result))
    elif args.quiet:
        print("Result: {}".format(result))
    else:
        print("Fib({}) = {}".format(args.num, result))

    if (args.output):
        with open("fibonacci.txt", "a") as f:
            f.write("The {}th Fibonacci number is {}.\n".format(args.num, result))


if __name__ == '__main__':
    main()

