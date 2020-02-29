import re

bzl_file = open('BZL-Hamlet-Preprocessed1.txt', 'r')
lines = bzl_file.readlines()
bzl_file.close()
character = ''
processed = []
for line in lines:
    if len(line) < 2:
        continue
    if line[1] == ' ' and character:
        character = re.sub(r'\d+', '', character)
        character = re.sub(r'\u2460|\u2461|\u2462|\u2463|\u2464|\u2465|\u2466|\u2467|\u2468|\u2469', '', character, flags=re.UNICODE)
        processed.append(character + '\n')
        character = ''
    tokenized = line.split()
    if tokenized[0].isnumeric():
        continue
    if tokenized[-1].isnumeric():
        tokenized = tokenized[:-1]
    if len(tokenized[0]) <= 1:
        tokenized = tokenized[1:]
    character += "".join(tokenized)
if character:
    processed.append(character + '\n')
out_file = open("BZL-Hamlet-processed-final.txt", "w+")
out_file.writelines(processed)
out_file.close()