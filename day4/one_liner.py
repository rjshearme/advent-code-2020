##### Part One ####

print(sum(1 for d in open("i").read().split("\n\n") if d.count(":")-d.count("ci")==7))


##### Part Two #####
print("There are {} valid passports".format(len([1 for d in open("input.txt").read().split("\n\n") if all([__import__("re").findall(p, d) for p in [r"\bpid:\d{9}\b", r"\beyr:20(2\d|30)\b", r"\biyr:20(1\d|20)\b", r"\bhgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)\b", r"\bhcl:#[\da-f]{6}\b", r"\becl:(amb|blu|brn|gry|grn|hzl|oth)\b", r"\bbyr:(19[2-9]\d|200[012])\b"]])])))
