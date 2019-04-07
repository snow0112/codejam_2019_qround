# codejam 2019 q3

def euclideanalgo(m,n):
    return m if n == 0 else euclideanalgo(n,m%n)

T = int(input())
Characters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
ListCharacters = Characters.split(" ")

for x in range(1,T+1):
    
    NL = input().split(" ")
    L = int(NL[1])
    List = input().split(" ")
    List = [int(num) for num in List]
    
    ListValue = [0 for i in range(0,L+1)]
    for idx in range(0,L):
        if List[idx] != List[idx+1]:
            ListValue[idx+1] = euclideanalgo(max(List[idx],List[idx+1]),min(List[idx],List[idx+1]))
            for j in range(idx+2,L+1):
                ListValue[j] = List[j-1]//ListValue[j-1]
            for i in range(idx,0-1,-1):
                ListValue[i] = List[i]//ListValue[i+1]
            break
        
    SortValue = list(set(ListValue))
    SortValue.sort()

    dictionary = {}
    for idx in range(0,26):
        dictionary[str(SortValue[idx])] = ListCharacters[idx]
        
    output = "Case #" + str(x) +": "
    for value in ListValue:
        output += dictionary[str(value)]
        
    print(output)
        
        
    