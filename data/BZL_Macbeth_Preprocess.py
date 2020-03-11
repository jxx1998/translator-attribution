import re

bzl_file = open('BZL-Macbeth-Preprocessed1.txt', 'r')
lines = bzl_file.readlines()
bzl_file.close()
processed1 = []


for line in lines:
    line = re.sub(r'\d+', '', line)
    if line:
        processed1.append(line)

characters = ["女巫甲 ",
                        ]
for line in processed1:


out_file = open("BZL-Macbeth-Preprocessed2.txt", "w+")
out_file.writelines(processed)
out_file.close()
