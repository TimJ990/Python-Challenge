d = {}

name = "Bob"

names = ["Bob", "Carl", "Carl"]

for name in names:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

candidates = list(d.keys())
print(candidates)
total = sum(d.values())
for name, count in d.items():
    print(name, count, count/total)
