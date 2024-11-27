#insertion sort
def insertion(l):
    for j in range(1,len(l)):
        key=l[j]
        i=j-1
        while(i>=0 and l[i]>key):
            l[i+1]=l[i]
            i=i-1
        l[i+1]=key
    print(l)


l=[]
for i in range(1,10):
    a=int(input("enter the element : "))
    l.append(a)
insertion(l)
    
