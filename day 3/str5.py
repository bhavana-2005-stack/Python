def occ():
    s="bhavana"
    res=""
    visited=[]
    for ch in s:
        if ch not in visited:
            cnt=s.count(ch)
            res+=ch+str(cnt)
            visited.append(ch)
    print(res)
occ()