import matplotlib.pyplot as plt

time_steps = []
reno_flow1 = []
reno_flow2 = []
cubic_flow1 = []
cubic_flow2 = []
yeah_flow1 = []
yeah_flow2 = []

f = open("./reno/reno1.tr")
for i in f.readlines():
    temp = i.split()
    time_steps.append(int(temp[0]))
    reno_flow1.append(round(float(temp[1])))

f = open("./reno/reno2.tr")
for i in f.readlines():
    temp = i.split()
    reno_flow2.append(round(float(temp[1])))

f = open("./cubic/cubic1.tr")
for i in f.readlines():
    temp = i.split()
    cubic_flow1.append(round(float(temp[1])))

f = open("./cubic/cubic2.tr")
for i in f.readlines():
    temp = i.split()
    cubic_flow2.append(round(float(temp[1])))

f = open("./yeah/yeah1.tr")
for i in f.readlines():
    temp = i.split()
    yeah_flow1.append(round(float(temp[1])))

f = open("./yeah/yeah2.tr")
for i in f.readlines():
    temp = i.split()
    yeah_flow2.append(round(float(temp[1])))


plt.plot(time_steps, reno_flow1, label = "reno_flow1")
plt.plot(time_steps, reno_flow2, label = "reno_flow2")
plt.plot(time_steps, cubic_flow1, label = "cubic_flow1")
plt.plot(time_steps, cubic_flow2, label = "cubic_flow2")
plt.plot(time_steps, yeah_flow1, label = "yeah_flow1")
plt.plot(time_steps, yeah_flow2, label = "yeah_flow2")

plt.legend()
plt.show()