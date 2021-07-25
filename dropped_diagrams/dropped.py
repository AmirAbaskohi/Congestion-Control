import matplotlib.pyplot as plt

def read_and_select(fileAddress):
    file = open(fileAddress)
    flow1 = []
    flow2 = []

    for i in file.readlines():
        if(i[0] == "d"):
            temp = i.split()
            if (int(temp[7]) == 1):
                flow1.append(float(temp[1]))
            if (int(temp[7]) == 2):
                flow2.append(float(temp[1]))

    return flow1, flow2

def calculate_dropped(fileAddress):
    flow1, flow2 = read_and_select(fileAddress)
    dropped_flow1 = []
    dropped_flow2 = []

    sec = 0
    count = 0
    i = 0
    while (i < len(flow1)):
        if(sec == int(flow1[i])):
            count += 1
            i += 1
        else:
            dropped_flow1.append(count)
            count = 0
            sec += 1
    
    sec = 0
    count = 0
    i = 0
    while (i < len(flow2)):
        if(sec == int(flow2[i])):
            count += 1
            i += 1
        else:
            dropped_flow2.append(count)
            count = 0
            sec += 1
    
    while(len(dropped_flow1) < 1000):
        dropped_flow1.append(0)
    while(len(dropped_flow2) < 1000):
        dropped_flow2.append(0)
    
    return dropped_flow1, dropped_flow2

time_steps = [i for i in range(1000)]
reno_flow1, reno_flow2 = calculate_dropped("./reno/info.tr")
cubic_flow1, cubic_flow2 = calculate_dropped("./cubic/info.tr")
yeah_flow1, yeah_flow2 = calculate_dropped("./yeah/info.tr")

plt.plot(time_steps, reno_flow1, label = "reno_flow1")
plt.plot(time_steps, reno_flow2, label = "reno_flow2")
plt.plot(time_steps, cubic_flow1, label = "cubic_flow1")
plt.plot(time_steps, cubic_flow2, label = "cubic_flow2")
plt.plot(time_steps, yeah_flow1, label = "yeah_flow1")
plt.plot(time_steps, yeah_flow2, label = "yeah_flow2")

plt.legend()
plt.show()
