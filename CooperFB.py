import fbchat as fbchat
import time


client = fbchat.Client("lukefarrell21@yahoo.com","imakoolkat21")
cooperMembers = ["Jake Shulman"]

def checkMessages():
	boolean = False
	last_messages = client.getThreadInfo(friend.uid,0)
	last_messages.reverse()  # messages come in reversed order
	print last_messages
	if last_messages[0].strip().lower() == "paying":
		boolean = True
		client.send(friend.uid, """
Thank you for complying.

If your payment is not recieved in 1 hour your Facebook will be disabled
""")
	return boolean

for member in cooperMembers:
	friend = client.getUsers(member)[0]
	client.send(friend.uid, """
This is the Cooper Treasurer Chat Bot:
You are recieving this notification because you have not paid dues. 

**If you do not pay Dues in the next 2 minutes your facebook will be disabled**

Reply "Paying" to prevent disabling**
""")

	time.sleep(60)
	if checkMessages == True: 
		print "SAFE"
		break
	client.send(friend.uid,  """
**You have 60 seconds to pay 
or notify the Cooper Treasurer about the status of your payment.**
""")

	time.sleep(30)
	if checkMessages == True: 
		print "SAFE"
		break
	client.send(friend.uid, """
**You have 30 seconds to pay 
or notify the Cooper Treasurer about the status of your payment
	""")


	time.sleep(10)
	if checkMessages == True: 
		print "SAFE"
		break
	client.send(friend.uid, """RIP""")



	for x in range(100):
		try:
			client.send(friend.uid, "Pay Dues")
			print "Successfully Sent"







		except:
			"Message Failed"