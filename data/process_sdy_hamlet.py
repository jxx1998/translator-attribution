READ_PATH = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Hamlet-NoAnnotations.txt"
WRITE_PATH = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Hamlet-Preprocess-Single-Lines-With_Names.txt"

READ_PATH2 = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Hamlet-Preprocessed-No_Names.txt"
WRITE_PATH2 = "/Users/zhengl/Downloads/translator-attribution/data/SDY-Hamlet-Preprocessed-Final.txt"

'''
Types of lines:
1. Begins with '[', but doesn't end with ']'. Characters move on/off stage.
2. Begins with '[', end with ']'. Other things like establish sentences.
*** Unless the next character is "伶"
3. New line characters
4. First line of a character: starts with a name, no indent
5. Later lines of the same character: starts with 4 spaces
5.5 Sometimes they don't add the spaces
6. Begins with '第'. Separates acts and scenes

** Note that some of the formattings seemed to be inconsistent
*** Currently, the names are still inside, wondering if we should
'''
def process():
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
            for line in content:
                write_f.write(line.replace('　', ''))

if __name__ == '__main__':
    process()
