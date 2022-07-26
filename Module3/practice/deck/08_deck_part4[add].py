class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        suits = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f"{self.value}{suits[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def more(self, other_card):
        if Deck.values.index(self.value) == Deck.values.index(other_card.value):
            return Deck.suits.index(self.suit) < Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.value) > Deck.values.index(other_card.value)

    def equal(self, other_card):
        return self.value == other_card.value and self.suit == other_card.suit

    def less(self, other_card):
        return not self.more(other_card) and not self.equal(other_card)


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        # TODO-0: конструктор копируем из предыдущей задачи
        for s in Deck.suits:
            for v in Deck.values:
                self.cards.append(Card(v, s))

    def show(self):
        # TODO-0: копируем из предыдущей задачи
        return f"deck[{len(self.cards)}]" + ', '.join([c.to_str() for c in self.cards])

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


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
