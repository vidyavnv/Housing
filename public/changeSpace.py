#import regex
import re
 
#start process_tweet
def processTweet(tweet):
    tweet = re.sub(r'(?<=\d)\s+(?=\d)', ',', tweet)
    return tweet
#end
 
#Read the tweets one by one and process it
fp = open('housingData.txt', 'r')
line = fp.readline()

f = open('house.txt','a') 
while line:
    print line
    processedTweet = processTweet(line)
    f.write(processedTweet+'\n')
    line = fp.readline()
#end loop
fp.close()
