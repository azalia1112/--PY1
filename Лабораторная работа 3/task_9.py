salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need = 0  # количество денег, чтобы прожить 10 месяцев
month = 0
while month < 10:
    remain = salary - spend
    spend *= (1 + increase)
    need -= remain
    month += 1
print(round(need))
