# 멜론뮤직 스크래핑
from bs4 import BeautifulSoup
import requests

# bs4 시작코드
'''
스크래핑 하고 싶은 주소를 url에 넣어주세요
'''
url = "https://www.melon.com/chart/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


trs = soup.select('table > tbody > tr')

for tr in trs:
    rank = tr.select_one('.rank').text
    title = tr.select_one('.rank01 > span > a').text
    artist = tr.select_one('.rank02 > a').text
    image = tr.select_one('img')['src']

    print(rank, title, artist, image)