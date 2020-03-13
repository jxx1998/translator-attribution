READ_PATH = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Macbeth.txt"
WRITE_PATH = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Macbeth-Preprocessd1.txt"

READ_PATH2 = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Macbeth-Preprocessd1.txt"
WRITE_PATH2 = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Macbeth-Preprocessed-Final.txt"

# with open(READ_PATH) as read_f:
#     with open(WRITE_PATH, 'w') as write_f:
#         content = read_f.readlines()
#         str = ""
#         for line in content:
#             # Type 3
#             if line == "\n":
#                 continue
#             # Type 1, 2, 6
#             elif line[0] in "第[" and line[1] != "伶":
#                 write_f.write(line)
#             else:
#                 # Type 5
#                 if line[0] == "　":
#                     str += line.strip()
#                 else:
#                     if str:
#                         write_f.write(str + '\n')
#                     str = line.strip()


with open(READ_PATH2) as read_f:
    with open(WRITE_PATH2, 'w') as write_f:
        content = read_f.readlines()
        prev = ""
        for line in content:
            line = line.replace('　', '').strip()
            if line[0] == "第" or (line[0] == "[" and line[-1] == "]") or line[-1] in "！。？":
                write_f.write(prev + line + "\n")
                prev = ""
            else:
                prev += line
