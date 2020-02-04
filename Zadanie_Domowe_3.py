import glob, os
import pandas as pd
from tkinter.filedialog import askdirectory

# Obliczanie wartości i zapisywanie do csv
def CalculatePlease(input_file, input_path):
    myFile = pd.read_csv(input_file, sep=',')
    myFile["Difference"] = myFile["Close"]-myFile["Open"]
    myFile.to_csv(input_path+"/" + input_file[:len(input_file)-4]+"_Output.csv", sep=",")

# Zapytanie o ścieżkę
path=askdirectory()

os.chdir(path)
for file in glob.glob("*.csv"):
    CalculatePlease(file,path)