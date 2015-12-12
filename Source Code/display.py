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
	
if __name__ == "__main__":
	pos = int(raw_input("Positive: "));
	neg = int(raw_input("Negative: "));
	neu = int(raw_input("Neutral: "));
	display(pos,neg,neu);
	raw_input();
