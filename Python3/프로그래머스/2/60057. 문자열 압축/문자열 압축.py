def solution(s):
    if len(s) == 1:
        return 1
    
    answer = 1001
    s += " " * len(s)
    
    for i in range(1, len(s) // 2):
        x = ""
        v = 1
        a = s[:i].strip()
        for j in range(i*2, len(s), i):
            if a == s[j-i:j]:
                v += 1
            else:
                x += str(v if v > 1 else '') + a
                a = s[j-i:j].strip()
                v = 1
        
        x += str(v if v > 1 else "") + a.strip()
        answer = min(answer, len(x))
            
    return answer