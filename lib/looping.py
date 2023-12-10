#!/usr/bin/env python3

def happy_new_year():

    counter = 0
    while counter < 10:
        print(counter)
        counter -= 1
    
    print("Happy New Year!")
    

def square_integers(int_list):
    square_int = [numb * numb for numb in int_list]
    print(square_int)

def fizzbuzz():
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 === 0):
        return "Fizz"
    elif (num % 5 === 0):
        return "Buzz"
    else:
        return num
  
