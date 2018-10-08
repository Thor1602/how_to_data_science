import json
import random
import os
for x in range(1,501):
    data = {}
    temp = []
    counter = 0
    while counter != 20:
        rand_num = random.randint(5,45)
        temp.append(str(rand_num))
        counter += 1
    data["temperature" + str(x)] = temp
    data = str(data)
    data = data[1:len(data)-1]
    with open("test_data.json", 'a+') as outfile:
        outfile.write(data.replace("'", "\""))
        outfile.write(",\n")

