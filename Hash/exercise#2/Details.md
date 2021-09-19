# A phone book

## Description:
 I'd like to check if there is one of the phone numbers in the phone book which is a prefix of another number.
 If the phone numbers are as follows, the rescue team's phone number is prefix of Young-seok's phone number.
 ```
 * rescue team : 119
 * Jun-young : 97 674 223
 * Young-seok : 11 9552 4421
 ```
  When 'phone_book' which is an array(list) containing phone numbers is given as a parameter of the solution method, write the solution method to return false if there is a phone number which is a prefix of another number, or return true if not.

## Restrictions:
1. Length of phone_book array is more than 1 and less than 1,000,000
2. Length of each phone number is more than 1 and less than 20
3. The same phone numbers cannot exist in the phone book

##### * 입출력 예시는 프로그래머스에 기재되어있으며 테스트 케이스 또한 프로그래머스 참고
##### * [참고 링크]: https://programmers.co.kr/learn/courses/30/lessons/42577


## Consideration
처음 코드는 다음과 같다.
```python
def solution(phone_book):
    phone_book.sort()
    for i, p in enumerate(phone_book[1:]):
        if p.startswith(tuple(phone_book[:i+1])):
            return False
    return True
```
 하나의 문자열에 다른 문자열이 포함되어 있는지 확인할 수 있는 startswith 함수를 사용하여 코드를 구현했었다. 우선 시간 복잡도는 sort함수 O(nlogn) + 반복문으로 list to tuple을 탐색하기 때문에 O(n^2)이다. 최대한 빠른 시간 내에 구현하고자 위와 같이 구현했었는데 런타임 초과로 인해 해당 문제의 효율성 테스트케이스 3,4번을 통과하지 못했었다.

 런타임을 줄일 방법을 생각했는데, 오름차순으로 정렬하면 접두사를 찾을 때 이전 인덱스 전체를 탐색하지 않아도 되고 바로 이전 인덱스만 탐색해도 된다는 것을 깨달았다.
 첫 번째 블록(전화번호 예시)을 정렬하면 str형이기 때문에 다음과 같이 정렬된다. 119 -> 1195524421 -> 97674223
 따라서 다음과 같이 코드를 수정할 수 있다.
 ```python
 def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    return True
 ```
  위 코드의 시간 복잡도는 O(nlogn) + O(n)이다. 그러나 이 문제의 의도 자체가 Hash 알고리즘을 사용하는 것이고 나의 목적 자체도 알고리즘 공부이기 때문에 아래와 같이 코드를 수정했다.
 ```python
 def solution(phone_book):
    hash_table = {}

    for phone_number in phone_book:
        hash_table[phone_number] = 1

    for phone_number in phone_book:
        prefix = ""
        for p in phone_number[:-1]:
            prefix += p
            if prefix in hash_table:
                return False
    return True
   ```
 
