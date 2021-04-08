import csv
import pandas as pd
from main import df

print("Importem llibreries per carragar les variables")



with open('output.csv', 'w+') as f:
    f.write(df)
    
print("S'ha creat un arxiu csv output.csv amb les dades obtingudes")
