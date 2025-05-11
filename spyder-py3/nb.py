from sklearn.datasets import fetch_20newsgroups
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

rawData = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
t = []
for i in range(len(rawData.data)):
 t.append([rawData.data[i], rawData.target_names[rawData.target[i]]])

data = pd.DataFrame(t, columns=['body','newsgroup'])

train, test = train_test_split(data, test_size = 0.4, stratify = data['newsgroup'], random_state = 42)

train_body = train['body'].to_list()
test_body = test['body'].to_list()

y_train = train['newsgroup'].to_list()
vectorizer = TfidfVectorizer( stop_words='english')
X_train = vectorizer.fit_transform(train_body)

clf = MultinomialNB()
clf.fit(X_train, y_train)

X_test = vectorizer.transform(test_body)
y_test = test['newsgroup'].to_list()

pred = clf.predict(X_test)

score = metrics.accuracy_score(y_test, pred)
print("Model accuracy: %0.3f" % score)
print()
print()

print("================ Test Example 1 ================")
test_message = "The Stars were the No. 3 seed in the Western Conference after going 1-2-0 in in the round-robin portion of the Stanley Cup Qualifiers. They defeated the No. 6 seed Calgary Flames in six games in the first round, the No. 2 seed Colorado Avalanche in seven games in the second round and the No. 1 seed Vegas Golden Knights in five games in the conference final to reach the Cup Final for the first time since 2000."
test = vectorizer.transform([test_message])
print(test_message, "====>", clf.predict(test))

print("================ Test Example 2 ================")
test_message = "This machine as CPU running at 9 Mhz with 500MB of RAM"
test = vectorizer.transform([test_message])
print(test_message, "====>", clf.predict(test))
