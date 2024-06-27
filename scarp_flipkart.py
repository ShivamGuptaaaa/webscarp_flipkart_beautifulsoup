import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_ = "DOjaWF gdgoEp")
    # print(soup)

    # Product_name
    names = box.find_all("div",class_="KzDlHZ")
    # print(names)

    for i in names:
        name = i.text
        Product_name.append(name)
        
    # print(Product_name)


    # Prices
    price = box.find_all("div",class_ = "Nx9bqj _4b5DiR")
    # print(prices)

    for i in price:
        name = i.text
        Prices.append(name)
        
    # print(Prices)


    # Description
    desc = box.find_all("ul",class_ = "G4BRas")
    # print(desc)

    for i in desc:
        name = i.text
        Description.append(name)
        
    # print(Description)
        
        
    # Reviews
    review = box.find_all("div",class_ = "XQDdHH")
    # print(review)

    for i in review:
        name = i.text
        Reviews.append(name)
        
    # print(Reviews)
    
print(len(Product_name))
print(len(Prices))
print(len(Description))
print(len(Reviews))

# # Handle varying lengths by padding shorter lists with NaN
# max_length = max(len(Product_name), len(Prices), len(Description), len(Reviews))

# Product_name.extend([np.nan] * (max_length - len(Product_name)))
# Prices.extend([np.nan] * (max_length - len(Prices)))
# Description.extend([np.nan] * (max_length - len(Description)))
# Reviews.extend([np.nan] * (max_length - len(Reviews)))

# df = pd.DataFrame({"Product Name": Product_name, "Prices" : Prices, "Description": Description, "Reviews":Reviews})
# df.to_csv("Flipkart Scrap Data.csv",index="False")
# df.head()


    # print(np)
    # while True :
    # np = soup.find("a",class_ = "_9QVEpD").get("href")
    # complete_next_page_link = "https://www.flipkart.com"+np
    # print(complete_next_page_link)

        # url = complete_next_page_link
        # r = requests.get(url)
        # soup = BeautifulSoup(r.text,"lxml")
