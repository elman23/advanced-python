import re


def main():
    line = "I think I understand regular expressions!"
    
    match_result = re.match("think", line, re.M | re.I)
    if match_result:
        print("Match found: {}!".format(match_result.group()))
    else:
        print("No match found!")
    
    search_result = re.search("think", line, re.M | re.I)
    if search_result:
        print("Search found: {}!".format(search_result.group()))
    else:
        print("No search found in search!")


if __name__ == '__main__':
    main()