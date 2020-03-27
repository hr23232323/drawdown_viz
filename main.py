import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


def main():
	#df = pd.read_csv("raw_data/1990_1.csv")
	#print(df)
	list_of_files = glob.glob("raw_data/*")
	num = 0
	for file in list_of_files:
		num+=1
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)
		print(file)
		print(df)

		palette = plt.get_cmap('Set1')
		plt.plot(df['day'], df['value'], marker='', color=palette(num), linewidth=1, alpha=0.9)
		plt.title("Drawdown Graph", loc='left', fontsize=12, fontweight=0, color='orange')
		plt.xlabel("Days")
		plt.ylabel("Change")
	#plt.show()





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



