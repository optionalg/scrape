import requests, bs4

print(type(bs4))
r = requests.get('http://polyratings.com/list.phtml', "html.parser")
r.raise_for_status()

r_soup = bs4.BeautifulSoup(r.text)

super_list = r_soup.select("center tr > td")
super_list = super_list[4:]
#professor_list = r_soup.select('tr > td > .nav2') + r_soup.select('tr > td > .blknav')


#print(type(professor_list_one))

#for x in range(10):
    #print("sss-----")
    #print(super_list[x].getText())
    #print("-----eee")


professor_list = []
for x in range(int(len(super_list)/4)):

    professor_list.append([super_list[0 + x].getText(), super_list[1 + x].getText(), super_list[2 + x].getText(), super_list[3 + x].getText()])

for x in range(len(professor_list)):
    print(professor_list[x])
