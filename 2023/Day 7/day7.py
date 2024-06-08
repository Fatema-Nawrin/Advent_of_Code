from collections import Counter

data = []
with open('./input', 'r') as in_data:
    for line in in_data:
        cards, bid = line.split()
        data.append({"cards": cards, "bid": int(bid)})


card_ranks_1 = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
card_ranks_2 = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]


def determine_rank(cards_values):
    match cards_values:
        case [5]:
            rank = 6
        case [4, 1]:
            rank = 5
        case [3, 2]:
            rank = 4
        case [3, 1, 1]:
            rank = 3
        case [2, 2, 1]:
            rank = 2
        case [2, 1, 1, 1]:
            rank = 1
        case [1, 1, 1, 1, 1]:
            rank = 0
    return rank

def total(data):
    result=0
    for i, hand in enumerate(data):
        result += hand["bid"]*(i+1)
    return result

def process_hands(data, card_ranks):
    for hand in data:
        cards_count = Counter(hand["cards"])
        cards_values = list(cards_count.values())
        cards_values.sort(reverse=True)
        hand["type_rank"] = determine_rank(cards_values)
    data.sort(key=lambda hand: (hand['type_rank'], *[card_ranks.index(c) for c in hand["cards"]]))
    return total(data)

part_1 = process_hands(data, card_ranks_1)
print(part_1)

def process_hands_with_jokers(data, card_ranks):
    for hand in data:
        card_count = {}
        jokers = 0
        for card in hand["cards"]:
            if card == "J":
                jokers += 1
            else:
                card_count[card] = card_count.get(card, 0) + 1
        sorted_cards = sorted(card_count.items(), key=lambda x: (-x[1], card_ranks.index(x[0])))
        cards_values = [count for _, count in sorted_cards]
        cards_values.sort(reverse=True)
        if not cards_values:
            cards_values = [jokers]
        else:   
            cards_values[0] += jokers 
        hand["type_rank"] = determine_rank(cards_values)
    data.sort(key=lambda hand: (hand['type_rank'], *[card_ranks.index(c) for c in hand["cards"]]))
    return total(data)

part_2 = process_hands_with_jokers(data, card_ranks_2)
print(part_2)