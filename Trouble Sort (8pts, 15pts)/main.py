t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    even = arr[0::2]
    odd = arr[1::2]
    even.sort()
    odd.sort()
    i = 0
    j = 0
    k = 0
    while(i<len(even) or j < len(odd)):
        if k%2 == 0:
            arr[k] = even[i]
            i+=1
        else:
            arr[k] = odd[j]
            j+=1
        k+=1
    while i<len(even):
        arr[k] = even[i]
        i+=1
        k+=1
    while(j < len(odd)):
        arr[k] = odd[i]
        i+=1
        k+=1
    ans = 1 
    s = "Case #{}: ".format(_+1)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            s += str(i)
            ans = 0
            break
    if ans:
        s += "OK"
    print(s)
