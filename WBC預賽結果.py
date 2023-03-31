from firebase import firebase
import requests
from bs4 import BeautifulSoup

r = requests.get('https://eltaott.tv/activity_area_fifth/battle_table/wbc2023/group_score')

c=[]
s=[]
if r.status_code == 200:
    soup = BeautifulSoup(r.text , 'html.parser')
    group = soup.select('span.groupTitle')
    country = soup.find_all('div',{'class' ,'col-auto mr-auto align-middle flags'})
    score = soup.find_all('div', {"class": "col-auto align-middle score"})
#把國家抓下來
    for index,i in enumerate(country):
            if index%20==0:
                print(group[index//20].text+":")
            print(i.text)
            c.append(i.text.strip())
    
#把分數抓下來
    for index,j in enumerate(score):
            if index%20==0:
                print(group[index//20].text+":")
            print(j.text)
            s.append(j.text.strip())
#合併兩個串列
if len(c) == len(s):
    list_combind = list(zip(c,s))
#把串列兩個一組
result = []
for i in range(0, len(list_combind), 2):
    pair = [list_combind[i], list_combind[i+1]] if i+1 < len(list_combind) else [list_combind[i]]
    result.append(pair)
#寫入資料庫
s = {'result':result}
url = 'https://wbc-8c0e7-default-rtdb.firebaseio.com/'

fb = firebase.FirebaseApplication(url,None)

for i in s:
    fb.post("預賽",s)
    print("{} 儲存完畢" .format(s))

