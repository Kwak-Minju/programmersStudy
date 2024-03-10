def solution(survey, choices):
    answer = ''
    result = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    typ =['R','T','C','F','J','M','A','N']
    for s, c in zip(survey, choices):
        if c > 4:
            result[s[1]] += c % 4       
        elif c < 4:
            result[s[0]] += 4 - c
    for r in range(0,len(result),2):
        if result[typ[r]] >= result[typ[r+1]]:
            answer += typ[r]
        else:
            answer += typ[r+1]
    return answer