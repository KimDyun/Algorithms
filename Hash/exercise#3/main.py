"""
Problem: Disguise

Description:
    Spies disguise themselves with different clothes every day.
    Clothes a spy has are as follows, and he(she) has to wear denim additionally or sunglasses tomorrow
    if he wear the blue T-shirt and round glasses today.

    * Face : round glasses, sunglasses
    * Tops : blue T-shirt
    * Bottoms : denim
    * Outer : long coat

    When 2D array(list) 'clothes' containing clothes the spy has is given,
    implement 'solution' method to return the number of combinations of different clothes.

Restrictions:
    1. Each row of clothes consists of [name, category].
    2. The number of clothes is more than 1 and less than 30.
    3. There are no clothes with the same name.
    4. All clothing names are 1 to 20 in length, and the name consists of only lowercase or '_'
    5. spies wear at least one.

    * 입출력 예시는 프로그래머스에 기재되어있으며 테스트 케이스 또한 프로그래머스 참고
    * [참고 링크] https://programmers.co.kr/learn/courses/30/lessons/42578
"""
# The number of cases
# Face : Two items
# Top : Only one
# Bottom : Only one
# (2+1) * (1+1) * (1+1) - 1 = 11
def solution(clothes):
    combination_cnt = 1
    hash_map = {}
    for item in clothes:
        category = item[1]
        if category in hash_map:
            hash_map[category] += 1 # The number of items
        else:
            hash_map[category] = 1
    for category in hash_map:
        item_cnt = category.values()
        combination_cnt *= (item_cnt+1)
    combination_cnt -= 1
    return combination_cnt
