from lxml import html
import requests

page = requests.get('http://polyratings.com/list.phtml')
tree = html.fromstring(page.content)

# This will create a list of buyers
professor_list_one = tree.xpath('//a[@class="blknav"]/text()')
#professor_list_two = tree.xpath('//a[@class="nav2"]/text()')

#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

for x in range(len(professor_list_one)):
    print(professor_list_one[x])

#print('Prices: ', prices)
