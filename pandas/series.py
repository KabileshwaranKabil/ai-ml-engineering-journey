import pandas as pd

print(f'version: {pd.__version__}') # version


age = [23,24,25,12,10,54,23]

series = pd.Series(age)
print(series)


print(series.loc[1])


marks = [72,54,76,87,98,76]

mseries = pd.Series(marks,index=['Mano','Gukesh','Dinesh','Leo','Kiran','George'])

print(mseries)
print(mseries.iloc[2]) # used even the index is different



series = pd.Series({
	"Kabilesh":23,
	"Dhanush":21,
	"Manomohan":56
	})

print(series)

# Filtering
print(series[series < 25 ])




