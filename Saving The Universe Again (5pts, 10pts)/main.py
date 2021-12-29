def calculateDamage(s):
    fullDamage = 0
    curDamage = 1
    for i in s:
        if i == 'C':
            curDamage *= 2
        elif i == 'S':
            fullDamage += curDamage
    return fullDamage
    

T = int(input())
for t in range(1,T+1):
    d,s  = input().split()
    d = int(d)
    fullDamage = calculateDamage(s)
    ans = 'Case #{}: '.format(t)
    if fullDamage <= d:
        ans += '0'
    else:
        st = []
        st[:0] = s
        
        if st.count('S') > d:
            ans += "IMPOSSIBLE"
        
        else:
            count = 0
            while fullDamage > d:
                #print(s)
                i = s.rfind("CS")
                s = s[:i] + "SC" + s[i+2:]
                #print(s)
                fullDamage = calculateDamage(s)
                count += 1
                #print(fullDamage)
            ans += str(count)
    print(ans)
    
