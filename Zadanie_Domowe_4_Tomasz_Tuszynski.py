import os
from tkinter.filedialog import askdirectory

def check_size(input_file):
    size = 0
    if os.path.isdir(input_file):
        for file in os.listdir(input_file):
            size += check_size(os.path.join(input_file, file))
    else:
        size += os.path.getsize(input_file)
    return size

path=askdirectory()
result = check_size(path)
result2 = round(result/10**6,2)
print("Wynik to "+ str(result) + "bajtów = " + str(result2) + " Megabajtów")