import bs4
import requests
KEYWORDS = ['видеролики', 'QA', 'JavaScript' ]
HEADERS = {'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'Sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'cache-control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
           'sec-ch-ua-mobile': '?0'}
base_url = "https://habr.com"
url = "https://habr.com/ru/all/"
response = requests.get(url, headers = HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    title = article.find("h2").find("span").text
    time_ = article.find(class_="tm-article-snippet__datetime-published").find('time').attrs["datetime"]
    href = article.find(class_="tm-article-snippet__hubs-item-link").attrs["href"]
    result = f"{time_},{title} / {base_url + href}"
    previews = article.find_all('p')
    for preview in previews:
        s = preview.text
        for key in KEYWORDS:
            if key in s:
                print(result)

