"""Обработка заказа интернет-магазина."""


def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def validate_order(items):
    """Проверяет корректность элементов заказа."""
    if not isinstance(items, list) or not items:
        raise ValueError("Заказ должен содержать хотя бы один товар")
    for item in items:
        if not all(key in item for key in ("name", "price", "quantity")):
            raise ValueError("У товара должны быть название, цена и количество")
        if item["price"] < 0 or item["quantity"] <= 0:
            raise ValueError("Цена и количество должны быть корректными")


def process_order(items):
    validate_order(items)
    total = calculate_total(items)
    print(f"Стоимость заказа: {total} руб.")
    return total


if __name__ == "__main__":
    order = [
        {"name": "Клавиатура", "price": 1500, "quantity": 1},
        {"name": "Мышь", "price": 800, "quantity": 2},
    ]
    process_order(order)
