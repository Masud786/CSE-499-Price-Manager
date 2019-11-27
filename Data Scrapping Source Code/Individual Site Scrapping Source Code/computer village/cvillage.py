from bs4 import BeautifulSoup
import requests
import time

#output csv file declared here
filename = "productss.csv"

f = open(filename,"w",encoding='utf-8-sig')

headers = "Product_Title,Price,Shop,Category_Id\n"

f.write(headers)

def webscrapCvillage():

    pages = [1]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.village-bd.com/graphics-card/{}'.format(page)).text

        soup = BeautifulSoup(source_link,'lxml')


        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = soup.find_all('div',class_='info-box')


        # using loop for grabing whole page data

        for product in productInfo:


            product_name = product.find ('div',class_='pro-name')

            title = product_name.a.text.upper()

            product_price = product.find('div',class_='price')

            tk = product_price.text.replace(",","").replace("৳","")
            
            data = title + "," + tk + "," + "COMPUTER VILLAGE" + "," + "1" + "\n"

            f.write(data)

        time.sleep(5)

webscrapCvillage()






