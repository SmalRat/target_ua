count = 0
with open("base.lst", "r", encoding="utf-8") as dictionary:
    with open("new_base.lst", "w", encoding="utf-8") as new:
        lines = dictionary.readlines()
        for i in range(len(lines)):
            if len(lines[i].lower().strip().split()[0]) < 6 and lines[i].lower()[0] == "є":
                new.writelines(lines[i] + "\n")
                count+=1
print(count)

