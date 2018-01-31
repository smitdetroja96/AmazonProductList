import bs4
import sys
from urllib.request import urlopen as  uReq
from bs4 import BeautifulSoup as soup

global my_url

def fun(url):

    uClient  = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"s-item-container"})


    for container in containers:

        product = container.findAll("h2",{"class":"a-size-medium s-inline s-access-title a-text-normal"})
        if 1<=len(product):
            product_name = product[0].text
            print(product_name+" ")

        company = container.findAll("span",{"class":"a-size-small a-color-secondary"})
        if 2<=len(company):
            company_name = company[1].text
            print(company_name+" ")

        saving = container.findAll("div",{"class":"a-row a-spacing-none"})
        if 4<=len(saving):
            saving_name = saving[3].text
            saving_name = saving_name.replace(u'\xa0',u'')
            saving_name = saving_name.replace(u' ',u'')
            saving_name = saving_name.replace(u'\n',u' ')
            print(saving_name+" ")

        price = container.findAll("span",{"class":"a-price-whole"})
        if 1<=len(price):
            total_price = price[0].text
            print(total_price+"\n")

        f.write(product_name.replace(",","|")+","+company_name.replace(",","|")+","+saving_name.replace(",","")+","+total_price.replace(",","   ")+"\n")

    return


name = input('enter product name ')

filename = 'products.csv'
f = open(filename,'w')

headers = 'productName, companyName, savingAmount, TotalPrice\n'
f.write(headers)
try:
    for y in range(0,10):
        my_url = 'https://www.amazon.in/'+name+'/s?ie=UTF8&amp;page='+str(y)+'&amp;rh=i%3Aaps%2Ck%3Aphone&page='+str(y)+'&keywords='+name+'&ie=UTF8&qid=2'
        fun(my_url)
except:
    exit(1)
