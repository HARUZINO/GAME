import random as r
from collections import Counter

def card_init(temp_deck,temp_hand):

    r.shuffle(temp_deck)

    for i in range(5):
        temp_hand.append(temp_deck[i])
        temp_deck.pop(i)

    return temp_deck,temp_hand

def card_show(temp_hand):
    print('==========')
    for i in range(5):
        if temp_hand[i] // 13 == 0 or temp_hand[i] == 0:
            print(i + 1, '번째 Card is : ♣', card_show_2(temp_hand[i]))
        elif temp_hand[i] // 13 == 1:
            print(i + 1, '번째 Card is : ♥', card_show_2(temp_hand[i]))
        elif temp_hand[i] // 13 == 2:
            print(i + 1, '번째 Card is : ◈', card_show_2(temp_hand[i]))
        else:
            print(i + 1, '번째 Card is : ♠', card_show_2(temp_hand[i]))

    return None

def card_show_2(temp_num):

    temp_num %= 13

    if temp_num == 0 or (temp_num % 9 != 0 and temp_num % 10 != 0 and temp_num % 11 != 0 and temp_num % 12 != 0):
        return temp_num + 2
    elif temp_num % 9 == 0:
        return 'J'
    elif temp_num % 10 == 0:
        return 'Q'
    elif temp_num % 11 == 0:
        return 'K'
    return 'A'

def card_show_3(temp_num):

    if temp_num // 13 == 0 or temp_num == 0:
        print('BEST Card is : ♣', card_show_2(temp_num))
    elif temp_num // 13 == 1:
        print('BEST Card is : ♥', card_show_2(temp_num))
    elif temp_num // 13 == 2:
        print('BEST Card is : ◈', card_show_2(temp_num))
    else:
        print('BEST Card is : ♠', card_show_2(temp_num))

    return None

def card_change(temp_deck,temp_hand):

    for i in range(5):
        print(i + 1, '번째 Card - Wanna Change? : ')
        answer = input()

        if answer == 'Y':
            r.shuffle(temp_deck)
            temp_hand[i] = temp_deck[0]
            temp_deck.pop(0)

            card_show(temp_hand)
        else:
            pass

    return temp_deck,temp_hand

def card_confirm(temp_hand):
    temp_hand.sort()
    temp_hand_remainder = sorted(list(map(lambda x: x % 13,temp_hand)))
    temp_hand_remainder_count = Counter(temp_hand_remainder)

    if temp_hand == [8,9,10,11,12] or temp_hand == [21,22,23,24,25] or temp_hand == [34,35,36,37,38] or temp_hand == [47,48,49,50,51]:
        return 'ROYAL STARIGHT FLUSH'

    if temp_hand[1] == temp_hand[0] + 1 and temp_hand[2] == temp_hand[0] + 2 and temp_hand[3] == temp_hand[0] + 3 and temp_hand[4] == temp_hand[0] + 4 \
            and (temp_hand[0] not in range(9,13) and temp_hand[0] not in range(22,26) and temp_hand[0] not in range(35,39) and temp_hand[0] not in range(48,52)):
        return 'STRAIGHT FLUSH'

    if 4 in list(temp_hand_remainder_count.values()):
        # any(temp_num == 4 for temp_num in temp_hand_remainder_count.values())
        return 'FOUR CARD'

    if 3 in list(temp_hand_remainder_count.values()) and 2 in list(temp_hand_remainder_count.values()):
        # any(temp_num == 3 for temp_num in temp_hand_remainder_count.values()) and any(temp_num == 2 for temp_num in temp_hand_remainder_count.values())
        return 'FULL HOUSE'

    if temp_hand_remainder == [8,9,10,11,12]:
        return 'MOUNTAIN'

    if all(temp_num in range(0,13) for temp_num in temp_hand) or all(temp_num in range(13,26) for temp_num in temp_hand) or all(temp_num in range(26,39) for temp_num in temp_hand) or all(temp_num in range(39,52) for temp_num in temp_hand):
        return 'FLUSH'

    if temp_hand_remainder[1] == temp_hand_remainder[0] + 1 and temp_hand_remainder[2] == temp_hand_remainder[0] + 2 and temp_hand_remainder[3] == temp_hand_remainder[0] + 3 and temp_hand_remainder[4] == temp_hand_remainder[0] + 4 \
            and (temp_hand[0] not in range(9,13) and temp_hand[0] not in range(22,26) and temp_hand[0] not in range(35,39) and temp_hand[0] not in range(48,52)):
        return 'STRAIGHT'

    if 3 in list(temp_hand_remainder_count.values()):
        # any(temp_num == 3 for temp_num in temp_hand_remainder_count.values())
        return 'TRIPLE'

    if list(temp_hand_remainder_count.values()).count(2) == 2:
        return 'TWO PAIR'

    if 2 in list(temp_hand_remainder_count.values()):
        # any(temp_num == 2 for temp_num in temp_hand_remainder_count.values()):
        return 'ONE PAIR'

    return 'BEST CARD'

def card_confirm_2(temp_result,temp_hand):

    temp_hand.sort()
    temp_hand_remainder = sorted(list(map(lambda x: x % 13, temp_hand)))
    temp_hand_remainder_count = Counter(temp_hand_remainder)

    print('===', temp_hand)
    print('===',temp_hand_remainder)
    print('===',temp_hand_remainder_count)

    if temp_result == 'ROYAL STARIGHT FLUSH':
        return 1024, temp_hand[4]

    if temp_result == 'STARIGHT FLUSH':
        return 512, temp_hand[4]

    if temp_result == 'FOUR CARD':
        temp_find_key = find_value_for_key(temp_hand_remainder_count, 4)
        temp_find_best_key = find_value_best_of_key(temp_hand,temp_find_key)

        return 256, temp_find_best_key

    if temp_result == 'FULL HOUSE':
        temp_find_key = find_value_for_key(temp_hand_remainder_count, 3)
        temp_find_best_key = find_value_best_of_key(temp_hand,temp_find_key)

        return 128, temp_find_best_key

    if temp_result == 'MOUNTAIN':
        return 64, temp_hand[4]

    if temp_result == 'FLUSH':
        return 32, temp_hand[4]

    if temp_result == 'STRAIGHT':
        return 16, temp_hand[4]

    if temp_result == 'TRIPLE':
        temp_find_key = find_value_for_key(temp_hand_remainder_count, 3)
        temp_find_best_key = find_value_best_of_key(temp_hand,temp_find_key)

        return 8, temp_find_best_key

    if temp_result == 'ONE PAIR':
        temp_find_key = find_value_for_key(temp_hand_remainder_count, 2)
        temp_find_best_key = find_value_best_of_key(temp_hand,temp_find_key)

        return 2, temp_find_best_key

    return 1, temp_hand[4]

def find_value_for_key(temp_dict, temp_value):
    for i in temp_dict.keys():
        if temp_dict[i] == temp_value:
            return i
    return None

def find_value_best_of_key(temp_hand, temp_value):
    
    # 현재 여기에서 에러 발생

    temp_max = 0

    for i in temp_hand:
        if i == 0 and temp_value == 0:
            pass

        if i % temp_value == 0 and i > temp_max:
            temp_max = i

    return temp_max








deck = list(range(52))
hand = []

# 1. 덱을 섞고 패를 나눠준다 / 덱에서 카드는 제거

card_init(deck,hand)

# 2. 패를 정리한다

hand.sort()

# 3. 체인지 할 카드를 선정

# card_show(hand)
# deck, hand = card_change(deck,hand)

# 4. 카드 분석

print('\n')


hand = [6, 16, 29, 31, 51]
card_show(hand)

mid_result = card_confirm(hand)
print(mid_result)

# 5. 숫자 / 문양 분석

score, final_result = card_confirm_2(mid_result, hand)
print('score : ', score)
card_show_3(final_result)

# 하단 코드는 테스팅 코드
#
# test_data = [0,0,0,0,0,0,0,0,0,0,0,0]
#
# for i in range(1000000):
#     deck = list(range(52))
#     hand = []
#
#     # 1. 덱을 섞고 패를 나눠준다 / 덱에서 카드는 제거
#
#     card_init(deck, hand)
#
#     # 2. 패를 정리한다
#
#     hand.sort()
#
#     # 테스트중
#
#     result = card_confirm(hand)
#
#     if result == 'BEST CARD':
#         test_data[0] += 1
#     elif result == 'ONE PAIR':
#         test_data[1] += 1
#     elif result == 'TWO PAIR':
#         test_data[2] += 1
#     elif result == 'TRIPLE':
#         test_data[3] += 1
#     elif result == 'STRAIGHT':
#         test_data[4] += 1
#     elif result == 'FLUSH':
#         test_data[5] += 1
#     elif result == 'FULL HOUSE':
#         test_data[6] += 1
#
#
#
#     if result != 'BEST CARD' and result != 'ONE PAIR' and result != 'TWO PAIR' and result != 'TRIPLE' and result != 'STRAIGHT' and result != 'FLUSH' and result != 'FULL HOUSE':
#         # print(i,'번째')
#         # card_show(hand)
#         # print(result)
#             pass
#
#     if result == 'MOUNTAIN':
#         print(i, '번째')
#         card_show(hand)
#         print(result)
#
# print(test_data)

# 하단 코드는 더미 코드

# chance = 5
#
# for i in range(chance):
#     choice = r.randrange(0,52)
#
#     if deck[choice] not in hand:
#         hand.append(deck[choice])
#     else: