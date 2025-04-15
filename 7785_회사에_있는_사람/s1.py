"""
4
Baha enter
Askar enter
Baha leave
Artem enter

Askar
Artem
"""

n = int(input())
log_dict = {}
name_set = set()
for i in range(n):
    name, log = map(str, input().split())
    log_dict[name] = log
    name_set.add(name)

result = []
for i in name_set:
    if log_dict[i] == 'enter':
        result.append(i)

result.sort(reverse=True)
for i in result:
    print(i)
