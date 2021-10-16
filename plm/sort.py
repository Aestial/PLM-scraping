import json 
import sys

with open(sys.argv[1]) as f:
    content = f.readlines()

content = [json.loads(x.strip()) for x in content]

output = sorted(content, key=lambda k: k[str(sys.argv[3])]) 

with open(sys.argv[2], 'w') as f:
    for item in output:
        f.write("%s\n" % item)