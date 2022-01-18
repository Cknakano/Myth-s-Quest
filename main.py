game_over = False
state = 0#sets initial state to 0 and when someone dies the states goes to -1 meaning the game will restart

def introduction():#this function starts the game introduction
  print("")
  print("Myth's Quest")
  print("Find the way to return to your universe")
  print("")
  boy_girl()

def boy_girl():
  print("Do you want to be a boy or girl?")
  print("(Type b for boy and g for girl)")
  answer = input("")
  if answer == "b":
    boy()
  elif answer == "g": # == used as an operator for equal
    girl()
  else:
    error()
    boy_girl() #if error, this loops back to give another chance
  print("")

def boy():
  name = input('What is your name?\n')
  print('Hi, %s.' % name)#this allows for an open option on what the player wants their name to be
  advent_start()
def girl():
  name = input('What is your name?\n')
  print('Hi, %s.' % name)#this takes the name the player put in and uses it to say hi
  advent_start()

def error():
  print("Invalid input, try again")
  print("........................")#this is repeatedly used so this code is used to loop back to this message and back to the original define statement in the code

def advent_start():
  print("")
  print("You wake up in an unknown world with no memory of where or why you are there.\r\nBut you are a calm and collected person so you don't panic and debate on what you should do.")
  town_belongings()

def town_belongings():
  print("")
  print("Do you want to look for a town or check your belongings?")
  print("(Type town or belongings)")
  answer = input("")
  if answer == "town":#if statements to make choices and answers for the player to choose
    town()
  elif answer == "belongings":#this elif statement allows for an “else if” statement if the first “if” answer is not the one given
    belongings()
  else:#this one allows for if both options are not given, something “else” will happen- in this case an error statement that I defined
    error()
    print("")
    town_belongings()

def meet_mercenaries():
  print("")#this allows a space between the different def statements, so that it does not look like one big paragraph
  print("After walking for awhile, you find a town and you start to ask people for some information on where you are.\r\nPeople look at you strangely, but one man tells you that you possess energy not from this world.\r\nYou continue walking around and after awhile you walk into a shop. In the shop you find a group of mercenaries.")
  print ("")
  print("Do you want to talk to the group of mercenaries or the store owner?")
  print("(Type mercenaries or store owner)")
  answer = input("")
  if answer == "mercenaries":#this is what the player would input and this decides the route they will take in the game
    mercenaries()#this outputs the next function based on the input- this leads to another def statement with the next steps
    print("")
  elif answer == "store owner":
    store_owner()
    print("")
  else:
    error()
    meet_mercenaries()

def town():
  print("")
  meet_mercenaries()

def belongings():
  print("")
  print("You find a device in your pocket, but it requires a password.")
  print("")
  print("Do you want to try and unlock it?")
  print("(Type yes or no)")
  answer = input("")#equal sign is used to set variables while == is used as an operator to make the variable equal something
  if answer == "yes":
    unlock_1()
  elif answer == "no":
    unlock_2()
  else:
    error()
    belongings()

def unlock_1():
  print("")
  print("You don't remember anything about where, why, or who you are. Did you expect to remember your password?")
  print("")
  print("You decide to just go look for people.")
  meet_mercenaries()

def unlock_2():
  print("")
  print("You decide to just go look for people.")
  meet_mercenaries()

def mercenaries():
  print("")
  print("You ask the mercenaries to tell you where you are and they tell you to follow them if you want to find out.")
  print("Do you follow them?")
  print("(Type yes or no)")
  answer = input("")
  if answer == "yes":
    yes_1()
  elif answer == "no":
    no_1()
  else:
    error()
    mercenaries()

def store_owner():
  print("")
  print("The store owner tells you that you don't belong in this world and that your energy will destory this world.\r\nYou must leave this world before 3 months pass or this world and you will be gone.\r\nYou find out that the mercenaries can help you find your way back to your world, but there is a condition....They want you to help them overthrow the current king and take over.\r\nWhat is your decision?")#\r\n allows the text to begin and move to the next line
  print("(Type accept for now or decline)")
  answer = input("")
  if answer == "accept for now":
    accept_1()
  elif answer == "decline":
    decline_1()
  else:
    error()
    store_owner()

def yes_1():
  print("")
  print("You go to their lair and they tell you that you don't belong in this world and that your energy will destory this world.\r\nYou must leave this world before 3 months pass or this world and you will be gone.\r\nThey can help you find your way back to your world, but there is a condition....They want you to help them overthrow the current king and take over.\r\nWhat is your decision?")
  print("(Type accept for now or decline)")
  answer = input("")
  if answer == "accept for now":
    accept_1()
  elif answer == "decline":
    decline_1()
  else:
    error()
    yes_1()

def no_1():
  print("")
  print("You leave the shop to look for a different group of people to ask\r\nYou run into a group called the Faithful Friends.\r\nThey inform you that you don't belong in this world and the energy you possess will destroy this world.\r\nYou must leave this world before 3 months pass or this world (including you) will be destroyed.\r\nThey inform you that there is a way to open the portal back to your world, which is to find 3 artifacts.\r\nThe Faithful Friends want to help you find the artifacts out of goodwill, but they also want you to help them capture the Young Threats.\r\nThe Young Threats are the group of mercenaries you met in the shop and you find out that their goal is to overthrow the King.\r\nIf you work with the mercenaries, you can get back to your world faster, but there is a risk.")
  print("")
  print("Do you choose to work with the Faithful Friends or the Young Threats?")
  print("(Type faithful friends or young threats)")
  answer = input("")
  if answer == "faithful friends":
    faithful_friends()
  elif answer == "young threats":
    young_threats()
  else:
    error()
    no_1()

def flashback():#this code is repeatedly used for flashback scenes so instead of rewriting this everytime, we defined this as a function so that we only have to type in this function
  print("")
  print("You have a flashback to when you first got your phone, and you remember that your password is your dog's name.\r\nWhat is your password?")
  print("(Type paws or cleo)")
  answer = input("")
  if answer == "paws":
    print("")
    print("You successfully unlocked your device!\r\nThe device contains a map to the different areas that could possibly contain the right artifact.")
  elif answer == "cleo":
    error_1()
    flashback()
  else:
    error()
    flashback()

def error_1():#this code is repeatedly used for password scenes so instead of rewriting this everytime, we defined this as a function so that we only have to type in this function
  print("Fail, try again")

def accept_1():
  print("")
  print("They inform you that there is a way to open the portal back to your world, which is to find 3 artifacts.")
  flashback()
  print("")
  print("The Young Threats have all the possible resources to help you find the artifacts faster.\r\nHowever, you have to help them overthrow the King, which could possibly destroy the world in another way.\r\nThe mercenaries are also on the run, if you get caught you will definitely die.\r\nDo you want to risk it or run away when you can?")
  print("(Type risk it or run away)")
  answer = input("")
  if answer == "risk it":
    print("")
    print("You must make the right choices from here on out or you will never return.")
    artifact_start_2()
  elif answer == "run away":
    print("")
    print("You run away when they are not paying attention, but now you have to run for your life because you know their plan to overthrow the king.\r\nYou meet a group called the Faithful Friends and they help you hide from the Young Threats.\r\nThe Faithful Friends want to help you find the artifacts out of goodwill, but they also want you to help them capture the Young Threats.\r\nDo you want to help them?")
    print("(Type yes or no)")
  answer = input("")
  if answer == "yes":
    artifact_start_3()
  elif answer == "no":
    print("")
    print("Seriously? You are going to refuse? How do you plan on finding 3 unknown artifacts before the end of 3 months? Plus you are now a target of the Young Threats.\r\nSorry but no is not an answer.")
    artifact_start_3()
  else:
    error()
    accept_1()

def decline_1():
  print("")
  print("Run for your life, you know their plan to overthrow the king.\r\nYou run into another group of people called the Faithful Friends.\r\nThey help you hide from the Young Threats and are nice enough to answer your questions.\r\nThey inform you that there is a way to open the portal back to your world, which is to find 3 artifacts.\r\nThe Faithful Friends want to help you find the artifacts out of goodwill, but they also want you to help them capture the Young Threats.\r\nDo you want to help them?")
  print("(Type yes or no)")
  answer = input("")
  if answer == "yes":
    flashback()
    artifact_start_3()
  elif answer == "no":
    print ("")
    print("Seriously? You are going to refuse? How do you plan on finding 3 unknown artifacts before the end of 3 months? Plus you are now a target of the Young Threats.\r\nSorry but no is not an answer.")
    flashback()
    artifact_start_3()
  else:
    error()
    decline_1()

def faithful_friends():
  print("")
  print("You check your belongings and find a device that requires a password.")
  flashback()
  artifact_start_1()

def young_threats():
  print("")
  print("You go back to the shop and seek help from them.")
  flashback()
  print("The Young Threats have all the possible resources to help you find the artifacts faster.\r\nHowever, you have to help them overthrow the King, which could possibly destroy the world in another way.\r\nThe mercenaries are also on the run, if you get caught you will definitely die.\r\nDo you want to risk it or run away when you can?")
  print("(Type risk it or run away)")
  answer = input("")
  if answer == "risk it":
    print("")
    print("You must make the right choices from here on out or you will never return.")
    artifact_start_2()
  elif answer == "run away":
    print("")
    print("You run away when they are not paying attention, but now you have to run for your life because you know their plan to overthrow the king.\r\nYou meet a group called the Faithful Friends and they help you hide from the Young Threats.\r\nThe Faithful Friends want to help you find the artifacts out of goodwill, but they also want you to help them capture the Young Threats.")
    print("(Type yes or no)")
  answer = input("")
  if answer == "yes":
    artifact_start_3()
  elif answer == "no":
    print("")
    print("Seriously? You are going to refuse? How do you plan on finding 3 unknown artifacts before the end of 3 months? Plus you are now a target of the Young Threats.\r\nSorry but no is not an answer.")
    artifact_start_3()
  else:
    error()
    young_threats()

def artifact_start_1():#started to number the different statements so that I could keep track of what route this def statement is for
  print("")
  print("Using this device, you set out with your group.")
  print("")
  print("The 3 artifacts that you need to find represent different metal tiers (bronze, silver, gold).\r\nYou must collect them in order, to receive hints about the next artifact(Bronze->Silver->Gold).")
  print("")
  print("The map first indicates that the bronze artifact is located at the tomb of the God of War.")
  print("")
  five_days1()

def artifact_start_2():
  print("")
  print("Using this device, you set out with your group.")
  print("")
  print("The 3 artifacts that you need to find represent different metal tiers (bronze, silver, gold).\r\nYou must collect them in order, to receive hints about the next artifact(Bronze->Silver->Gold).")
  print("")
  print("The map first indicates that the bronze artifact is located at the tomb of the God of War.")
  print("")
  three_days()

def artifact_start_3():
  print("")
  print("Using this device, you set out with your group.")
  print("")
  print("The 3 artifacts that you need to find represent different metal tiers (bronze, silver, gold).\r\nYou must collect them in order, to receive hints about the next artifact(Bronze->Silver->Gold).")
  print("")
  print("The map first indicates that the bronze artifact is located at the tomb of the God of War.")
  print("")
  five_days2()

def five_days1():
  print("")
  print("You have to get there by foot, so it will take you approximately 5 days to reach the tomb.\r\nAfter 2 days, you run out of rations.\r\nDo you want to go hunting for food or starve?")
  print("(Type hunt or starve)")
  answer = input("")
  if answer == "hunt":
    print("")
    print("You successfully caught a deer and cooked it, you now have energy for the rest of your journey.")
    god_war1()
  elif answer == "starve":
    print("")
    print("Really? You want to starve for 3 more days? You are not going to survive..Eat!\r\nYou decided to hunt for food and caught fish, this should be enough for the rest of the journey.")
    god_war1()
  else:
    error()
    five_days1()

def five_days2():
  print("")
  print("You have to get there by foot, so it will take you approximately 5 days to reach the tomb.\r\nAfter 2 days, you run out of rations.\r\nDo you want to go hunting for food or starve?")
  print("(Type hunt or starve)")
  answer = input("")
  if answer == "hunt":
    print("")
    print("You successfully caught a deer and cooked it, you now have energy for the rest of your journey.")
    god_war3()
  elif answer == "starve":
    print("")
    print("Really? You want to starve for 3 more days? You are not going to survive..Eat!\r\nYou decided to hunt for food and caught fish, this should be enough for the rest of the journey.")
    god_war3()
  else:
    error()
    five_days2()
  
def three_days():
  print("")
  print("The mercenaries have horses so it will only take you 3 days to reach the tomb.\r\nHowever, after 2 days you run out of rations.\r\nDo you want to go hunting for food or starve?")
  print("(Type hunt or starve)")
  answer = input("")
  if answer == "hunt":
    print("")
    print ("You successfully caught a deer and cooked it, now you have energy for for awhile.")
    god_war2()
  elif answer == "starve":
    print("")
    print("You're lucky you only have to go one more day without food before reaching the tomb, but you will have to hunt for food when you reach the tomb.")
    god_war2()
  else:
    error()
    three_days()

def wrong_artifact():#this code is repeatedly used for wrong artifact selection scenes, where the player dies so instead of rewriting this everytime, we defined this as a function so that we only have to type in this function
  print("")
  print("You selected the wrong artifact and triggered an explosion, you died.\r\nTry again")
  print("(Type yes or no)")
  answer = input("")#these input and output choices allow the user to start again or go to the ending
  if answer == "yes":
    state == -1
    introduction()#if they put yes, it will loop back to the beginning
  elif answer == "no":
    ending()#if they put no, then it will go straight to the ending

def god_war1():
  print("")
  print("You arrived at the tomb of the God of War.\r\nYou enter the tomb, and you are given a riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact is used by Ares in the event of wars, to defend himself along with his shield.\r\nWhich is the correct artifact?")
  print("(Type spear or sword)")
  answer = input("")
  if answer == "spear":
    print("")
    print("Correct answer, your map now shows you a new location for the 2nd artifact.")
    god_arch1()
  elif answer == "sword":
    wrong_artifact()
  else:
    error()
    god_war1()

def god_war2():
  print("")
  print("You arrived at the tomb of the God of War.\r\nYou enter the tomb, and you are given a riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact is used by Ares in the event of wars, to defend himself along with his shield.\r\nWhich is the correct artifact?")
  print("(Type spear or sword)")
  answer = input("")
  if answer == "spear":
    print("")
    print("Correct answer, your map now shows you a new location for the 2nd artifact.")
    god_arch2()
  elif answer == "sword":
    wrong_artifact()
  else:
    error()
    god_war2()

def god_war3():
  print("")
  print("You arrived at the tomb of the God of War.\r\nYou enter the tomb, and you are given a riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact is used by Ares in the event of wars, to defend himself along with his shield.\r\nWhich is the correct artifact?")
  print("(Type spear or sword)")
  answer = input("")
  if answer == "spear":
    print("")
    print("Correct answer, your map now shows you a new location for the 2nd artifact.")
    god_arch3()
  elif answer == "sword":
    wrong_artifact()
  else:
    error()
    god_war3()

def god_arch1():
  print("")
  print("The map shows the location of the 2nd artifact as the tomb of the God of Archery.\r\nYou now enter the tomb, and you are given another riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact was used to defect Apollo by the monster Python from a far distance.\r\nWhich is the correct artifact?")#this one is for the far left where nothing bad happens and you continue on to the last location
  print("(Type bow and arrow or knives)")
  answer = input("")
  if answer == "bow and arrow":
    print("")
    print("Correct answer, your map now shows you a new location for the 3rd and final artifact.\r\nThe map shows the location of the 3rd artifact as the ocean.")
    print("")
    print("With no trouble along the way, you arrive at the last location, the vast ocean.\r\nThe final artifact will be given to you if you guess the name of this Greek God, and the correct artifact weapon.")
    god_tri1()
  elif answer == "knives":
    wrong_artifact()
  else:
    error()
    god_arch1()
    
def god_arch2():
  print("")
  print("The map shows the location of the 2nd artifact as the tomb of the God of Archery.\r\nHowever, suddenly you hear an alert about officers coming your way.The officers are only a few hours away, but it will take you at least 2 days to reach the next tomb.\r\nDo you want to ambush the officers or continue your journey to the tomb?")
  print("(Type ambush or continue)")
  answer = input("")
  if answer == "ambush":
    print("")
    print("You succeed in annihilating half of the officers, but another half managed to corner you- you were captured and killed.")
    print("Try again?")
    print("(Type yes or no)")
    answer = input("")
    if answer == "yes":
     introduction()
    elif answer == "no":
     ending()
  elif answer == "continue":
    print("")
    print("You managed to get to the tomb and throw off the officers along the way.\r\nYou now enter the tomb, and you are given another riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact was used to defect Apollo by the monster Python from a far distance.\r\nWhich is the correct artifact?")
    print("(Type bow and arrow or knives)")
    answer = input("")
    if answer == "bow and arrow":
      print("")
      print("Correct answer, your map now shows you a new location for the 3rd and final artifact.\r\nThe map shows the location of the 3rd artifact as the ocean.")
      merc_ot()
    elif answer == "knives":
      wrong_artifact()
    else:
      error()
      god_arch2()
  else:
    error()
    god_arch2()

def god_arch3():
  print("")
  print("The map shows the location of the 2nd artifact as the tomb of the God of Archery.\r\nYou now enter the tomb, and you are given another riddle that will help you figure out which of the 2 artifacts before you is the correct one you need.\r\nRiddle: This artifact was used to defect Apollo by the monster Python from a far distance.\r\nWhich is the correct artifact?")#this one is for the one on the far right where the young threats are trying to kill the faithful friends
  print("(Type bow and arrow or knives)")
  answer = input("")
  if answer == "bow and arrow":
    print("")
    print("Correct answer, your map now shows you a new location for the 3rd and final artifact.\r\nThe map shows the location of the 3rd artifact as the ocean.")
    print("")
    print("At this point, the Young Threats have tracked you down and are trying to kill you guys (they have horses).")
    yt_kill()
  elif answer == "knives":
    wrong_artifact()
  else:
    error()
    god_arch3()

def yt_kill():
  print("")
  print("Do you play smart or run")
  print("(Type smart or run)")
  answer = input("")
  if answer == "smart":
    print("")
    print("You have successfully laid out a trap and managed to get them to retreat.\r\nYou arrive at the final location, the vast ocean.\r\nThe final artifact will be given to you if you guess the name of this Greek God, and the correct artifact weapon.")
    god_tri3()
  elif answer == "run":
    print("")
    print("You tried running away, but they were on horses so they managed to catch you. You were put to death.")
    print("Try again?")
    print("(Type yes or no)")
    answer = input("")
    if answer == "yes":
     introduction()
    elif answer == "no":
     ending()
  else:
    error()
    yt_kill()

def god_tri1():
  print("")
  print("Riddle: Who is the Greek God of the Sea and what is his weapon?")
  print("(Type poseidon/lance, poseidon/trident, or zeus/lightning)")
  answer = input("")
  if answer == "poseidon/lance":
    wrong_artifact()
  elif answer == "poseidon/trident":
    print("")
    print("Correct answer, you have successfully opened the portal back to their world.")
    ending()
  elif answer == "zeus/lightning":
    wrong_artifact()
  else:
    error()
    god_tri1()

def merc_ot():
  print("")
  print("Before going to the last location the mercenaries want you to keep your side of the deal and help them overthrow the king.\r\nYou have to help them otherwise you will die.\r\nBefore going to the final location you follow them into the kingdom and plan your attack.\r\nDo you want to kill the king at night or march in now full force?")
  print("(Type night or now)")
  answer = input("")
  if answer == "night":
    print("")
    print("Success, you have killed the king and all of his followers. The Young Threats are now in control.\r\nWith the kingdom's military in your hand, you now venture out to the final location of the artifact.\r\nWith the kingdom in your hands, you no longer need to worry about resources.\r\nYou arrive at the final location, the vast ocean.\r\nThe final artifact will be given to you if you guess the name of this Greek God, and the correct artifact weapon.")
    god_tri2()
  elif answer == "now":
    print("")
    print("You were caught by the officers and executed")
  else:
    error()
    merc_ot()

def god_tri2():
  print("")
  print("Riddle: Who is the Greek God of the Sea and what is his weapon?")
  print("(Type poseidon/lance, poseidon/trident, or zeus/lightning)")
  answer = input("")
  if answer == "poseidon/lance":
    wrong_artifact()
  elif answer == "poseidon/trident":
    print("")
    print("Correct answer, you have successfully opened the portal back to their world. However, the lives of the people are now in the hands of the Young Threats and they are miserable.")
    ending()
  elif answer == "zeus/lightning":
    wrong_artifact()
  else:
    error()
    god_tri2()

def god_tri3():
  print("")
  print("Riddle: Who is the Greek God of the Sea and what is his weapon?")
  print("(Type poseidon/lance, poseidon/trident, or zeus/lightning)")
  answer = input("")
  if answer == "poseidon/lance":
    wrong_artifact()
  elif answer == "poseidon/trident":
    print("")
    print("Correct answer, you have successfully opened the portal back to their world. Success, you return to your world and this world remains in peace.")
    ending()
  elif answer == "zeus/lightning":
    wrong_artifact()
  else:
    error()
    god_tri3()

def ending():
  print("")
  print("Thank you for playing Myth's Quest!")
  

while not game_over:#allows loop for when game over, the game will loop back to the introduction
  if state == -1:
    game_over = True
  elif state == 0:
    introduction()#this makes sure the introduction starts up first before the other functions and statements(loops back to introduction)
#this game has 5 different endings:
#1.Successfully retrieve all artifacts to open the portal back home and both worlds remain in peace
#2.Fail, get caught by officers, dead
#3.Succeed, but the Young Threats also successfully took over the kingdom, which makes life harder for people
#4.Chose the wrong artifact, died by an explosion
#5.Failed to collect all 3 artifacts
