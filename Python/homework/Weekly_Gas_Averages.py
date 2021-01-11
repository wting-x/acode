import matplotlib.pyplot as plt


input_txt = 'D:/1994_Weekly_Gas_Averages.txt'
x = []
y = []

f = open(input_txt)
i = 1

for line in f:
    line = line.strip('\n')
    line = line.split(' ')

    x.append(i)
    y.append(float(line[0]))
    i+=1

f.close

plt.plot(x, y, color='g', marker='s', linestyle='-')
plt.margins(0.02)
plt.xlabel("Weekly")
plt.ylabel("Averages")
plt.title("1994_Weekly_Gas_Averages")

plt.show()
