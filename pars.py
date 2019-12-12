import requests

#import pdfkit

from bs4 import BeautifulSoup

url = "https://habr.com/ru/"

header = {"User Agent":	"Chrome/78.0.3904.108 Safari/537.36"}

response = requests.get(url, headers=header)

habr_html = response.text
soup = BeautifulSoup(habr_html, 'html.parser')
#pdfkit.from_string(soup, 'ede.pdf')

#post__title-text  - заголовок статьи
#post__text post__text-html js-mediator-article - текст статьи
#voting-wjt__counter voting-wjt__counter_positive  js-score   - колличество лайков
# post-stats__views-count    - количество просмотров
# post__body post__body_crop  - весь текст

titles = (soup.find_all("a", "post__title_link"))
contents = (soup.find_all("div", "post__body"))
likes = (soup.find_all("span", "post-stats__result-counter"))
count = len(titles)
print("titles: ", count)
print("contents: ", len(contents))
print("likes: ", len(likes))

# создание списка
posts = []
i = 0
while i < count:
    posts.append(
        {
         'title': titles[i].text,
         'content': contents[i].text,
         'likes': likes[i].text
        }
    )
    i += 1


f = open('Habr_pars.txt', 'w', encoding='utf8')

txt = str(posts)
print(txt)



f.write(txt)

f.close()
#posts.sort(key='likes')
#


# Вывести в цикле список
#for post in posts:
    #открываем файл
    #записываем в файл
