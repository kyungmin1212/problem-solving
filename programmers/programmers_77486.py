def solution(enroll, referral, seller, amount):
    answer = []
    parent = {}
    money = {}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        money[enroll[i]] = 0

    for i in range(len(seller)):
        name = seller[i]
        m = amount[i] * 100
        flag = False
        while parent[name] != "-":
            bonus = int(m * 0.1)
            money[name] += m - bonus
            name = parent[name]
            m = bonus
            if bonus == 0:
                flag = True
                break

        if flag:
            continue
        bonus = int(m * 0.1)
        money[name] += m - bonus

    for i in range(len(enroll)):
        answer.append(money[enroll[i]])

    return answer