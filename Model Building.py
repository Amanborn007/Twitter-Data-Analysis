import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

data = pd.read_csv('Dataset/twitter_sentiments.txt', sep=",")

tfidf_vectorizer = TfidfVectorizer(lowercase=True, max_features=1000, stop_words=ENGLISH_STOP_WORDS)
train, test = train_test_split(data, test_size=0.2, stratify=data['label'], random_state=21)
tfidf_vectorizer.fit(train.tweet)

train_idf = tfidf_vectorizer.transform(train.tweet)
test_idf  = tfidf_vectorizer.transform(test.tweet)

model_LR = LogisticRegression()
model_LR.fit(train_idf, train.label)


predict_train = model_LR.predict(train_idf)
predict_test = model_LR.predict(test_idf)


pipeline = Pipeline(steps= [('tfidf', TfidfVectorizer(lowercase=True,
                                                      max_features=1000,
                                                      stop_words= ENGLISH_STOP_WORDS)),
                            ('model', LogisticRegression())])



pipeline.fit(train.tweet, train.label)
pipeline.predict(train.tweet)

text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]
pipeline.predict(text)




from joblib import dump
dump(pipeline, filename="text_classification.joblib")


data[data.label == 1]