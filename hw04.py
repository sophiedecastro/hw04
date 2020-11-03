import requests
from bs4 import BeautifulSoup

# keyword = 'drill'
# keyword = 'claremont mckenna' # change search term by changing it here
# page_number='1' # start at 1, must write as a string for concatenation
keyword = 'speaker'
results = [] # a list of dictionaries // want results to be a total number includeng previous pages, not restart each time

# create header with user agent to show that actual person not bot trying to access website 
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

# connect to amazon HTML
# change to ebay url to access ebay
# r = requests.get('https://www.amazon.com/s?k=drill'+keyword, headers = headers) 
# r = requests.get('https://www.ebay.com/sch/i.html?_nkw=hammer'+keyword, headers = headers) 

# to download first 10 webpage results
for i in range(1,11): # start at one, go up to 11 because ebay starts counting its pages at 1 not 0

    # string concatenation: 
    # r = requests.get('https://www.ebay.com/sch/i.html?_nkw=hammer'+keyword+'&_pgn'+page_number, headers=headers) 
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn'+str(i), headers=headers) 
    print('r.status_code=', r.status_code)

    # creates soup object to be able to search html to extract individual items
    soup = BeautifulSoup(r.text, 'html.parser')

    # bs4 syntax
    # input css selectors
    # items = soup.select('a') # use this to check that it is downloading and returning a bunch of a tags 
    # items = soup.select('.a-text-normal.a-link-normal') # for amazon, need a new one for ebay

    '''
    # carrot/arrow things show where it will look, cascading
    titles = soup.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
    for title in titles:
        print('item=', title.text)

    # use .text to make it more readable and get rid of span tags from html
    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=', price.text)

    statuses = soup.select('.SECONDARY_INFO')
    for status in statuses:
        print('status=', status.text)
    '''

    # do the same thing above for status and add below

    # combine into one step to associate item with price
    # extract item boxes rather than just titles/prices
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        # print('---') # print a line to separate items
        # make a dictionary
        result = {}
        titles = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for title in titles:
            # print('item=', title.text)
            result['title'] = title.text # using title because that's what we're calling it in the assignment
        prices = box.select('.s-item__price') # extracting price css selector inside of box, if keep at soup.select it will browse the entire website still 
        for price in prices: # not showing up for some reason? 
            # print('price=', price.text)
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
            result['status'] = status.text
            # print('status=', status.text)
            # print('result=',result)
        results.append(result)

    print('len(results)=',len(results))
    
# 3 last steps for HW:
# 1) make this work for top 10 results pages not just the first one
# 2) also get the status: .SECONDARY_INFO 
# 3) output to json file 

# DONE?
# task 3):
import json
j = json.dumps(results)
with open('items.json','w')as f: # makes json file in same folder
    f.write(j)
# print('j=',j)
# returns a list of dictionaries 

# NOT DONE
# task 2): just add another soup select for status using .SECONDARY_INFO 

# DONE?
# task 1): work for ten pages
# change the page number range as seen above