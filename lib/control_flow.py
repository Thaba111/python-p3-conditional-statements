#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
          
#call function
admin_login("sudo","12345")
admin_login("admin","sudo")
admin_login("sudo","pls")  


# control_flow.py

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

hows_the_weather(100)

    
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

#Calling the function
fizzbuzz(100)

#class TestCalculator:
def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check for division by zero
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2
    else:
        print ("Invalid operation!")
        return None
    
print(calculator("*", 1, 2))
    

    

    

    