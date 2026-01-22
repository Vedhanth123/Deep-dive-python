
from pathlib import Path
from os import chdir

def main():

    new_file = Path.cwd() / 'test_file.txt'

    new_file.touch() # creates a file

    new_file.write_text("Hello joker!")

    new_file.unlink() # to delete the file

    new_dir = Path.cwd() / 'new_dir'

    new_dir.mkdir() # creates a directory

    chdir(new_dir) # changes using os module

    print(f"CWD {Path.cwd()}") # it reflects it too

    new_dir.rmdir() # remove the directory toooo.

    

if __name__ == '__main__':
    main()