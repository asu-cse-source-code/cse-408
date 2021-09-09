import os

# Read all files from data folder
def scan_folder(parent):
    # iterate over all the files in directory 'parent'
    for file_name in os.listdir(parent):
        if file_name.endswith(".txt"):
            # if it's a txt file, print its name (or do whatever you want)
            print(file_name)
        else:
            current_path = "".join((parent, "/", file_name))
            if os.path.isdir(current_path) and current_path != 'Code':
                # if we're checking a sub-directory, recursively call this method
                scan_folder(current_path)

def main():
    scan_folder(".")



if __name__ == "__main__":
    main()