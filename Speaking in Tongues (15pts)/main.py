dict = {}
a = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
b = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'
for i in range(len(a)):
    dict[a[i]] = b[i]
dict['z'] = 'q'
dict['q'] = 'z'
T = int(input())
for t in range(1,T+1):
    s = input()
    ans = ''
    for i in s:
        ans += dict[i]
    print("Case #{}: {}".format(t,ans))
