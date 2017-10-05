from textblob.classifiers import NaiveBayesClassifier
import sys
test = [
     ('what is my order status?', 'Orderstatus'),
     ('what is my latest order status?', 'Orderstatus')
 ]
with open('train.json', 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

print(str(cl))
print(cl.classify(sys.argv[1]))
print(cl.accuracy(test))
indent = cl.classify(sys.argv[1])
file = open(indent.lower()+".txt", "r") 
print(file.read())

prob_dist = cl.prob_classify(sys.argv[1])
print(prob_dist.max())
print(round(prob_dist.prob(indent), 2))
