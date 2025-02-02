import requests
from bs4 import BeautifulSoup

# スクレイピングするURL
url = "https://example.com"

# HTML取得
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 例: ページタイトルを取得
title = soup.title.text
print("ページタイトル:", title)