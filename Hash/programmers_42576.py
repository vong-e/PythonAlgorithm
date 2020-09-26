#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    #participant, completion 배열의 value를 index를 사용해서 비교하기 위해 정렬을 해준다.
    participant.sort()
    completion.sort()

    #completion 배열의 크기만큼 for loop를 돈다.
    for i in range(len(completion)):
        if participant[i] != completion[i]: #participant, completion 배열의 각 인덱스를 비교, 다르다면 바로 완주자 명단에 없는 참가자임.
            return participant[i] #해당 참가자를 리턴, 동명이인이 있을 경우에도 sort이후 인덱스로 비교하기때문에 따로 처리가 필요 없다.

    return participant[i+1] #정렬된 completion 명단이 모두 participant의 명단과 같았으므로 정렬된 participant의 마지막 참가자가 완주를 하지 못했다.


p = ['leo', 'kiki', 'eden']
c = ['eden', 'kiki']	
print("테스트 케이스: ", solution(participant=p, completion=c))