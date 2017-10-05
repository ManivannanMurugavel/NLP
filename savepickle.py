import pickle
from textblob.classifiers import NaiveBayesClassifier
import sys
with open('centurylink.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

f = open('centurylink.pickle', 'wb')
pickle.dump(cl, f)
f.close()
