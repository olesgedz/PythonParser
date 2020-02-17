import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
# #https://www.cvedetails.com/
# user_id = 12345
# url для второй страницы
url = 'https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-66/version_id-77221/Apache-Http-Server-2.2.8.html'
r = requests.get(url)
r = r.text.encode('cp1251')
tree = html.fromstring(r)
#print(tree.xpath('//div[@id="searchresults"]'))
# res = tree.xpath('//div[@id="searchresults"]')
# for n in res[0]:
# 	print(n)
# div_node = tree.xpath('//div')[0]  # div тег
# div_node.xpath('.//h2')  # все h2 теги, которые являются дочерними div ноде
# soup = BeautifulSoup(r, "lxml")
# soup = soup.find('tr', {'class': 'srrowns'})
#print(soup.find_all('a')[1].text)
# excel = pd.DataFrame(data = soup.text, index=[0])
r = tree.xpath('//tr[@class="srrowns"]')

i = 0
udict = {}
for tag in r: # look got to make keys
	udict[i] = {'ver': tag.xpath('.//td')[1].xpath('.//a/text()')[0], 'score': tag.xpath('.//td')[7].xpath('.//div/text()')[0]}
	i+=1
i = 0
for tag in r:  
	print(udict[i]['ver'] + ' ' + udict[i]['score'])
	i+=1
excel = pd.DataFrame(data=udict, index=['ver'])
excel = (excel.T)
print(excel)
excel.to_excel('dist.xlsx')

