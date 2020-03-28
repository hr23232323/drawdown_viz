import pandas as pd
import numpy as np
import glob
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def main():
	list_of_files = glob.glob("raw_data/*")
	#create_main_chart(list_of_files)
	create_side_chart(list_of_files)



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


def create_main_chart(list_of_files):
	plt.style.use('seaborn-darkgrid')
	# create a color palette
	palette = plt.get_cmap('tab10')
	fig, ax = plt.subplots(figsize=(10, 6))

	num=0
	for file in list_of_files:
		num+=1
		file_label = re.search("\\d+", file).group(0)
		
		#print(file, file_label)
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)
		
		if(file == "raw_data\\2020_1.csv"):
			ax.plot(df['day'], df['value'], marker='', color="red", linewidth=1.5, alpha=1, label=file_label)
		else:
			ax.plot(df['day'], df['value'], marker='', color=palette(num), linewidth=1, alpha=0.6, label=file_label)

	# Add legend
	plt.legend(loc=1, ncol=2)
	plt.title("Comparing the COVID-19 bear market to others from history", loc='left', fontsize=12, fontweight=0, color='black')
	plt.xlabel("Days into the bear market", fontsize=12)
	plt.ylabel("Value of a $10,000 investment", fontsize=12)
	fmt = '${x:,.0f}'	
	tick = mtick.StrMethodFormatter(fmt)
	ax.yaxis.set_major_formatter(tick)
	plt.show()



def create_side_chart(list_of_files):
	plt.style.use('seaborn-darkgrid')
	# create a color palette
	palette = plt.get_cmap('tab10')
	fig, ax = plt.subplots(figsize=(14, 7))

	# custom ranges
	custom_xlim = (0, 300)
	custom_ylim = (5000, 10000)

	num = 0
	for i in range(1, 10):
		num+=1
		file = list_of_files[i]
		ax = plt.subplot(3, 3, i)

		file_label = re.search("\\d+", file).group(0)
		df_temp = pd.read_csv(file)
		df = process_df(df_temp)

		if(file == "raw_data\\2020_1.csv"):
			ax.plot(df['day'], df['value'], marker='', color="red", linewidth=1.5, alpha=1, label=file_label)
		else:
			ax.plot(df['day'], df['value'], marker='', color=palette(num), linewidth=1, alpha=0.6, label=file_label)

		# Not ticks everywhere
		if num in range(7) :
			plt.tick_params(labelbottom='off')
		if num not in [1,4,7] :
			plt.tick_params(labelleft='off')

		plt.legend(loc=1, ncol=1, handlelength=0)
		fmt = '${x:,.0f}'	
		tick = mtick.StrMethodFormatter(fmt)
		ax.yaxis.set_major_formatter(tick)
		plt.setp(ax, xlim=custom_xlim, ylim=custom_ylim)

	# Axis title
	fig.text(0.5, 0.02, 'Days into the bear market', ha='center', va='center')
	fig.text(0.06, 0.5, 'Value of a $10,000 investment', ha='center', va='center', rotation='vertical')

	plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    main()
