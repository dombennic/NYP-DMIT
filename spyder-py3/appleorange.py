import json

from sklearn import tree
features = [[140,1], [130,1], [150,0], [170, 0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
answer = clf.predict([[160,0]])

lists = answer.tolist()
json_str = json.dumps(lists)
print(json_str)