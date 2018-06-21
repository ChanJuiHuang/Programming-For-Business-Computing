# n代表幾面牆壁, m代表油漆幾次
n, m = [int(x) for x in input().split()]

# wall牆壁
wall = [1] * n

# color_wall顏色對應牆壁數量的字典
color_wall = {}

# start_wall起始牆壁, end_wall結束牆壁, color牆壁顏色代碼
painting_data = []
for _ in range(m):
    start_wall, end_wall, color = [int(x) for x in input().split()]
    painting_data.append((start_wall, end_wall, color))

for data in painting_data:
    wall[data[0]-1:data[1]] = [data[2]]*(data[1] - data[0] + 1)

for color in wall:
    if color not in color_wall:
        color_wall[color] = 1
    else:
        color_wall[color] += 1

print(';'.join([str(color_wall[data[2]]) + ' ' + str(data[2]) for data in painting_data]))
