from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 这是我们想要生成词云的文本
text = "Python wordcloud wordcloud Python wordcloud wordcloud Python wordcloud wordcloud Python example example"

# 创建WordCloud对象，并设置参数
wc = WordCloud(background_color="white", max_words=2000)

# 生成词云
wc.generate(text)

# 展示词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")  # 关闭坐标轴
plt.show()
