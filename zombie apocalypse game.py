import time

def zombiepocket():
	print("there seems to be something it its pocket")
	searchornot= input("what do you do\n 1- search its pocket\n 2- leave it\n")
	while not (((searchornot == "1") or (searchornot == "2") or (searchornot == "search its pocket") or (searchornot == "leave it"))):
		print ("please enter a valid value")		
		searchornot = input("what do you do\n 1- search its pocket\n 2- leave it\n")
		
	if((searchornot == "1") or (searchornot == "search its pocket")):
		print ("congrats you found a cookie. it seems good for consumption, so you keep it")
		zombiepocket.cookie = True
	else:
		print ("ok you do you")
		zombiepocket.cookie = False

def ending():
	print ("you checked your radio (yes you have a radio) for any signal but found none so you slept")
	time.sleep(3)	
	print("you wake up at 6 a.m")
	if (zombiepocket.cookie or cookie):
		print("you ate the cookie you found yesterday. your day feels good right off the bat")
	elif at_shop.snacks:
		print("you ate the snacks you found yesterday. Your day feels good right off the bat")
	else: 
		print("you have nothing to eat. you dont feel that good")
	time.sleep(3)
	print("you check the radio again")
	print ("WHAAAAT theres signal")
	time.sleep(3)
	print ("*from the radio* any survivors should go to the *static* (im not that creative to come up with a name but lets say you know what they meant) hospital. the army will be collecting people from there to get them to safety.")
	time.sleep(8)
	print ("")
	print("you now know what you are going to do today")
	print("")
	print("to be continued...")
	print("IDK if ill be making a sequel or not so dont count on me")			

def at_shop():
	print("you find a shop nearby but theres a truck next to it")
	print ("it doesn't have any fuel but you can spend the night there")
	sleep=input("where do you sleep?\n1-the shop\n2-the truck\n")
	while not(((sleep=="the shop") or (sleep=="1") or  (sleep=="the truck") or (sleep=="2"))):
		print("please enter a valid value")
		sleep = input("where do you sleep?\n1-the shop\n2-the truck\n")
	else:
		if (sleep == "the shop") or (sleep == "1"):
			print ("you broke into the shop. luckily no zombies are in there")
			print("you search the shop and find some snacks. you keep them")
			time.sleep(2)
			at_shop.snacks = True
			print("a while later you find a (WHAAAAAT) YOU FOUND A GUN AND FOUR BULLETS")
			if age>=20: 
				print ("you keep the gun")
				at_shop.gun = True
				at_shop.bullets = 4
			else:
				print ("you left it there as you are too young to use it")
				at_shop.snacks=True
				at_shop.gun = False
		else:
			print("you broke into the truck")
			at_shop.snacks = False
			print("what a lucky dude. you found a shotgun and three shells")
			if age >= 20:
				print ("you keep them")
				at_shop.shotgun =True
				at_shop.shells = 3
			else:
				print ("you left them as you are too young to use it")
				at_shop.shotgun =False
	time.sleep(3)
	ending()

def at_house():
	print("you went to the house")
	time.sleep(1)
	print("you broke in. luckily there were not any zombies in there")
	time.sleep(1)
	print("you found a shotgun and 10 shells")
	if age >= 20:
		print ("you keep them")
		at_house.shotgun =True
		at_house.shells=10
	else:
		print ("you left them as you are too young to use it")
		at_house.shotgun =False
	time.sleep(3)
	ending()

def shop_or_house():
	print ("ok. now, there are two ways now you can either go to the nearest shop or the nearest house")
	shoporhouse = input("where do you go?\n 1-shop\n 2-house\n")
	while not (((shoporhouse == "1") or (shoporhouse == "2") or (shoporhouse == "shop") or (shoporhouse == "house"))):
		print ("please enter a valid value")
		shoporhouse = input("where do you go?\n 1-shop\n 2-house\n")
	if ((shoporhouse == "1") or (shoporhouse == "shop")):
		at_shop()
	else:
		at_house()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print ("initiating zombie apocalypse 2.0.0")
print("loading...")
time.sleep(7)
name = input ("what's your name\n")	
print("ok", name, "great to have you here")
age = int(input("how old are you (in digits)\n"))	
print ("lets see if you will survive this.")
ar= input("it's night. you are scavanging a town for food. THERE'S A MIDDLE-AGED ZOMBIE IS RUNNING AT YOU! WHAT DO YOU DO?\n1-run\n2-attack\n")

while not ((ar == "1") or ( ar == "attack") or (ar == "2") or (ar == "run")):
	print ("please enter a valid value")
	ar = input ("what do you do?\n1-run\n2-attack\n")
	
if (((ar == "2") or (ar == "attack")) and (age >= 20)):
	print("good blow. you knocked them to the ground and found a bat. what a lucky person")
	zombiepocket()
	shop_or_house()
	
elif (((ar == "2") or (ar == "attack")) and (age < 20)):
	print ("you weren't strong enough. now you are on the ground, but there's a bat next to you.")
	arlost = input ("what do you do? \n1- snatch it and beat the zombie\n2-try to escape\n")
	
	while not (((arlost == "1") or (arlost == "2") or (arlost == "try to escape") or (arlost == "snatch it and beat the zombie"))):
		print ("please enter a valid value")
		arlost = input ("what do you do? \n1- snatch it and beat the zombie\n2-try to escape\n")
		
	if ((arlost == "2") or (arlost == "try to escape")):
		print ("you died")
		print ("please restart the program")
	else:
		print("lucky you. it died.")
		zombiepocket()
		shop_or_house()
else:
	print ("you have escaped and reached a shop")
	zombiepocket.cookie = False
	cookie = False
	at_shop()
