def foo(n,m):
    if n-m<0:
        answer= 0
    else:
        answer = 1+foo((n-m),m)
    return answer
print(foo(13,2))