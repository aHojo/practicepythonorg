from datetime import datetime

files = ["C:\\Users\Jocke\\Documents\Programming\\Python\Merging\\file1.txt", "C:\\Users\Jocke\\Documents\Programming\\Python\Merging\\file1.txt", "C:\\Users\Jocke\\Documents\Programming\\Python\Merging\\file1.txt"]

now = datetime.now()
filename = now.strftime("%Y-%m-%d-%H-%M-%S")

def mergeFile(filepath):
  print(filepath)
  with open(filepath, 'rt', encoding='UTF-8') as f:
    temp = f.read()
    with open(f"{filename}.txt", 'at', encoding='UTF-8') as merger:
      merger.writelines(temp +"\n")

for file in files:
  mergeFile(file)