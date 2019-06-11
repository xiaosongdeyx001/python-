from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'http://comment.bilibili.com/72036817.xml'
html = requests.get(url).content
html_data = str(html, 'utf-8')
soup = BeautifulSoup(html_data, 'lxml')
results = soup.find_all('d')

comments = [comment.text for comment in results]
comments_dict = {'comments': comments}

df = pd.DataFrame(comments_dict)
df.to_csv('bilibili.csv', encoding='utf-8')