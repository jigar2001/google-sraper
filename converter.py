import pandas as pd

def convert_to_excel(scrap_data):
	df = pd.DataFrame(scrap_data)  
	df.to_excel("scrapdata.xlsx", index = False)