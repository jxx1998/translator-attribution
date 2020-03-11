import re

bzl_file = open('BZL-Macbeth-Preprocessed1.txt', 'r')
lines = bzl_file.readlines()
bzl_file.close()
processed1 = []


for line in lines:
    line = re.sub(r'\d+', '', line)
    if line:
        processed1.append(line)

characters = "女巫甲 |女巫乙 |女巫丙 |顿 |玛 |队长 |列 |麦 |麦夫人 |多 |罗 |门 |安 |凯 |弗 |西 |士兵 |小西 |瑟 |医 |三女巫 "
processed2 = []
for line in processed1:
    line = line.strip()
    parsed = [token.strip() + '\n' for token in re.split(characters, line) if token]
    print(parsed)
    processed2.extend(parsed)


out_file = open("BZL-Macbeth-Preprocessed3.txt", "w+")
out_file.writelines(processed2)
out_file.close()
