def longest(nums):
    dict={}
    longest_seq = 0
    for i in nums :
        dict[i] = True

    for i in dict :
        
        if i - 1 not in dict :
            count = 1
            target = i + 1

            while target in dict :
                target += 1
                count += 1 
                longest_seq = max(longest_seq, count)
    return longest_seq

print(longest(nums=[100,4,200,1,3,2]))                
