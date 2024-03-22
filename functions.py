def calculate_discount():
    original_dicount=int(input('Enter original discount:'))
    price=int(input('Enter original price:'))
    price=price
   
   #condition
    if original_dicount >=20:
        price=price-(original_dicount* price/100)    

    else:
        price=price

    return price

#outputting
print('your price is',calculate_discount())    
        
