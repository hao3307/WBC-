from firebase import firebase
import requests
from bs4 import BeautifulSoup

r = requests.get('https://eltaott.tv/activity_area_fifth/battle_table/wbc2023/knockout')

c=[]
s=[]
if r.status_code == 200:
    soup = BeautifulSoup(r.text , 'html.parser')
    country = soup.find_all('div',{'class' ,'col-auto mr-auto align-middle flags'})
    score = soup.find_all('div', {"class": "col-auto align-middle score"})
    
    # for index,i in enumerate(country):
    #         if index%20==0:
    #             print(group[index//20].text+":")
    #         print(i.text)
    #         c.append(i.text.strip())
    

    # for i in country:
    #     print(i.text.strip())
    for index,i in enumerate(country):
            if index%2==0:
                print()
            print(i.text.strip())
            c.append(i.text.strip())
    for index,j in enumerate(score):
            if index%2==0:
                print()
            print(j.text.strip())
            s.append(j.text.strip())
    if len(c) == len(s):
        list_combind = list(zip(c,s))
    result = []
    for i in range(0, len(list_combind), 2):
        pair = [list_combind[i], list_combind[i+1]] if i+1 < len(list_combind) else [list_combind[i]]
        result.append(pair)
a = result[0]
s = {'result':a}
url = 'https://wbc-8c0e7-default-rtdb.firebaseio.com/'

fb = firebase.FirebaseApplication(url,None)

for i in s:
    fb.post("冠軍賽",s)
    print("{} 儲存完畢" .format(s))
b = result[1:3]
s = {'result':b}
url = 'https://wbc-8c0e7-default-rtdb.firebaseio.com/'

fb = firebase.FirebaseApplication(url,None)

for i in s:
    fb.post("四強賽",s)
    print("{} 儲存完畢" .format(s))
c = result[3:]
s = {'result':c}
url = 'https://wbc-8c0e7-default-rtdb.firebaseio.com/'

fb = firebase.FirebaseApplication(url,None)

for i in s:
    fb.post("八強賽",s)
    print("{} 儲存完畢" .format(s))