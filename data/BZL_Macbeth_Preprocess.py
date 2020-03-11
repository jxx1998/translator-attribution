import re

bzl_file = open('BZL-Macbeth-Preprocessed3.txt', 'r')
lines = bzl_file.readlines()
bzl_file.close()
processed = []


# for line in lines:
#     line = re.sub(r'\d+', '', line)
#     if line:
#         processed1.append(line)
#
# characters = "女巫甲 |女巫乙 |女巫丙 |顿 |玛 |队长 |列 |麦 |麦夫人 |多 |罗 |门 |安 |凯 |弗 |西 |士兵 |小西 |瑟 |医 |三女巫 |使 |班 |麦克德夫 "
# processed2 = []
# for line in processed1:
#     line = line.strip()
#     if line:
#         parsed = [token.strip() + '\n' for token in re.split(characters, line) if token]
#         match = re.search(characters, line)
#         if match:
#             assert match.pos == 0
#             processed2.extend(parsed)
#         else:
#             assert len(parsed) == 1
#             if processed2:
#                 processed2[-1] = processed2[-1].strip() + parsed[0]

prev = ""
for line in lines:
    line = re.sub(r' ', '', line)
    if line[-2] in "。?!":
        processed.append(prev + line)
        prev = ""
    else:
        prev += line.strip()


out_file = open("BZL-Macbeth-Preprocessed-Final.txt", "w+")
out_file.writelines(processed)
out_file.close()
