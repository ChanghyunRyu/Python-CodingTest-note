def solution(today, terms, privacies):
    answer = []
    check = {}
    for term in terms:
        name, period = term.split()
        check[name] = int(period)

    today = str_to_year(today)
    for i in range(len(privacies)):
        year, term = privacies[i].split()
        year = str_to_year(year)
        plus_month(year, check[term])
        if check_period(today, year):
            answer.append(i+1)
    return answer


def str_to_year(string):
    result = list(map(int, string.split('.')))
    return result


def plus_month(date, m):
    date[1] += m
    y, month = divmod(date[1], 12)
    date[0] += y
    date[1] = month
    if month == 0:
        date[1] = 12
        date[0] -= 1


def check_period(today, year):
    print(year)
    if today[0] > year[0]:
        return True
    elif today[0] == year[0] and today[1] > year[1]:
        return True
    elif today[0] == year[0] and today[1] == year[1] and today[2] >= year[2]:
        return True
    else:
        return False


print(solution("2019.12.09", ["A 12"], ["2018.12.10 A", "2010.10.10 A"]))
print(solution("2020.12.28", ["A 12", "B 1"], ["2019.01.01 A", "2020.11.28 B"]))
