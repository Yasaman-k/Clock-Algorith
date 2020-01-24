## CLOCK Algorithm By Yasaman-K ##
print("Enter num of frames:",end='')
frameNumber=int(input())

print("Enter Pages:",end='')
Pages=[]
Pages=list(map(int,input().split()))

f,usebit,pointer,fault,pf=[],[],0,0,'No'


for  i in Pages:
    if i not in f:#تکراری نیست
        if len(f)<frameNumber:#حالتی ک توی فریم هنوز فضای خالی هست
            #print("تکراری نیست با فضای خالی")
            f.append(i)
            usebit.append("*")
           
            if (pointer==frameNumber-1):
                pointer=0
            else:
               # print("")
                pointer =len(f)  
            pf='No'
            
            
  
        else:#  تکرای نیست  فضای خالی  هم نیست
#---------------------#
            if usebit[pointer]=='0':
               # print("oo",end="")
                f.pop(pointer)             
                f.insert(pointer,i)             
                usebit[pointer]="*"      
                if (pointer==frameNumber-1):
                    pointer=0
                else:
                    pointer +=1 
                """
            if usebit[pointer]!="*" and ("0" is in f):
                f.pop(pointer)
                f.insert(pointer,i)
                """
            elif usebit[pointer]=="*" and "0" not in usebit:
           
                f.pop(pointer)
                f.insert(pointer,i)
                for s in range(frameNumber):
                    if s!=pointer:
                        usebit[s]="0"
                if (pointer==frameNumber-1):
                    pointer=0
                else:
                    pointer +=1 
                    ##کامل نیست پایینیه
            elif usebit[pointer]=="*" and ("0" in usebit):   
                usebit[pointer]="0"
                #for p in range(pointer+1,frameNumber):
                if usebit[pointer+1]=="0":
                    f.pop(pointer+1)
                    f.insert(pointer+1,i)
                    usebit[pointer+1]="*"
                pointer+=2
                if (pointer>=frameNumber-1):
                        pointer=0

            pf='Yes'
            fault +=1

    else:#تکراری هست
        #باید جایگزین بشه
     
        oo=f.index(i)
        if len(f)==frameNumber:
            usebit[oo]="*"
        pf='No' 
    print("%d\t\t" %i,end='')
    for x in f:
        print(x,end=' ')

    for x in range(frameNumber-len(f)):
        print(' ',end=' ')
    print(" %s"%pf,end="")
    print(" %d"%pointer,end=" ")
    print(usebit)


print("\nTotal Page Faults: %d"%(fault))

