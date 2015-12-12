
import webbrowser;
import math;


new = 2; #open in new tab if possible.

def display(pos,neg,neu):
	template = open("template.html");
	lines = template.readlines();
	result = open("result.html",'w');
	for line in lines:
		if("Positive" in line):
			line = line.replace("11",str(pos));
		elif("Negative" in line):
			line = line.replace("2",str(neg));
		elif("Neutral" in line):
			line = line.replace("2",str(neu));
		result.write(line+"\n");
		#print(line);
	result.close();
	webbrowser.open("result.html",new = new);
	
tweetFile = "TwitterDataSet/test_set_tweets_porter.txt";
usersFile = "TwitterDataSet/test_set_users.txt";
positivesFile = "TwitterDataSet/Positive.txt";
negativesFile = "TwitterDataSet/Negative.txt";

positives = open(positivesFile).readlines();
negatives = open(negativesFile).readlines();
tweets = open(tweetFile).readlines();
#tweets = tweets[:10];
#users = open(usersFile).readlines();
pcount=len(positives);

ncount=len(negatives);
ppos=pcount/(pcount+ncount);
pneg=ncount/(pcount+ncount);
for x in range(len(positives)):
    positives[x] = positives[x].replace("\n","");
for x in range(len(negatives)):
    negatives[x] = negatives[x].replace("\n","");
positives = frozenset(positives);
negatives = frozenset(negatives);
#print positives;
pos = 0;
neg = 0;
neu = 0;
counter = 0;
old = 0;
new = 0;
tweetid={};
for tweet in tweets:
    pos_ = 0;
    neg_ = 0;
    posprob=0;
    negprob=0;
    for word in tweet.split():
        word = word.lower();
        if word in positives:
            pos_ += 1;
        elif word in negatives:
            neg_ += 1;
    if(pos_!=0 and neg_!=0):
            posprob=pos_/(pos_+neg_);
            negprob=neg_/(pos_+neg_);
    if not tweetid.has_key(tweet.split()[0]):
            tweetid[tweet.split()[0]]=[pos_,neg_];
            #if(negprob!=0):
                    #tweetid[tweet.split()[0]]=math.log(posprob/negprob);
    else:
            tweetid[tweet.split()[0]][0]+=pos_;
            tweetid[tweet.split()[0]][1]+=neg_;
            #if(negprob!=0):
                    #tweetid[tweet.split()[0]]+=math.log(posprob/negprob);
    #print tweet.split()[0];
    #print "%d %d ",pos_,neg_;
    if(neg_>pos_):
        #print "-"+tweet;
        neg += 1;
    elif(pos_>neg_):
        #print tweet;
        pos += 1;
    else:
        #print "*"+tweet;
        neu += 1;
    counter += 1;
    new = int((counter*100)/len(tweets));
    if(new != old):
        print str(new)+"%";
        old = new;
#print tweetid;

for x in tweetid.keys():
        tweetid[x].append(math.log(float(tweetid[x][0])/float(tweetid[x][1])));
print tweetid;
display(pos,neg,neu);
print pos;
print neg;
print neu;
raw_input();
