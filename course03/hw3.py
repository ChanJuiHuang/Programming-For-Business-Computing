input_data = input().split(',')
a = int(input_data[0])
b = float(input_data[1])
c1 = int(input_data[2])
c2 = int(input_data[3])
n = int(input_data[4])

p1 = [(a + c1)/2]
p2 = [(a + b*p1[0] + c2)/2]

for i in range(n):
    p1.append((a + b*p2[i] + c1)/2)
    p2.append((a + b*p1[i+1] + c2)/2)

print("%0.2f %0.2f" % (p1[-1], p2[-1]))
