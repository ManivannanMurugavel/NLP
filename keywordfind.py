import RAKE
import sys
rake_object = RAKE.Rake("keyword.txt")
text = sys.argv[1]
keywords = rake_object.run(text)
print "keywords: ", keywords
