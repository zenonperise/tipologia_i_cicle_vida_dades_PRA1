import csv
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from functools import reduce

df=pd.read_csv('output.csv', index_col=0) 

# Codi wordcloud Title

title_df=df['title']
wordcloud_title= reduce(lambda x,y:x+ " " + y, title_df)
wordcloud = WordCloud(width=1200, height=780, margin=0, min_word_length=5, background_color="white")
wordcloud.generate(wordcloud_title)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Codi wordcloud Summary


summary_df=df['summary']
wordcloud_title= reduce(lambda x,y:x+ " " + y,summary_df)
wordcloud = WordCloud(width=1200, height=780, margin=0, min_word_length=5, background_color="white")
wordcloud.generate(wordcloud_title)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
