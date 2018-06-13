def give_change(payment):
    change = {
        '500': 0,
        '100': 0,
        '50': 0,
        '10': 0,
        '5': 0,
        '1': 0
    }
    c = 1000 - payment
    while c > 0:
        if c >= 500:
            c -= 500
            change['500'] += 1
        elif c >= 100:
            c -= 100
            change['100'] += 1
        elif c >= 50:
            c -= 50
            change['50'] += 1
        elif c >= 10:
            c -= 10
            change['10'] += 1
        elif c >= 5:
            c -= 5
            change['5'] += 1
        elif c >= 1:
            c -= 1
            change['1'] += 1
    return change


change = give_change(int(input()))
for _, c in change.items():
    print(c, end=' ')
