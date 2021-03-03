import requests
from bs4 import BeautifulSoup

URL = 'https://www.jobindex.dk/jobsoegning/it/systemudvikling/storkoebenhavn?q=python'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='result_list_box')

job_elems = results.find_all('div', class_='PaidJob-inner')


for job_elem in job_elems:
	title = job_elem.find_all('b')
	beskrivelse = job_elem.find_all('p')
	print(title, beskrivelse, end='\n'*2)
