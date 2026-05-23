import pandas as pd
import numpy as np

# Series
a_dict = {'1st': 1, '2nd': 3, '3rd': 5, '4th':7, '5th': 9}
ser = pd.Series(a_dict)
print(ser)

print('Range access:')
print(ser[0:3])

print('Access: Index number')
# print(ser[1])

print('Access: Index label')
print(ser['2nd'])



# Data frames
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)


df = pd.read_csv('pandas/data.csv')
print(df.to_string())

