import sys
import json
import logParser

def parse_log(file):
    if file:
        a = logParser.main(file)
        resp = json.dumps(a,sort_keys=False)
        return a
    else:
        return "File cannot be read"
n = len(sys.argv)
if n < 2:
    print("Missing filename")
else:
    print(parse_log(sys.argv[1]))
