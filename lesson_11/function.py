"""
7. Список містить словники - дані про ціну і тираж кожного з  журналів. Скласти
програму, яка визначає середню вартість журналів, тираж яких  більше 10 000
примірників.

    ```python
    [
      {"name": "Space", "volume": 20000, "price": 12.45},
      {"name": "SeaSide", "volume": 5000, "price": 10.45},
      {"name": "Fortune", "volume": 10000, "price": 17.99},
      {"name": "Vouge", "volume": 25000, "price": 7.68},
    ]
    ```
"""


def get_average_price(journal_list: list, volume: int) -> float:
    """Function returns average price of journals with volume greater than volume"""
    total_price = 0
    count = 0
    for journal in journal_list:
        if journal["volume"] > volume:
            total_price += journal["price"]
            count += 1

    return 0 if not count else total_price / count


journal_list = [
    {"name": "Space", "volume": 20000, "price": 12.45},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Fortune", "volume": 10000, "price": 17.99},
    {"name": "Vouge", "volume": 25000, "price": 7.68},
]
volume = 10000

if __name__ == "__main__":
    print(get_average_price(journal_list, volume))