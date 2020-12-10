
def findAllSums(n,s):
    total=sum(s)
    if total == n: 
        return [s]
    result=[]
    for i in [1,2,3]:
      if total+i<=n:
          news=list(s)
          news.append(i)
          result.extend(findAllSums(n,news))
    return result

tribonacci_memo={}
def tribonacci(n):
    if n==0: return 1
    if n==1: return 1
    if n==2: return 2
    if not n in tribonacci_memo:
        tribonacci_memo[n]=tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
    return tribonacci_memo[n]

print("i, brute force, tribonacci")
for i in range(20):
    print(i,", ",len(findAllSums(i,[])),", ",tribonacci(i))

