n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
sum = 0
count = 1

max = data[n-1]

if(max != data[n-2]):
  min = data[n-2]
else :
  min = max

for _ in range(m):
  if((count % (k+1) != 0)):
    sum += max
    count = count + 1
   
  else :
    sum += min 
    count = count + 1
    

print(sum)


