import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


def main():
	#df = pd.read_csv("raw_data/1990_1.csv")
	#print(df)
	list_of_files = glob.glob("raw_data/*")
	num = 0
	plt.style.use('seaborn-darkgrid')
	for file in list_of_files:
		num+=1
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)
		print(file)
		print(df)

		if(file == "raw_data\\2020_1.csv"):
			plt.plot(df['day'], df['value'], marker='', color="orange", linewidth=1.5, alpha=1)
		else:
			plt.plot(df['day'], df['value'], marker='', color="grey", linewidth=1, alpha=0.5)


	# style
	print(plt.style.available)

	plt.title("Drawdown Graph", loc='left', fontsize=12, fontweight=0, color='orange')
	plt.xlabel("Days")
	plt.ylabel("Change")
	#plt.xscale("log")
	plt.show()





def process_df(dataframe):
	# Add new columns for day and % change
	dataframe["day"] = dataframe.index
	dataframe["change"] = (1+(1*((dataframe.Open-dataframe.Open.shift(1))/dataframe.Open)))
	dataframe["value"] = dataframe.change.cumprod()
	
	# Drop extra columns
	dataframe = dataframe.drop(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
	
	#Drop last row (no change)
	dataframe.drop(dataframe.head(1).index,inplace=True)
	return dataframe




if __name__ == "__main__":
    # execute only if run as a script
    main()



