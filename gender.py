import nltk
from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
#print(labeled_names)
import random
def gender_features(word):
    return {'last_letter': word[-1]}
random.shuffle(labeled_names)
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[10:], featuresets[:10]
#print(featuresets[:5])
#print(test_set)
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(classifier.classify(gender_features('Jospin')))
