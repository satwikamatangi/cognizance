#Written by Satwika
import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])
newSeries = ser.str.title()
print(newSeries)