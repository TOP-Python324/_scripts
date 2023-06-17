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


# переменная для аннотаций
Hand = tuple[int, int, int, int, int]


def hand_rand() -> Hand:
    """Генерирует кортеж из пяти случайных номиналов игральных карт."""
    # hand = tuple(rr(2, 15) for _ in range(5))
    hand = ()
    for _ in range(5):
        while True:
            card = rr(2, 15)
            if hand.count(card) < 4:
                break
        hand += (card, )
    return hand


def poker_comb(hand: Hand) -> str:
    """Находит самую старшую покерную комбинацию в переданном кортеже с номиналами игральных карт."""
    unique = set(hand)
    unique_len = len(unique)
    max_repeats = max(hand.count(card) for card in unique)
    
    if unique_len == 4:
        return 'пара'
    
    elif unique_len == 3:
        if max_repeats == 2:
            return 'две пары'
        else:
            return 'сет'
    
    elif unique_len == 5:
        min_card = min(hand)
        if sorted(hand) == list(range(min_card, min_card+5)):
            return 'стрит'
    
    # elif unique_len == 2:
    else:
        if max_repeats == 3:
            return 'фулл-хаус'
        else:
            return 'каре'
    
    return 'старшая карта'



cnt = 0
search = 'стрит'
while True:
    if poker_comb(hand_rand()) == search:
        break
    cnt += 1

print(f'{search}: {cnt}')
