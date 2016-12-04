import numpy, collections

from collections import Counter

# Print absolute path of files in current directory #

def print_path():
    for file in os.listdir(os.getcwd()):
        print(os.path.abspath(file))

# Read students file and generate languages list #

def gen_lang():
    doc = list(open('/Users/SMcGhin/Documents/IntroPython2016/Examples/Session01/students.txt', 'r'))
    data = []
    for line in doc[1:-1]:
        students, languages = line.strip().split(':')
        data.append(languages)
        data = [langs.split(',')[0] for langs in data]
    print(Counter(sorted(data)))




