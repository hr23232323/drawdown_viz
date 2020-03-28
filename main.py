import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


def main():
	#df = pd.read_csv("raw_data/1990_1.csv")
	#print(df)
	list_of_files = glob.glob("raw_data/*")
	# style
	plt.style.use('seaborn-darkgrid')
	for file in list_of_files:
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)
		
		if(file == "raw_data\\2020_1.csv"):
			plt.plot(df['day'], df['value'], marker='', color="orange", linewidth=1.5, alpha=1)
		else:
			plt.plot(df['day'], df['value'], marker='', color="grey", linewidth=1, alpha=0.5)


	plt.title("Comparing the COVID-19 bear market to others from history", loc='left', fontsize=10, fontweight=0, color='black')
	plt.xlabel("Days into the bear market", fontsize=12)
	plt.ylabel("Value of a $10,000 investment", fontsize=12)
	#plt.xscale("log")
	plt.show()





def process_df(dataframe):
	# Add new columns for day and % change
	dataframe["day"] = dataframe.index
	dataframe["change"] = (1+(1*((dataframe.Open-dataframe.Open.shift(1))/dataframe.Open)))
	dataframe["value"] = 10000 * dataframe.change.cumprod()
	
	# Drop extra columns
	dataframe = dataframe.drop(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
	
	#Drop last row (no change)
	dataframe.drop(dataframe.head(1).index,inplace=True)
	return dataframe




if __name__ == "__main__":
    # execute only if run as a script
    main()



