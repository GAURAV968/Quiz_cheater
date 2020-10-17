from urllib import request
import json
import bs4
import webbrowser
import requests
from googlesearch import search

glink="https://docs.google.com/forms/d/e/1FAIpQLSfeqDpkBmcGq_vTVG9gYyn6g_DYfthu646vB8Y6c2KHy0xSow/viewform?usp=sf_link"
#glinl=input("Enter the google form link")
url='https://google-form-exporter.herokuapp.com/formdress?url='+glink

html = request.urlopen(url).read()
soup = bs4.BeautifulSoup(html,'html.parser')
site_json=json.loads(soup.text)
ques=""
option=""
for d in site_json['fields']:
    if(d.get('typeid')==2):
        ques=d.get('label')
        option=""
        flag=1
        y=d.get('widgets')[0].get('options')
        for op in y:
        	option=option + ' ' +op.get('label')
        query=ques+ " " + option
        for j in search(query, tld="com", lang='en', num=5,start=0, stop=5, pause=2):
            if(flag==1):
                flag=0
                webbrowser.open(j, new=1)
            else:
                webbrowser.open(j, new=2)

        input()
        print()
        print()
