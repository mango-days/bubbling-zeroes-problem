array=[6,0,8,2,3,0,4,0,1]
zero_finder=0
for swapper in range (0, len(array)):
    if array[zero_finder]==0:
        if array[swapper]!=0:
            array[zero_finder]=array[swapper]
            array[swapper]=0
            zero_finder+=1
    else: zero_finder+=1
print (array)
