import os
import glob

directory = '/Users/arunprajapati/Downloads/[FreeCourseSite.com] Udemy - Data Science Natural Language Processing (NLP) in Python/Data Science Natural Language Processing (NLP) in Python'

srt_files = glob.glob(glob.escape(directory) +'/**/*.srt',recursive=True)

for file in srt_files:
    try:
        os.remove(file)
    except Exception as e:
        print(e)
    else:
        print(f"{file}Removed successfully")