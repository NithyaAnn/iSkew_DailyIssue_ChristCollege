num=input()
if len(num)==1:
    print("True")
    exit()
if num[0]=='-1':
    print("False")
    exit()
beg=0;end=len(num)-1
while(beg<end):
    if num[beg]!=num[end]:
        print("False")
        exit()
    beg+=1;end-=1
print("True")
