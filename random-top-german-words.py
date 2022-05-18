#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import codecs

print("""Please choose the number of the option you want and press ENTER:
1- Top 2000 words (Wikipedia)
2- Top 5k words (Internet corpus)
3- Top 10k words (uni-leipzig.de)
4- Top 25k words (OpenSubtitles 2016)
5- Top 50k words (Internet corpus)
""")

c = raw_input()
if c == "1":
    file_name = "./docs/top-2000.txt"
elif c == "2":
    file_name = "./docs/top-5k.txt"
elif c == "3":
    file_name = "./docs/top-10k.txt"
elif c == "4":
    file_name = "./docs/top-25k.txt"
elif c == "5":
    file_name = "./docs/top-50k.txt"

raw_data = open(file_name, 'r').read().decode("utf-8")
words_array = raw_data.split(',')

words_count = len(words_array)

print("Press ENTER to print new words, or CTRL+C to exit...")

text = ""
with codecs.open("additional.txt", "a+", "utf-8") as f:
    while True:
        c = raw_input()
        if c == '':
            i = random.randint(1, words_count)^M
            print(words_array[i])
            text = words_array[i]
        elif c == 'quit':
            break
        else:
            f.write("<item><word>" + text + "</word>\n" + "<misc>" + c.decode("utf-8") + "</misc>\n</item>\n")

exit()
