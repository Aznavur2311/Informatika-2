salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цены

money_capital = 0
current_spend = spend

for month in range(months):
    deficit = max(0, current_spend - salary)
    money_capital += deficit
    if month < months - 1:
        current_spend *= (1 + increase)

import math
money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
