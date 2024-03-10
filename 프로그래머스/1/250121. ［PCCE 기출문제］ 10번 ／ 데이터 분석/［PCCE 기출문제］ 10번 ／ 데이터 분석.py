def solution(data, ext, val_ext, sort_by):
    answer = []
    ind = {"code":0,"date":1,"maximum":2,"remain":3}

    for dt in data:
        if dt[ind[ext]] < val_ext:
            answer.append(dt)
    answer.sort(key = lambda x:x[ind[sort_by]])
    return answer