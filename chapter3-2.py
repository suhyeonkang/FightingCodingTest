n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
sum = 0
count = 1

## 원래 내가 작성한 코드
# max = data[n-1]

# if(max != data[n-2]):
#   min = data[n-2]
# else :
#   min = max

# for _ in range(m):
#   if((count % (k+1) != 0)):
#     sum += max
#     count = count + 1
   
#   else :
#     sum += min 
#     count = count + 1
    

# print(sum)

## 반복되는 수의 집합을 활용해서 다시 풀어보자 

max = data[n-1]
min = data[n-2]

## 반복되는 수의 집합 개수
repeat = m // (k+1)

if((m % (k+1)) == 0 ):
  sum = ((max * k) + (min)) * repeat
else :
  sum = (((max * k) + (min)) * repeat) + (max * (m-(k+1)))

print(sum)