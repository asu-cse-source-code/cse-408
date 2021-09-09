import os
import re

def scan_folder(parent, text_data = ''):
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):
        if file_name.endswith(".txt"):
            # if it's a txt file, print its name (or do whatever you want)
            #print(file_name)
            with open(f'{parent}/{file_name}') as data:
                text_data += data.read()
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path) and current_path != 'Code':
                # if we're checking a sub-directory, recursively call this method
                text_data += scan_folder(current_path)
    return text_data

def cse408_bow(filepath, voc):
    text_data = scan_folder(filepath)
    text_data = re.sub(r'[^\w\s]', '', text_data).replace('\n', '')
    print(text_data.split())
    

cse408_bow('../Data/kNN/', [])