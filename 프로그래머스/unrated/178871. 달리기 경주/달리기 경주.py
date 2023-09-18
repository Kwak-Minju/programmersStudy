def solution(players, callings):
    rank = {player: idx for idx, player in enumerate(players)}
    for i in callings:
        ra = rank[i]
        
        players[ra],players[ra-1] = players[ra-1],players[ra]
        
        rank[players[ra]] = ra
        rank[players[ra-1]] = ra -1
        
    return players