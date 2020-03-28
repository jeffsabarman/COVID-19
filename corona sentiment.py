from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
import matplotlib.pyplot as plt

analyser = SentimentIntensityAnalyzer()
begin_date = dt.date(2019,12,1)
end_date = dt.date(2020,3,18)

limit = 1000

def detector(x):
    try:
        return detect(x)
    except:
        None

tweets = query_tweets('COVID-19 or corona virus', begindate= begin_date, enddate= end_date, limit = limit)

df = pd.DataFrame(t.__dict__ for t in tweets)
df['lang'] = df['text'].apply(lambda x:detector(x))
df = df[df['lang'] == 'en']

df2 = df['text']

x = []
y = []
pos = 0
neg = 0
neut = 0
all = []
for i in range(0,len(df2)):
    x.append(i)
for num in range (0,len(df2)):
    sentence = df2.iloc[num]
    score = analyser.polarity_scores(sentence)
    com_score = score.get('compound')
    if com_score >= 0.05:
        pos+=1
        all.append(1)
    elif com_score > -0.05 and com_score <0.05:
        neut+=1
        all.append(0)
    elif com_score <= -0.05 :
        neg+=1
        all.append(-1)
    y.append(com_score)


plt.plot(x, all)
plt.xlabel('Sentence')
plt.ylabel('Score Sentiment')
plt.title('COVID-19 Sentiment Analysis')
plt.show()

print("Number of Positive Statement : ", pos)
print("Number of Negative Statement : ", neg)
print("Number of Neutral Statement : ", neut)

if pos>neg:
    print("The overall statement are POSITIVE!")
else:
    print('The overall statement are NEGATIVE...')




