a = 1
import os
import glob

directory = '/Users/arunprajapati/Downloads/[FreeCourseSite.com] Udemy - Data Science Natural Language Processing (NLP) in Python/Data Science Natural Language Processing (NLP) in Python/7. NLTK Exploration'

g = glob.glob(directory + '**/*',recursive=True)

os.listdir(directory)
print(g)