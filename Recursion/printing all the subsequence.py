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