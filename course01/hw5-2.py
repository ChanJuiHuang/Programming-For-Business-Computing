import math

# n個城鎮, p個基地台, d可覆蓋半徑d以內的城鎮
n, p, d = [int(x) for x in input().split()]

# 城鎮座標
cities_coordinate = []

# 城鎮人口
cities_people = []

for _ in range(n):
    city_data = input().split()
    cities_coordinate.append([int(city_data[0]), int(city_data[1])])
    cities_people.append(int(city_data[2]))


# 未被基地台覆蓋的城鎮
uncovered_cities = [i for i in range(n)]

# 被基地台覆蓋的城鎮
covered_cities = []

# 被選擇蓋基地台的城鎮
selected_cities = []

# 被覆蓋的總人數
total_covered_people = 0


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


while p > 0:
    max_covered_people = 0
    final_selected_city = -1
    final_covered_cities = []

    # 找出覆蓋最多人的城市
    for i in range(n):
        t1_selected_city = i
        t1_covered_people = 0
        t1_covered_cities = []
        selected_coordinate = cities_coordinate[i]

        # 計算距離t1_selected_city在d以內的城鎮
        for uncovered_city in uncovered_cities:
            uncovered_coordinate = cities_coordinate[uncovered_city]

            if distance(selected_coordinate, uncovered_coordinate) <= d:
                t1_covered_people += cities_people[uncovered_city]
                t1_covered_cities.append(uncovered_city)

        if t1_covered_people > max_covered_people:
            max_covered_people = t1_covered_people
            final_selected_city = t1_selected_city
            final_covered_cities = t1_covered_cities

    total_covered_people += max_covered_people
    selected_cities.append(final_selected_city)
    covered_cities.extend(final_covered_cities)
    uncovered_cities = [x for x in uncovered_cities if x not in covered_cities]

    p -= 1

for selected_city in selected_cities:
    print(selected_city+1, end=' ')
print(total_covered_people)
