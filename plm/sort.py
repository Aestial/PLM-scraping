import json 

with open("medicines.jl") as f:
    content = f.readlines()

content = [json.loads(x.strip()) for x in content]

output = sorted(content, key=lambda k: k['marca']) 

with open('sorted-medicines.jl', 'w') as f:
    for item in output:
        f.write("%s\n" % item)