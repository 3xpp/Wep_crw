from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup
print('HERE IS THE SEARCH BRUH !!! , U ARE LOOKING IN GARTEN & PFLANZEN !!! ')
r3x0r = input()
link = 'https://www.ebay-kleinanzeigen.de/s-garten-pflanzen/dresden/'+r3x0r+'/k0c89l3820'
my_url = link
#print(' Please copy and paste a Valid Ebay-kleineanzeige Link and paste it here ')
#my_url = input()
#open the Url & grabbing the page
uClient = Ureq(my_url)
#make every thing to varibale
page_html = uClient.read()
#close the client
uClient.close()
#html parser
page_soup = soup(page_html,"html.parser")
#Grabb the items from the url & put them in virable
items = page_soup.findAll("article",{"class":"aditem"})
#	for item in items:
#		title = item.div.div["data-imgtitle"]
if 'Es wurden leider keine in page_html':
        print('leder gibt es keine ergebnse')
filename = "ebay.csv"
f = open(filename,"w")
headers = "Title, Price \n"
f.write(headers)
for item in items:
	title_first = item.findAll("div",{"class":"aditem-main"})
	title = title_first[0].a.text

	price_first = item.findAll("div",{"class":"aditem-details"})
	price = price_first[0].strong.text
	
	ort = price_first[0].text[30:64]
	print("title : "+title)
	print("price : "+price )
	#print("ort : "+ort)
	f.write(title + ","+ price.replace(",","|") +"\n")
