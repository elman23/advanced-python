import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        help="The Fibonacci number you wish to calculate",
        type=int
    )

    args = parser.parse_args()

    result = fib(args.num)
    print("The {}th Fibonacci number is {}".format(args.num, result))


if __name__ == '__main__':
    main()

