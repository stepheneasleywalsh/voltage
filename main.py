import math
import random


def V(t):
    value = 311 * math.sin(100 * math.pi * t)
    noise = random.randint(-1,1)
    return round(value, 0) + noise


f = open("data.csv","w")
f.write("TIME / s, VOLTAGE / V")
f.write("\n")

t = 0
while t <= 0.2:
    t = round(t,3)
    line = str(t)+","+str(V(t))
    print(line)
    f.write(line)
    f.write("\n")
    t += 0.002

f.close()

quit()