print ("Hello and welcome to my first Python Game!")
bullets = 10
time = 60
print ("You are the village hunter and you've been sent on a mission to hunt a buffalo. You have 10 bullets in your gun and one hour to hunt down the buffalo. Manage them well.")
name = input("What's your name? ").capitalize()
age = int(input("How old are you? "))
print ("Hello, " + name + ", you are", age, "years old, right?")
if age >= 18:
  print ("Congrats, you're eligible to play this game.")
  wantstoplay = input("Do you want to play? ").lower()
  if wantstoplay == "yes":
    print ("Great, then let's get started!")
    
    leftright = input("You emerge from your house and follow the path into the forest. Do you go left or right? (left/right) ").lower()
    if leftright == "left":
      ans = input("Nice, you follow the left path and emerge in front of a river. Takes 5 minutes. There's a crocodile waiting in the water. Do you shoot the crocodile or go around the beach to the other side? (shoot/around) ").lower()
      time -= 5
      if ans == "shoot":
        ans = input("You had to shoot the crocodile twice before you could kill it. You swim across the river in 5 minutes. Now you have a crocodile's corpse. Do you take it home and forget the buffaloes, or do you leave it in the water and continue your search for the buffaloes? (take/leave) ").lower()
        bullets -= 2
        time -= 5
        if ans == "leave":
          ans = input("You forget the crocodile and move on. There's a thick line of trees just by the left and an open field of grass further on. Where do you go? (field/trees) ").lower()
          if ans == "field":
            print("That's right, buffaloes graze on grasses.")
          elif ans == "trees":
            print("Are you hunting snakes and monkeys now? Try to follow the open fields next time, Tarzan. You go back out to the open fields. That takes you an extra 12 minutes.")
            time -= 12
            
          ans = input("Out on the open fields, you find vultures circling over something in the grass. Must be dead meat. You wave your hands violently and shout to scare the scavengers away. You draw closer and discover that the vultures were feeding on the dead body of a... buffalo! This one was probably hunted down by a cheetah or lion, and it's odious smell indicates it's been there for at least 2 days. Do you pack the carcass into your hunter's bag and go home, or do you hunt a fresh buffalo? (pack/hunt) ")
          if ans == "hunt":
            print ("Good decision. The meat would be contaminated by now anyway. You simply walk away as the vultures flock downwards again.")
          elif ans == "pack":
            ans = input("You start to pack the almost slimy meat into your bag (ew!), and then suddenly you hear several voices that sound like laughter. You know those sounds. Hyenas! Before you can lift you head, you see them, three fierce looking hyenas eyeing the carcass. Do you run away or kill them. (run/kill) ")
            if ans == "kill":
              print ("You take three clean shots and the hyenas drop dead. Now you have lots more meat. But you've spent 3 bullets and 5 minutes doing that. Time to continue the hunt.")
              time -= 5
              bullets -= 3
            elif ans == "run":
              print ("You back slowly away from the carcass and then run away. Luckily for you, the hyenas are only interested in the dead meat anyway. They go for it while you continue your hunt. But now you've wasted 10 minutes for nothing.")
              time -= 10
            
          ans = input("After searching for 10 minutes, you find antelopes, rabbits, deer, but no buffalo. Then, you remember when someone told you that buffaloes loved buffalo grass more than anything. You've seen that grass somewhere, but choose to overlook it. Do you go back or go ahead? (back/ahead) ")
          if ans == "ahead":
            ans = input("You go ahead and continue searching. 5 minutes later, there's a herd of buffaloes up ahead! Do you spring out to surprise them or do you sneak up on them? (spring/sneak) ")
            time -= 5
            if ans == "sneak":
              ans = input("You sneak up slowly to the herd, and ten minutes later, you are close enough to take a shot. Do you take a shot or crawl closer? (shot/crawl) ").lower()
              if ans == "shot":
                print ("BAAM!! A huge buffalo goes down and the herd flees!")
                bullets -= 1
                
              elif ans == "crawl":
                print ("You crawl closer for 3 minutes, and a male buffalo sniffs the air and then alerts the herd. They stampede aimlessly, and you have to take four shots to avoid them trampling you to death in the grass. One buffalo goes down, and the rest flees!")
                bullets -= 4
                time -= 3
              ans = input("Now you have a buffalo down. You heave it up your shoulders and start your journey home. But just before you can exit the forest,  you sight a dark heap circling in the sky. It's the notorious flock of huge bald eagles. They won't let you pass without trying to rob you of your catch. Do you find another way home or confront the birds? (another/confront) ")
              if ans == "confront":
                print("You approach the eagles, take one shot of the gun, which startles them all away, then you take your journey home. That takes you only 15 minutes.")
                time -= 15
                bullets -= 1
              elif ans == "another":
                print("You simply turn around and take another way home. That takes you 25 minutes.")
                time -= 25
              print ("The end.")
              if time <= 0 or bullets <= 0:
                print("You have run out of time/bullets. GAME OVER. Try again.")
              else:
                print("Congrats. You successfully returned with a buffalo. YOU HAVE WON THE GAME!")
            else:
              print("You run out towards the herd, but the noise startles the herd and they all stampede away before you can get close enough to get a shot away. GAME OVER. Try again.")
            
          else:
            print("You track back for 10 minutes before finding a meadow filled with buffalo grass, and there's a buffalo sprinting away very quickly from you. It disappears from sight before you can go after it. Now you can't find it's herd. GAME OVER. Try again.")
            
          
        else:
          print("You take the crocodile home, but THIS ISN'T THE MEAT YOU WERE SENT TO HUNT. Go back and get a buffalo! GAME OVER.")

        
      else:
        print("The river is so long, it takes you all day to walk across the beach to the other side. The buffaloes won't be waiting by now. GAME OVER. Try again.")

      
    
      
    else:
      print("You followed the path on the right and step on a trap. Now you can't hunt a buffalo. GAME OVER. Try again.")
      
    
    
  else:
    print ("If you don't want to play, what then are you doing here? Leave...")
else:
  print ("Sorry, you're not old enough to play.")