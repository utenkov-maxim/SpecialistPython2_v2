class Card:
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        suits = {Card.DIAMONDS: '\u2666', Card.HEARTS: '\u2665', Card.SPADES: '\u2660', Card.CLUBS: '\u2663'}
        return f"{self.value}{suits[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def __gt__(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def __eq__(self, other_card):
        return self.value == other_card.value and self.suit == other_card.suit

    def __lt__(self, other_card):
        return not self > other_card and not self == other_card


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [Card.HEARTS, Card.DIAMONDS, Card.CLUBS, Card.SPADES]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи
        for s in Deck.suits:
            for v in Deck.values:
                self.cards.append(Card(v, s))

    def __str__(self):
        # TODO-0: копируем из предыдущей задачи
        return f"deck[{len(self.cards)}]" + ', '.join([str(c) for c in self.cards])

    def draw(self, x):
        # TODO-1: Принцип работы данного метода прописан в 00_task_deck.md
        return [self.cards.pop(0) for i in range(x)]

    def shuffle(self):
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md
        #   Подсказка: https://www.w3schools.com/python/ref_random_shuffle.asp
        from random import shuffle
        shuffle(self.cards)

    def shift(self, num_card):
        # TODO-1: реализуем новый метод "сдвиг"
        #  Принцип работы: перемещает num_card с верха колоды под низ\
        for i in range(num_card):
            self.cards.append(self.cards.pop(0))

    def __getitem__(self, item):
        return self.cards[item]


deck = Deck()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())

deck.shuffle()

card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())

# 3. Сравнение карт:
if card1 > card2:
    print(f"{card1} больше {card2}")
if card1 < card2:
    print(f"{card1} меньше {card2}")

# 4. Итерация по колоде:
for card in deck:
    print(card)

# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])


# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
