"""
Problem: A participant who didn't finish the race
Description: There are lots of marathoner. Everyone finished the race, except one.
             When there are 'participant' list which contains name of all participants
             and 'completion' list which contains name of people who finished the race,
             implement the Solution method to return a participant who didn't finished the race.
Restrictions:
    1. The number of participants : 1 ~ 100,000
    2. Length of completion is 1 less than length of participant
    3. Participants' names consist of more than 1 and less than 20 alphabetic lowercase letters.
    4. Some of the participants may have the same name.

* 입출력 예시는 프로그래머스에 기재되어있으며 테스트 케이스 또한 프로그래머스 참고
    https://programmers.co.kr/learn/courses/30/lessons/42576
"""


def Solution(participant, completion):
    key = 0
    participant_dict = {} # hash table
    for p in participant:
        participant_dict[hash(p)] = p # key, value
        key += hash(p)
    for c in completion:
        key -= hash(c) # The key which can retrieve athlete who didn't finish the race
    return participant_dict[key]


participant_list = ["leo", "kiki", "eden"]
completion_list = ["eden", "kiki"]
return_value = "leo"

if Solution(participant_list, completion_list) == return_value:
    print("Correct")
else:
    print("Wrong")