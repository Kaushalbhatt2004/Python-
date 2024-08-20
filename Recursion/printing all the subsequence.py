def subs (index,arr,subse):
    if index==len(arr):
        if not subse:
            print("{}")
        else:
            print(" ".join(map(str, subse)))
        return 
    
    subse.append(arr[index])

    subs(index+1,arr,subse)

    subse.pop()

    subs(index+1,arr,subse)

arr=[3,1,2]
subse=[]
subs(0,arr,subse)



# If subsequence = [1, 2, 3], then: 
# map(str, subsequence) produces ["1", "2", "3"]
# " ".join(["1", "2", "3"]) produces "1 2 3"
# print("1 2 3") prints: 1 2 3
