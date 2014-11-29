file = raw_input("\nPlease enter the name of the file that you want censored: ")
text = open(file)
word = raw_input("\nPlease enter the word that you would like to have censored from the test: ")
print "\n"
output = []
for line in text:
	line = line.rstrip()
	words = line.split()
	for x in words:
		if x == word:
			output.append("#" * len(word))
		else:
			output.append(x)
			
y = " ".join(output)
	
print y