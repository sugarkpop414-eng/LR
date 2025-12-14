money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
capital = money_capital
while True:
    capital += salary
    if capital < spend:
        break
    capital -= spend
    months = months + 1
    spend *= (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:",months)