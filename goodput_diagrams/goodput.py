import matplotlib.pyplot as plt

def read_and_select(fileAddress, destNum1, destNum2):
    file = open(fileAddress)
    flow1 = []
    flow2 = []

    for i in file.readlines():
        if("ack" in i and i[0] == "+"):
            temp = i.split()
            if (int(temp[2]) == destNum1 and int(temp[7]) == 1):
                flow1.append(float(temp[1]))
            if (int(temp[2]) == destNum2 and int(temp[7]) == 2):
                flow2.append(float(temp[1]))

    return flow1, flow2

def calculate_goodput(fileAddress, destNum1, destNum2):
    flow1, flow2 = read_and_select(fileAddress, destNum1, destNum2)
    goodput_flow1 = []
    goodput_flow2 = []

    sec = 0
    count = 0
    i = 0
    while (i < len(flow1)):
        if(sec == int(flow1[i])):
            count += 1
            i += 1
        else:
            goodput_flow1.append(count)
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
            goodput_flow2.append(count)
            count = 0
            sec += 1
    
    while(len(goodput_flow1) < 1000):
        goodput_flow1.append(0)
    while(len(goodput_flow2) < 1000):
        goodput_flow2.append(0)
    
    return goodput_flow1, goodput_flow2

time_steps = [i for i in range(1000)]
reno_flow1, reno_flow2 = calculate_goodput("./reno/info.tr", 4, 5)
cubic_flow1, cubic_flow2 = calculate_goodput("./cubic/info.tr", 4, 5)
yeah_flow1, yeah_flow2 = calculate_goodput("./yeah/info.tr", 4, 5)

plt.plot(time_steps, reno_flow1, label = "reno_flow1")
plt.plot(time_steps, reno_flow2, label = "reno_flow2")
plt.plot(time_steps, cubic_flow1, label = "cubic_flow1")
plt.plot(time_steps, cubic_flow2, label = "cubic_flow2")
plt.plot(time_steps, yeah_flow1, label = "yeah_flow1")
plt.plot(time_steps, yeah_flow2, label = "yeah_flow2")

plt.legend()
plt.show()
