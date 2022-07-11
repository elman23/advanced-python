import re


def main():
    string = "This is the string to replace."
    print("Before replacing:\t {}".format(string))
    replaced = re.sub("to replace", "replaced", string, 0)
    print("After replacing:\t {}".format(replaced))


if __name__ == '__main__':
    main()