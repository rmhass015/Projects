from madlibstories import humorStory, sportStory

print("""
      Welcome to

      8b    d8    db    8888b.  88     88 88""Yb 
      88b  d88   dPYb    8I  Yb 88     88 88__dP 
      88YbdP88  dP__Yb   8I  dY 88  .o 88 88""Yb 
      88 YY 88 dP"\"""Yb 8888Y"  88ood8 88 88oodP 

      The game where you write the story!
      """)

madlibType = input("Which MADLIB would you like to choose? Type 'Humor', 'Sports' or 'Avatar': ")

while madlibType.upper() is not "EXIT":
      if madlibType.upper() == "HUMOR":
            food = input("Type a food: ")
            name = input("Type a friends name: ")
            adj1 = input("Type an adjective (emotion): ")
            bird = input("Name a type of bird: ")
            verb1 = input("Enter a verb: ")
            verb2 = input("Enter another verb: ")
            verb3 = input("Enter one last verb: ")
            noun1 = input("Enter a noun (thing): ")

            humorStory = ("It was " + food + " day at school, and " + name + " was super " + adj1 + " for lunch. But when they went outside to eat, a " + bird + " stole their " + food + "! " + name + " chased the " + bird + " all over school. " + name + " " + verb1 + ", " + verb2 + ", and " + verb3 + " through the playground. Then " + name + " tripped on their " + noun1 + " and the " + bird + " escaped! Luckily, " + name + "'s friends were willing to share their " + food + " with them.")

            print(humorStory)

      elif madlibType.upper() == "SPORTS":
            noun1 = input("Type a noun (living creature): ")
            adj1 = input("Type a style or color of hair: ")
            adj2 = input("Type an adjective: ")
            verb1 = input("Type a verb (past tense): ")
            adj3 = input("Type another adjective: ")
            adj4 = input("Type another adjective: ")
            vehicle = input("Type a kind of vehicle: ")
            adj5 = input("Type an adjective: ")
            obj1 = input("Type an object (plural): ")
            obj2 = input("Type another object: ")
            material = input("Type something sharp: ")
            verb2 = input("Type another verb (present tense): ")
            noun2 = input("Type a body part: ")
            verb3 = input("Type a verb ening in 'ed': ")
            building = input("Type a type of building: ")

            sportStory = "For my birthday, my mom surprised me with a trip to go to baseball camp. There was a " + noun1 + " sitting next to me on the bus with " + adj1 + " hair. We became good friends. As the bus drove up the " + adj2 + " road, we looked at each other as we " + verb1 + " past a " + adj3 + " stadium. Could this really be where we're going to play baseball? The opposing team arrived on a " + adj4 + " " + vehicle + ". I couldn't believe my eyes! They were wearing baseball caps with " + adj5 + " " + obj1 + " and uniforms with a " + obj2 + ". Their spikes were made out of " + material + "! I sure hope they aren't as good as they look! The first inning told most of the story. Our team stood in the field and watched the baseballs " + verb2 + " by our " + noun2 + "'s. In the last inning, the bases were loaded and my friend " + verb3 + " one right over the " + building + ". Our team won the game! "

            print(sportStory)

      elif madlibType.upper() == "EXIT":
            print("Thanks for playing!")
            exit()

      else:
            print("Not a real story.")
            print("Please try again.")



