import requests
from bs4 import BeautifulSoup

URL = 'https://www.it-jobbank.dk/job/storkoebenhavn?q=python'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='result_list_box')

job_elems = results.find_all('div', class_='jobsearch-result')

for job_elem in job_elems:
	place = job_elem.find('span', class_='job-location')
	company = job_elem.find('div', class_='job-company')
	title = job_elem.find('h3', class_='job-title')
	description = job_elem.find('div', class_='job-body') 
	if None in (place, company):
		continue
	print('Firma: ', company.text.strip())
	print('Placering: ', place.text.strip())
	print('Titel: ', title.text.strip())
	print('Jobbeskrivelse: ', description.text.strip())
	print()
