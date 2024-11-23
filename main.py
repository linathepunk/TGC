from telethon import TelegramClient
import re
import os

API_ID   = ""
API_HASH = ""

async def getCodesAsync(client):
	await client.start()
	me = await client.get_me()
	print("+" + str(me.phone) + "\n")

	for msg in await client.get_messages(777000, limit=5):
		code = re.search(r'\b\d{5}\b', msg.message)

		if not code:
			continue

		if msg.date.hour < 10:
			hour = "0" + str(msg.date.hour)
		else:
			hour = str(msg.date.hour)

		if msg.date.minute < 10:
			minute = "0" + str(msg.date.minute)
		else:
			minute = str(msg.date.minute)

		print(hour + ":" + minute + " " + code.group())

async def deleteAsync(client):
	await client.start()
	await client.log_out()

while True:
	os.system("clear")
	print("Choose an session or option:")

	i = 0
	sessions = []
	for file in os.listdir():
		if file.endswith(".session"):
			i+=1
			print(str(i) + ". " + file)
			sessions.append(file)

	i+=1
	print(str(i) + ". Add session")
	i+=1
	print(str(i) + ". Delete session")
	i+=1
	print(str(i) + ". Exit")

	num = input("> ")

	if num.isnumeric() and int(num) >= 1 and int(num) <= len(sessions):
		os.system("clear")
		client = TelegramClient(sessions[int(num)-1], API_ID, API_HASH)
		client.loop.run_until_complete(getCodesAsync(client))
		client.disconnect()
		input("\nPress enter to back")
	elif num.isnumeric() and int(num) == i-2:
		while True:
			os.system("clear")
			name = input("Enter a name of session(letters only): ")
			if name.isalpha():
				client = TelegramClient(name, API_ID, API_HASH)
				client.start()
				client.disconnect()
				break
			else:
				input("Wrong name. Press enter to restart.")
	elif num.isnumeric() and int(num) == i-1:
		while True:
			os.system("clear")
			print("Choose an session to delete")

			i = 0
			sessions = []
			for file in os.listdir():
				if file.endswith(".session"):
					i+=1
					print(str(i) + ". " + file)
					sessions.append(file)

			i+=1
			print(str(i) + ". Back")

			num = input("> ")

			if num.isnumeric() and int(num) >= 1 and int(num) <= len(sessions):
				os.system("clear")
				answer = input("Are you sure you want delete " + sessions[int(num)-1] + "(y/n): ")

				if answer == "y" or answer == "yes":
					client = TelegramClient(sessions[int(num)-1], API_ID, API_HASH)
					client.loop.run_until_complete(deleteAsync(client))
					client.disconnect()
				else:
					break
			elif num.isnumeric() and int(num) == i:
				break
			else:
				input("Wrong answer. Press enter to restart.")

	elif num.isnumeric() and int(num) == i:
		exit()
	else:
		input("Wrong answer. Press enter to restart.")
