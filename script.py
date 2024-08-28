import matplotlib.pyplot as plt
from collections import defaultdict

# Задание 1. Функция для чтения и возвращения списка
def read_sales_data(file_path):
    sales_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            product_name, quantity, price, date = line.strip().split(', ')
            sales_data.append({
                'product_name': product_name,
                'quantity': int(quantity),
                'price': float(price),
                'date': date
            })
    return sales_data

# Задание 2. Функция с суммой продаж по продуктам

def total_sales_per_product(sales_data):
    sales_summary = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        sales_summary[sale['product_name']] += total_sale
    return sales_summary

# Задание 3. Функция с общей суммой продаж по дням

def sales_over_time(sales_data):
    """Возвращает словарь с общей суммой продаж по дням."""
    time_summary = defaultdict(float)
    for sale in sales_data:
        total_sale = sale['quantity'] * sale['price']
        time_summary[sale['date']] += total_sale
    return time_summary

# Путь к файлу, файл находится в одной директории со скриптом
file_path = 'products_info.txt'
sales_data = read_sales_data(file_path)

# Вывод на экран продукта с наибольшей выручкой
product_sales = total_sales_per_product(sales_data)
top_product = max(product_sales, key=product_sales.get)
print(f"Продукт, принесший наибольшую выручку: {top_product} на сумму {product_sales[top_product]:.2f}")

# Вывод на экран дня с наибольшей суммой продаж
time_sales = sales_over_time(sales_data)
top_day = max(time_sales, key=time_sales.get)
print(f"День с наибольшей суммой продаж: {top_day} на сумму {time_sales[top_day]:.2f}")

# Построение графиков
fig, axs = plt.subplots(2, 1, figsize=(10, 14))

# График общей суммы продаж по каждому продукту
axs[0].bar(product_sales.keys(), product_sales.values(), color='blue')
axs[0].set_xlabel('Продукты')
axs[0].set_ylabel('Общая сумма продаж')
axs[0].set_title('Общая сумма продаж по продуктам')
axs[0].tick_params(axis='x', rotation=45)

# График общей суммы продаж по дням
axs[1].bar(time_sales.keys(), time_sales.values(), color='green')
axs[1].set_xlabel('Даты')
axs[1].set_ylabel('Общая сумма продаж')
axs[1].set_title('Общая сумма продаж по дням')
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()