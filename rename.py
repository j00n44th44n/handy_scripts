import os
from os import path, listdir

def main():
    print("Desire Text to Remove")
    key_word = input()
    print("Optionally Desire Text to Replace")
    replace_word = input()
    current_path = os.getcwd()
    for filename in listdir(current_path):
        try:
            if filename == "main.py" or filename == ".idea":
                continue
            new_filename = filename.replace(key_word, replace_word)
            src = path.join(current_path,filename)
            dst = path.join(current_path,new_filename)
            os.replace(src,dst)
        except:
            pass


main()