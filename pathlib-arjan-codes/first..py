# introduction to pathlib library

# if we use strings for paths, we get into problems
# 1) combining paths is hard
# 2) linux vs windows problem
# 3) some information is hard to get
# 4) its buggy 

# Pathlib is an object oriented way of representing paths

from pathlib import Path

def main():

    # get current working directory
    print("Current working directory {Path.cwd}")
    print("Home directory {Path.home}")

    path = Path("") # we created a path object but... doesnt' check the path exisis or not.
    print(path.exists()) # check if path exisists or not.

    newPath = Path("") / "user" / "Downloads"  # here / operator is oeverloaded so that we can just write our paths just like we write for strings
    # this is then translated to the respective linux or windows path

       

    # we can also get absolute path of a path by just using .resolve()
    path = Path("first.py")
    print(path)
    print(path.resolve()) # it returns the absolute path of the first.py file

    full_path = path.resolve()

    print(f"Parent: {full_path.parent.parent}")
    print(f"Name: {full_path.name}")
    print(f"Stem: {full_path.stem}")
    print(f"suffix: {full_path.suffix}")
    print(f"Is directory: {full_path.is_dir()}")
    print(f"Is file: {full_path.is_file()}")



if __name__ == "__main__":
    main()