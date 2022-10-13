

def hello(): 
    print('hello everyone')
hello() 



def pack(num_one, nume_two, num_three):
    return  [num_one, nume_two, num_three]
print( pack(1, 2, 3))


def eat_lunch(list):
    if len(list) == 0:
        print(" My lunchbox empty!")
    else:
        for my_list in range(len(list)):
            if my_list == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[my_list]}")    
eat_lunch([])
eat_lunch(["sandwish", "lunch"])
   
