# 單位進貨成本
c = int(input())

# 單位零售價格
r = int(input())

# 需求的可能個數
n = int(input())

# 訂貨量
q = int(input())

# N 份報紙的機率
n_list = []
for _ in range(0, n+1):
    n_list.append(float(input()))


def expect_profit(c, r, n, q, n_list):
    total_profit = 0
    for i in range(0, q):
        total_profit += (i*r - c*q)*n_list[i]
    total_profit += (r*q - c*q)*(1-sum(n_list[:q]))
    return int(total_profit)


print(expect_profit(c, r, n, q, n_list))
