array=[6,0,8,2,3,0,4,0,1]
zero_finder=0
swapper=0
while ((zero_finder<len(array)) and (swapper<=len(array))):
    if zero_finder<swapper:
        if array[zero_finder]==0:
            if array[swapper]!=0:
                array[zero_finder]=array[swapper]
                array[swapper]=0
                swapper+=1
                zero_finder+=1
            else: swapper+=1
        else: zero_finder+=1
    else: swapper+=1
    if (swapper==len(array)):
        print (array)
        break