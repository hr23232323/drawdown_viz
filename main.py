import pandas as pd
import numpy as np
import glob

def main():
	#df = pd.read_csv("raw_data/1990_1.csv")
	#print(df)
	list_of_files = glob.glob("raw_data/*")

	for file in list_of_files:
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)
		print(df)


def process_df(dataframe):
	# Add new columns for day and % change
	dataframe["day"] = dataframe.index
	dataframe["change"] = (100*((dataframe.Open-dataframe.Open.shift(1))/dataframe.Open))
	
	# Drop extra columns
	dataframe = dataframe.drop(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
	
	#Drop last row (no change)
	dataframe.drop(dataframe.head(1).index,inplace=True)
	return dataframe




if __name__ == "__main__":
    # execute only if run as a script
    main()



