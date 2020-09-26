#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[i+1]


p = ['leo', 'kiki', 'eden']
c = ['eden', 'kiki']	
print("테스트 케이스: ", solution(participant=p, completion=c))