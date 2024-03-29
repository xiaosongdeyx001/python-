from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

df = pd.read_csv('bilibili.csv', header=None)

text = ''
for line in df[1]:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('peiqi.jpg')

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\simhei.ttf',
    max_words=2000,
    max_font_size=80,
    random_state=30,
)
wc.generate_from_text(text)
# 看看词频高的有哪些,把无用信息去除
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
print(sort[:50])
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("佩奇.jpg")
print('生成词云成功!')