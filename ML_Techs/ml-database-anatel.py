import pandas as pd
from pandas_ods_reader import read_ods

dados = read_ods("Anatel.ods", 1)

a = 2
b = 10
print(a + b)

