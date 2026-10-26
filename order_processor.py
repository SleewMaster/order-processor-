"""Обработка заказа интернет-магазина."""


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def process_order(items):
    total = calculate_total(items)
    print(f"Стоимость заказа: {total} руб.")
    return total


if __name__ == "__main__":
    order = [
        {"name": "Клавиатура", "price": 1500, "quantity": 1},
        {"name": "Мышь", "price": 800, "quantity": 2},
    ]
    process_order(order)
