"""Обработка заказа интернет-магазина."""


def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


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
