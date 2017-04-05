import random
import os.path

while True:
	prompt = raw_input("Is this an official run? That is, should I mark off the pairs you are about to generate so they are not generated again? Type 'y' for yes or 'n' for no:\n")
	if prompt == 'y':
		official_run = True
		f = open('past_partners.txt','a')
		f.write('\n')
		break
	elif prompt == 'n':
		official_run = False
		break
	else:
		print "Just type 'y' or 'n'!"

f = open('past_partners.txt','r')
past_pairs = list()
for line in f:
	past_pair = set(line.split(','))
	past_pairs.append(past_pair)
f.close()

def checkOff(group):
	f = open('past_partners.txt','a')
	group = group.split(',')
	group = [person.strip() for person in group]
	print group
	for i in range(len(group) - 1):
		f.write(group[i] + ",")
	f.write(group[-1] + "\n")
	f.close()

if os.path.isfile('names.txt') and os.access('names.txt', os.R_OK):
	f = open('names.txt','r')
	names = [line[:-1] for line in f if line[0] != "*"]
	if len(names) < 2:
		ValueError("Here's the thing: there's not enough people in Lunch Lottos")
	while len(names) != 0:
		if len(names) == 3:
			trio = random.sample(names, 3)
			if set(trio) not in past_pairs:
				names.remove(trio[0])
				names.remove(trio[1])
				names.remove(trio[2])
				s = str(trio[0] + ",", trio[1] + ", " + trio[2])
				print s
				if official_run: checkOff(s)
				break
		pair = random.sample(names, 2)
		if set(pair) not in past_pairs:
			names.remove(pair[0])
			names.remove(pair[1])
			s = str(pair[0] + ", " + pair[1])
			print s
			if official_run: checkOff(s)
else:
	Exception("Here's the thing: File doesn't exist. Make a file names.txt and add all the names of people in lunch lottos, formatted one name per line.")