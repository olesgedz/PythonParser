import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
# #https://www.cvedetails.com/
url = 'https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-66/version_id-77221/Apache-Http-Server-2.2.8.html'
request = requests.get(url)
text = request.text.encode('cp1251')
tree = html.fromstring(text)
text = tree.xpath('//tr[@class="srrowns"]')
i = 0
udict = {}
for tag in text:  # look got to make keys
	udict[i] = {'ver': tag.xpath('.//td')[1].xpath('.//a/text()')[0], 'score': tag.xpath('.//td')[7].xpath('.//div/text()')[0]}
	i+=1
i = 0
df = pd.DataFrame(data=udict,  index=['ver', 'score'])
df = (df.T) 
writer = pd.ExcelWriter('dist.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']
worksheet.set_zoom(90)
# Add some cell formats.
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%'})

# Note: It isn't possible to format any cells that already have a format such
# as the index or headers or any cells that contain dates or datetimes.

# Set the column width and format.
worksheet.set_column('B:B', 18, format1)

# Set the format but not the column width.
worksheet.set_column('C:C', None, format2)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
