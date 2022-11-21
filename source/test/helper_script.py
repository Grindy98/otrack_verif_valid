import re
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        for l in infile.readlines():
            x = re.search(r'run\((\[.*\])\)', l)
            if x:
                lst = eval(x.groups()[0])
                lst = [ '"' + x + '"' if (' ' in x) else x for x in lst]
                print('otrack ' + ' '.join(lst))
