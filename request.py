print("You will write a short note to the Minister of Defence stating what your army will need for a mission.")

name = input("Enter your name: ")
m_name = input("Name of a movie: ")
m_place = input("Name of a country: ")
enemy = input("Place of origin in plural eg(British, Americans): ")
weapon1 = input("A weapon (plural): ")
food1 = input("Name of food: ")
med = input("Name of medicinal drug: ")
weapon3 = input("Name of weapon (plural): ")
stop_loc = input("Name of place: ")
thing1 = input("A thing (plural): ")
colour = input("A colour: ")
cloth = input("Clothing (eg. trousers): ")
celebrity = input("Name of a celebrity: ")
famous = input("Name of a famous person: ")
quote = input("A quote/saying: ")
thing2 = input("A thing (plural): ")
money1 = input("A number that ends with zero: ")
money2 = input("A number that ends with five: ")
weapon4 = input("Name of weapon (plural): ")
food2 = input("Name of food: ")
weapon2 = input("A weapon(plural): ")

print("Hi, this is General " + name.capitalize() + ", and I'm going to be leading my troops on the Operation " + m_name.capitalize() + " mission to " + m_place.capitalize() + ".")
print("We're going to fight against the " + enemy.capitalize() + " who have wrongfully taken over the land. Therefore, I request your immediate assistance as we don't have the necessary equipment to fight against soldiers who have " + weapon1 + " and " + weapon2 + ".")
print("Also, during the said mission, my troops are going to need food and medicine supplies, which is why I'm going to ask that you include " + food1 + ", " + food2 + " and a pack of " + med + " for our survival.")
print("For the weapons, my soldiers are well trained to use " + weapon3 + " and " + weapon4 + ", which we are also requesting for.")
print("We will stop at " + stop_loc.capitalize() + " along the way to pick up a dozen " + thing1 + " and some " + thing2 + ", so we will need about " + money1 + " dollars and another " + money2 + " dollars for miscelleanous.")
print("A pack of " + colour + " " + cloth + " would also be appreciated for our camouflage missions.")
print("As you probably already know, " + celebrity.capitalize() + " is trapped in that location, so this mission is of utmost importance. Your immediate response will thus be highly appreciated.")
print("As " + famous.capitalize() + " used to say, " + " '" + quote + ".'")