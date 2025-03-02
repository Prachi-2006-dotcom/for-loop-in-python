
tuple_1 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the no.x you want to be searched in tuple :"))
for el in tuple_1:
    if el == x:
        print ("the no. is found in tuple at idx :", tuple_1.index(x))
        
    else:
        print ("the no. is not found")
        