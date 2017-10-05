import pickle
import sys
import random

f = open('centurylink.pickle', 'rb')
cl = pickle.load(f)
f.close()
intent = cl.classify(sys.argv[1])
print(intent)
#prob_dist = cl.prob_classify(sys.argv[1])
#print(prob_dist.max())
#print(round(prob_dist.prob(intent), 2))
txt = open(intent.lower()+".txt","r")
response = txt.read().splitlines()
print(random.choice(response))
