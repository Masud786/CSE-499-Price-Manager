from bs4 import BeautifulSoup
import requests
import time

# output csv file declared here
filename = "star.csv"

f = open(filename, "w", encoding='utf-8')

headers = "Product_Title,Price,Shop,Category_Id\n"

f.write(headers)

def webscrapStartech():
    pages = [1,2,3,4,5]

    # declared the url directory and store it in a variable
    # techland gpu section
    for page in pages:
        source_link = requests.get('https://www.startech.com.bd/component/graphics-card?page={}'.format(page)).text

        soup = BeautifulSoup(source_link, 'lxml')

        # search element from specified url html

        body = soup.find('body')

        # here product-thumb is a css class so that i used it as a variable for better understanding

        productInfo = body.find_all('div', class_='col-xs-12 col-md-4 product-layout grid')

        # using loop for grabing whole page data

        for product in productInfo:

            product_name = product.find('h4', class_='product-name')

            title = product_name.a.text.upper()

            product_price = product.find('div', class_='price space-between')

            tk = product_price.span.text.replace(",","").replace("৳","")

            # int(tk)

            data = title + "," + tk + "," + "STARTECH" + "," + "1" + "\n"

            f.write(data)
        time.sleep(5)

webscrapStartech()
