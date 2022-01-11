import os

path = ""

text_files = glob.glob(path + "/**/File.py", recursive = True)

print(text_files)