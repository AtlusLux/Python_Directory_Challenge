import os
Week = 1
directory = "C:/Users/luxte/Desktop/Homework/CyberSecurity-Notes/" + "/Week "+ str(Week) + "/Day 1" "Day 2" "Day 3"

while Week < 25 :
    if not os.path.exists(directory):
        os.makedirs(directory)
    Week += 1 
    directory = "C:/Users/luxte/Desktop/Homework/CyberSecurity-Notes/" + "/Week "+ str(Week) + "CyberSecurity-Notes/Day 1" "CyberSecurity-Notes/Day 2" "CyberSecurity-Notes/Day 3"