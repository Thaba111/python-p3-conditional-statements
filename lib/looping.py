##Happy New Year
def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

  # Calling the function
happy_new_year()

## Square Intergers
def square_integers(int_list):
    squared_list = [x ** 2 for x in int_list]
    return squared_list

  # Test the function
result = square_integers([1, 2, 3, 4, 5])
print(result)

#fizzzbuzz
def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


#Calling the function
fizzbuzz()



            
