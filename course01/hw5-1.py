# 單位進貨成本
c = int(input())

# 單位零售價格
r = int(input())

# 需求的可能個數
n = int(input())

# 一份報紙的殘值
s = int(input())

# N 份報紙的機率
n_list = []
for _ in range(0, n+1):
    n_list.append(float(input()))


def expect_profit(c, r, n, s, n_list):
    total_profit_dict = {}
    for q in range(0, len(n_list)):
        total_profit = 0
        for i in range(0, q):
            total_profit += (i*r - c*q + (q-i)*s)*n_list[i]
        total_profit += (r*q - c*q)*(1-sum(n_list[:q]))
        total_profit_dict[q] = total_profit

    max_q = max(total_profit_dict, key=total_profit_dict.get)
    return max_q, int(total_profit_dict[max_q])


max_q, max_profit = expect_profit(c, r, n, s, n_list)
print(max_q, max_profit)
