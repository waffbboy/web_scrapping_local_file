import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time

def find_infinix():

    html_file = requests.get('https://slot.ng/catalogsearch/result/?q=infinix').text

    soup = BeautifulSoup(html_file, 'lxml')
    # scrapping for all the details for the infinix phones needed to create my data frame
    infinix_search_result = soup.find_all('div', class_="item-product")

    phone_prize = []
    # phone_link = []
    phone_name = []
    phone_img = []

    for i, item in enumerate(infinix_search_result):
        # print('{0} : {1}'.format(i,item))
        # print(len(infinix_search_result))
        infinix_product_info_name = item.find('div', class_="product-info").h3.text.strip()
        # print(infinix_product_info )
        infinix_product_price = item.find('div', class_="price-box price-final_price").find('span',
                                                                                            class_="price-wrapper").span.text
        # print(infinix_product_price)

        infinix_product_link = \
        item.find('div', class_="product-info").find('h3', class_="product-name").find('a', class_="product-item-link")[
            'href']

        # print( infinuix_product_link)

        infinix_product_img = item.find('div', class_="product-thumb").find('span', class_="second-thumb").find('span',
                                                                                                                class_="product-image-container").find(
            'span', class_="product-image-wrapper").find('img', class_="product-image-photo")['src']

        # print(infinix_product_img)

        phone_prize.append(infinix_product_price)

        phone_name.append(infinix_product_info_name)

        phone_img.append(infinix_product_img)



    #creation of my dataframe

    rows = [phone_prize,phone_name,phone_img]


    my_data = pd.DataFrame(list(zip(phone_prize,phone_name,phone_img)), columns = ['Product_Prize','Product_Name','Product_Img'])




    #storing Data Frame to a csv file

    my_data.to_csv('Infinix_phone_type.csv', index= False)


    # view file in current working directory



    print(os.listdir(os.getcwd()))


if __name__=='__main__':
    while True:
        find_infinix()
        time_wait = 10
        print('Waiting {}seconds'.format(time_wait))
        time.sleep(time_wait * 60)