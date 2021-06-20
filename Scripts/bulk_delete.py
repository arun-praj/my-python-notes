

#Add below line to line no.1 to make command folder and 
#!/usr/local/bin/python3

# Rename to bulk_delete.command
# In Terminal make the Python script file executable by running "chmod +x my_python_script.command"

import os
import glob
from time import perf_counter

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ColorComment(Bcolors):
    def warning(self, cmt):
        print(f"{self.WARNING}{cmt}{self.ENDC}")
    def danger(self, cmt):
        print(f"{self.FAIL}{cmt} {self.ENDC}")
    def success(self, cmt):
        print(f"{self.OKGREEN}{cmt} {self.ENDC}")
    def underline(self, cmt):
        print(f"{self.UNDERLINE}{cmt} {self.ENDC}")
    
colorComment = ColorComment()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def del_bulk(path_without_filename, extension):
    """ Delete Bult """
    directory = path_without_filename
    success = True
    count = 0
    files = glob.glob(glob.escape(directory) + f'/**/*.{extension}', recursive=True)
    print(f"\n{files.__len__()} {extension} files found.\n")

    if files.__len__() == 0 or input(colorComment.warning('Are you sure? (Y/N) : ')) not in ['y', "Y", "yes"]:
        return False
        
    start = perf_counter()
    for file in files:
        try:
            os.remove(file)
            count = count+1
        except Exception as e:
            print(e)
            success = False
            colorComment.danger(f"Error Occured: {e}") 
            break
        else:
            print(f"{count}. {file}:  Removed successfully\n")
    end = perf_counter()

    if success != False:
        colorComment.success(f"\n{count} {extension} files deleted in {end - start} second/s.") 
    return None

    

def info(path_without_filename):
    print("\n" + "______________________________________"*2)
    print("How to: Paste this file to a folder of which files you want to delete.")
    print("______________________________________"*2+ "\n" )
    print(f"You ran your script from :{path_without_filename}")
    colorComment.warning('Warning: All the files you choose from this directory and subdirectory will get deleted permanemtly')
    print("______________________________________"*2+ "\n" )



if __name__ == "__main__":
    clear()
    extension_not_allowed = ['*']
    path_without_filename = "/".join(__file__.split('/')[:-1])
    info(path_without_filename)
    ans = input("Enter the extension (srt,jpeg,mp4) : ").lower()
    if ans not in extension_not_allowed:
        del_bulk(path_without_filename, extension=ans)
    else:
        colorComment.danger("Not allowed")


