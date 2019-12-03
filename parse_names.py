import fileinput
import regex
import sys

html = open(sys.argv[1], "r")
# name_list = open(sys.argv[2], "a")
for line in html:
    name_search = regex.search("<li>(.*)</li>", line)
    name_search_long = regex.search("<li><a(.*)>(.*)</a>", line)
    if name_search and len(line) < 40:
        print("{}".format(name_search.group(1)))
        # name_list.write("{}\n".format(name_search.group(1)))
    if name_search_long:
        name = name_search_long.group(2)
        print("{}".format(name))
        # name_list.write("{}\n".format(name_search_long.group(2)))