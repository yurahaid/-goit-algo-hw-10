import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('fruit_juice', lowBound=0, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += lemonade+fruit_juice, "Profit"

# Додавання обмежень
model += 2*lemonade + fruit_juice <= 100  # Обмеження для води
model += lemonade <= 50  # Обмеження для цукру
model += lemonade <= 30  # Обмеження для лимонного соку
model += 2*fruit_juice <= 40  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонаду:", lemonade.varValue)
print("Виробляти фруктового соку:", fruit_juice.varValue)
