"""
해시(hash)란 데이를 효율적으로 관리하기 위해 사용하는 자료구조이다.
해시는 '키(Key)'와 '값(Value)'의 쌍으로 이루어진 데이터 구조를 의미한다.
여기서 핵심적인 것은 바로 '키(Key)'로 데이터를 검색하는 것이다.
이처럼 키를 통해 데이터를 빠르게 검색할 수 있도록 도와주는 자료구조가 해시 테이블(Hash Table)이다.
key가 바로 hash값이다.

1.특징
1) "key와 value가 쌍으로 이루어진 데이터구조를 갖는다"
이를 이용해 데이터를 빠르게 저장하고 검색할 수 있는데, 해시는 데이터를 저장할 위치(index)를 '해시 함수'를 통해 계산한다.

2) 따라서, 데이터의 저장 및 검색 속도가 매우 빠르다는 장점이 있다. (일반적으로 O(1)의 * 시간 복잡도를 가짐)
*시간 복잡도 :
어떤 알고리즘이 문제를 해결하는데 걸리는 시간을 표현하는 방식이다.
시간 복잡도를 나타낼 때는 보통 빅오(O) 표기법을 사용하는데, 예를 들어, 리스트의 모든 요소를 순회하는 경우 시간 복잡도는 O(n)이다.

3) 그러나 해시 함수가 서로 다른 키에 대해 같은 해시 값을 생성하는 '*해시 충돌(Hash Collision)'을 해결해야하는 문제가 있다.
이를 해결하기 위해 여러가지 방법(*체이닝(Chaining), *오픈 어드레싱(Open Addressing) 등)이 사용됩니다.

*해시충돌 : 서로 다른 두 개의 입력값에 대한 해시 함수의 결과값이 같을 때 발생하는 상황을 말함.
ex. hash_function = lambda x: x % 5
위 hash function의 x값으로 서로다른 input인 2와 7 모두 result는 동일하게 '2'를 return 한다.
따라서 key 2통해 조회하려는 value가 2, 7 모두에 해당하기때문에, hash의 장점인 빠른 조회를 활용할 수 없게 된다.
*체이닝(Chaining) :같은 해시 값을 가지는 데이터를 연결 리스트로 연결하는 방법이다. 이 때문에 하나의 버킷에 여러 개의 키-값 쌍이 저장될 수 있다.
ex. hash_table = {1: [('apple', '사과')], 2: [('banana', '바나나'), ('orange', '오렌지')]}
*오픈 어드레싱(Open Addressing)
모든 데이터가 해시 테이블 자체에 저장되는 방법입니다. 만약 해시 충돌이 발생하면, 다른 버킷에 데이터를 저장한다.
이를 위해 선형 탐사(Linear Probing), 이차 탐사(Quadratic Probing), 이중 해싱(Double Hashing) 등의 방법을 사용할 수 있다.
ex. hash_table = {1: ('apple', '사과'), 2: ('banana', '바나나'), 3: ('orange', '오렌지')}

"""
"""
[programmers]
<문제 설명>
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

<제한 사항>
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
<입출력 예제>
phone_book -> return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
"""
def solution(phone_book):
    temp = sorted(phone_book) #정렬하면, 바로뒤의 값과의 비교만 하면 되는것이 포인트
    for i in range(len(temp)):
        if i ==len(temp)-1:
            return True
        elif len(temp[i])>len(temp[i+1]):
            continue
        elif temp[i] == temp[i+1][:len(temp[i])]:
            return False
    return True


"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.
예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 
다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

<종류 / 이름>
얼굴	/ 동그란 안경, 검정 선글라스
상의	/ 파란색 티셔츠
하의	/ 청바지
겉옷	/ 긴 코트
코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
"""
def solution(clothes):
    """
    1) category_map안에 각 의류종류별로 개수를 구한다.
    2) 의류별로 의류의 개수 + 1(안입은 케이스) = 해당 의류종류의 가지수이다.
    3) 결국, 의류1의 가지수 * 의류2의 가지수 *...*의류n의 가지수에서 하나도 안입은 1가지를 제외하면 해결!
    """
    category_map = {}
    for key, cate in clothes:
        category_map[cate] = category_map.get(cate, 0) + 1
    answer = 1
    for i in category_map:
        answer *= (category_map[i] + 1)
    return answer - 1


"""
[프로그래머스]
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 
노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

<제한사항>
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
입출력 예
genres - plays - return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
"""

def solution(genres, plays):
    answer = []
    from collections import Counter
    gen_cnt = {}
    play_dict = {}
    for cnt, (gen, play) in enumerate(zip(genres, plays)):
        gen_cnt[gen] = gen_cnt.get(gen, 0) + play
        if gen not in play_dict:
            play_dict[gen] = {cnt: play}
        else:
            play_dict[gen][cnt] = play
    gen_cnt = dict(Counter(gen_cnt).most_common())
    for key in gen_cnt.keys():
        temp = dict(Counter(play_dict[key]).most_common())
        temp_list = [i for i in temp.keys()][:2]
        answer.extend(temp_list)
    return answer

