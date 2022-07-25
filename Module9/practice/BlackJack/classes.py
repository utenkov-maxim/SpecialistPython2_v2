# Возьмите классы Deck и Card с GIST'а занятия. Доработайте классы, если требуется.
class Card:
    # Сюда копируем последнюю версию класса Карты
    ...

    # Добавляем метод, возвращающий кол-во очков для каждой карты
    def points(self):
        return Deck.card_points[self.value]


class Deck:
    # Количество очков, которые дают карты
    card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    # Сюда копируем последнюю версию класса Колоды
    ...