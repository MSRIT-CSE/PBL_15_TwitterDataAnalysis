import webbrowser;

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
	
tweetFile = "TwitterDataSet/training_set_tweets.txt";
usersFile = "TwitterDataSet/training_set_users.txt";
positivesFile = "TwitterDataSet/Positive.txt";
negativesFile = "TwitterDataSet/Negative.txt";

positives = open(positivesFile).readlines();
negatives = open(negativesFile).readlines();
tweets = open(tweetFile).readlines();
#tweets = tweets[:10];
users = open(usersFile).readlines();
#str1= raw_input("Enter tweet id: ");
for x in range(len(positives)):
    positives[x] = positives[x].replace("\n","");
for x in range(len(negatives)):
    negatives[x] = negatives[x].replace("\n","");
positives = frozenset(positives);
negatives = frozenset(negatives);

pos = 0;
neg = 0;
neu = 0;
counter = 0;
old = 0;
new = 0;

locread= raw_input("enter the location : ");
usr=[]
for user in users:
        user__=user.split("\t");
       # print user__;
        if(user__[1]==locread+"\n"):
                #print user__[1];
                usr.append(user__[0]);     
        
#print usr
for tweet in tweets:
    tweet__=tweet.split("\t");
    #print tweet__;
    for ii in range(len(usr)):
            if tweet__[0]==usr[ii]:
                #print tweet__;
                pos_ = 0;
                neg_ = 0;
                for word in tweet.split():
                    word = word.lower();
                    if word in positives:
                        pos_ += 1;
                    elif word in negatives:
                        neg_ += 1;
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
display(pos,neg,neu);
print pos;
print neg;
print neu;
raw_input();
