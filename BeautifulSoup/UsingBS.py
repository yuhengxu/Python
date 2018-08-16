# copy css Selector寻找爬取元素的位置
# 谁，在哪，第几个，长什么样子
# body > div.main-content >ul > li:nth-child(1) > img


# copy Xpath来查找元素的位置
# 谁，在哪，第几个，长什么样子
# /html/body/div[2]/ul/lu[1]/img
from bs4 import BeautifulSoup

# open a local html
with open('C:/Users/yuheng/Desktop/python/Simple.html', 'rb') as wb_data:
    # Using beautifulSoup to analysis the html as a lxml document
    Soup = BeautifulSoup(wb_data, 'lxml')
    # print(Soup)

    # select the web element as we want
    # Copy selector : body > div:nth-child(1) > img
    # image = Soup.select('body > div:nth-child(1) > img')
    # 与beautifulsoup的格式要求不符，更改如下
    image1 = Soup.select('body > div:nth-of-type(1) > img')
    #selecto all the images
    image2 = Soup.select('body > div > img')
    print(image1, image2, sep = '\n----------------\n')

for title in titles:
    print(title.get_text())

