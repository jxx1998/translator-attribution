import re

zsh_file = open('ZSH-Macbeth-Preprocessed1.txt', 'r')
lines = zsh_file.readlines()
zsh_file.close()
processed = []


# for line in lines:
#     line = line.strip()
#     if line:
#         processed.append(line + "\n")

ongoingDialogue = False
prev = ""
for line in lines:
    line = line.strip()
    if ' ' in line:
        if prev:
            processed.append(prev + '\n')
        ongoingDialogue = True
        prev = line[line.find(' ') + 1:]
    elif line[0] == "第":
        if prev:
            processed.append(prev + '\n')
        processed.append(line + '\n')
        prev = ""
        ongoingDialogue = False
    else:
        prev += line


out_file = open("ZSH-Macbeth-Preprocessed2.txt", "w+")
out_file.writelines(processed)
out_file.close()
