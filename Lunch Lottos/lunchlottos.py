import random
import os.path

if os.path.isfile('names.txt') and os.access('names.txt', os.R_OK):
	f = open('names.txt','r')
	names = [line[:-1] for line in f if line[0] != "*"]
	if len(names) < 2:
		ValueError("Here's the thing: there's not enough people in Lunch Lottos")
	while len(names) != 0:
		if len(names) == 3:
			trio = random.sample(names, 3)
			names.remove(trio[0])
			names.remove(trio[1])
			names.remove(trio[2])
			print trio[0] + ",", trio[1] + ",", trio[2]
			break
		pair = random.sample(names, 2)
		names.remove(pair[0])
		names.remove(pair[1])
		print pair[0] + ",", pair[1]
else:
	Exception("Here's the thing: File doesn't exist. Make a file names.txt and add all the names of people in lunch lottos, formatted one name per line.")