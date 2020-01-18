import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import pprint as pp

class Parser:

	#CONSTRUCTOR
	def __init__(self,url):
		self.soup = bs(urllib.request.urlopen(url).read(), "lxml")

	def getMetaData(self):
		#print(self.soup.prettify())
		table = self.soup.find('table',{'class':'datatable01'})
		print(table)




# MAIN FUNCTION --------------------------------------------------------------
if __name__ == "__main__":

    webSite = Parser("https://www-fars.nhtsa.dot.gov/Main/index.aspx")
    webSite.getMetaData()