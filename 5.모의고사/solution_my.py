def solution(answers):
    patterns = [[1,2,3,4,5], 
                [2,1,2,3,2,4,2,5],
                [3,3,1,1,2,2,4,4,5,5]]
    
    scores = [0,0,0]
    idxs = [0,0,0]
    max_score_mans = []
    
    for answer in answers:
        for i in range(0,3):
            if patterns[i][idxs[i]] == answer: scores[i] += 1
        
        new_idxs = [idx + 1 for idx in idxs]
        idxs = new_idxs
        for i in range(0,3):
            if idxs[i] == len(patterns[i]): idxs[i] = 0
    
    max_score = max(scores)
    for i in range(0,3):
        if scores[i] == max_score: max_score_mans.append(i+1)
    
    return max_score_mans