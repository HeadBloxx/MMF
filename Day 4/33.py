import random
friends = ["Alice","Hamza","Imran","Aldin"]

#1st opt
print(random.choice(friends))

#2nd opt
random_index = random.randint(0,4)
print(friends[random_index])