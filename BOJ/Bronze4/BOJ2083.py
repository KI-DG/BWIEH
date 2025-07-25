while(True):
    name, old, weight = map(str, input().split())

    if name == "#":
        break

    if int(old) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
