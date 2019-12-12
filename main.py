import requests

#import pdfkit

from bs4 import BeautifulSoup

url = "https://habr.com/ru/"

header = {"User Agent":	"Chrome/78.0.3904.108 Safari/537.36"}

response = requests.get(url, headers=header)

html = response.text

soup = BeautifulSoup(html, 'html.parser')
#pdfkit.from_string(soup, 'ede.pdf')


#post__title-text  - заголовок статьи
#post__text post__text-html js-mediator-article - текст статьи
#voting-wjt__counter voting-wjt__counter_positive  js-score   - колличество лайков
# post-stats__views-count    - количество просмотров
# post__body post__body_crop  - весь текст


#like =

titles = (soup.find_all("a", "post__title_link"))

contents = (soup.find_all("div", "post__body"))

likes = (soup.find_all("span", "post-stats__result-counter"))

count = len(titles)


class List(object):
    """__init__() functions as the class constructor"""

    def __init__(self, title=None, content=None, like=None):
        self.title = title
        self.content = content
        self.like = like

# создать список с названием posts
posts = []
#i = 0;
#while i < count:
    #print(titles[i])
    #print(contents[i])
    #print(likes[i])
    #i += 1

#сортировака по лайкам
#posts.sort(key='likes')
#
#sorted(posts, key=lambda likes: likes.like)
#print(i)


# Вывести в цикле список
#for post in posts:
    #открываем файл
    #записываем в файл

f = open('Habr_pars.txt', 'w')
for a in posts:
    f.write(a.title + '\n')
    f.write(a.contets + '\n')
    f.write(a.like + '\n')

f.close()



#pdfkit.from_string(...)


#<span class="voting-wjt__counter voting-wjt__counter_positive  js-score" title="Общий рейтинг 53: ↑53 и ↓0">+53</span>