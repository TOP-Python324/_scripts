# рука из пяти карт, только номиналы, J=11, Q=12, K=13, A=14
# найти самую старшую комбинацию в руке
    # старшая карта
    # пара
    # две пары
    # сет
    # стрит
    # фулл-хаус
    # каре


from random import randrange as rr

# hand = tuple(rr(2, 15) for _ in range(5))
hand = ()
for _ in range(5):
    while True:
        card = rr(2, 15)
        if hand.count(card) < 4:
            break
    hand += (card, )

combination = 'старшая карта'

unique = set(hand)
unique_len = len(unique)
max_repeats = max(hand.count(card) for card in unique)

if unique_len == 4:
    combination = 'пара'

elif unique_len == 3:
    if max_repeats == 2:
        combination = 'две пары'
    else:
        combination = 'сет'

elif unique_len == 5:
    min_card = min(hand)
    if sorted(hand) == list(range(min_card, min_card+5)):
        combination = 'стрит'

# elif unique_len == 2:
else:
    if max_repeats == 3:
        combination = 'фулл-хаус'
    else:
        combination = 'каре'

print(hand, combination, sep='\n')
