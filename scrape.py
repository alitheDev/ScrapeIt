#Python program to scrape website and save quotes from website

#importing libraries
import requests
from bs4 import BeautifulSoup
import csv

#the link of the website we want to scrape
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) #getting the request

#for parsing we use beautifulsoap library
soup = BeautifulSoup(r.content, 'html5lib')


quotes=[] # storing qoutes

#creating table
table = soup.find('div', attrs = {'id':'all_quotes'})

#Making Row
for row in table.findAll('div',
						attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
	quote = {}
	quote['theme'] = row.h5.text
	quote['url'] = row.a['href']
	quote['img'] = row.img['src']
	quote['lines'] = row.img['alt'].split(" #")[0]
	quote['author'] = row.img['alt'].split(" #")[1]
	quotes.append(quote)

#creating CSV file
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['theme','url','img','lines','author'])
	w.writeheader()
	for quote in quotes:
		w.writerow(quote)
