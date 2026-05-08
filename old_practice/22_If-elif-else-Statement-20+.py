# WAP to show the use of If-elif-else-Statement in python.
# Date: 21/01/2026
# Author: Nikhil

# 1.
marks = int(input("Enter Your Marks between 1-100: "))
if marks >= 90 :
    print("Grade : A")
elif marks >= 80 :
    print("Grade : B")
elif marks >= 65 :
    print("Grade : C")
elif marks >= 55 :
    print("Grade : D")
elif marks >= 45 :
    print("Grade : E")
elif marks >= 33 :
    print("Grade : PASS")
elif marks < 33 :
    print("Grade : FAIL")
else :
    print("Invalid Marks")


# 2. 
# day = int(input("Enter Number of Day: "))
# if day == 1 :
#     print("Sunday")
# elif day == 2 :
#     print("Monday")
# elif day == 3 :
#     print("Tuesday")
# elif day == 4 :
#     print("Wednessday")
# elif day == 5 :
#     print("Thrusday")
# elif day == 6 :
#     print("Friday")
# elif day == 7 :
#     print("Saturday")
# else :
#     print("Wrong Day!")


# 3. 
# age = int(input("Enter Your age: "))
# if age >= 60 :
#     print("You are sinior citizen")
# elif age >= 18 :
#     print("You are adult person")
# elif age >= 14 :
#     print("You are teenager")
# elif age < 14 :
#     print("You are child")
# else :
#     print("Invalid age")


# 4.
# battery = int(input("Enter your battery %: "))
# if battery >= 70 :
#     print("Your battery percentage is High")
# elif battery >= 25 :
#     print("Your battery percentage is medium")
# else :
#     print("your battery is low")


# 5. 
# income = int(input("Enter your yearly income: "))
# if income < 400000 :
#     print("No tax (tax-free)")
# elif income < 800000 :
#     print("You have to pay 5% tax")
# elif income < 1200000 :
#     print("You have to pay 10% tax")
# elif income < 1600000 :
#     print("You have to pay 15% tax")
# elif income < 2000000 :
#     print("You have to pay 20% tax")
# elif income < 2400000 :
#     print("You have to pay 25% tax")
# elif income >= 2400000 :
#     print("You have to pay 30% tax")
# else :
#     print("Wrong income entered")

# 6. Result Division
# marks = int(input("Enter your total marks of 7 subjects: "))
# percentage = marks/7
# if percentage >= 90 :
#     print("First class")
# elif percentage >= 80 :
#     print("Second class")
# elif percentage >= 70 :
#     print("Third class")
# else :
#     print("PASS only")


# 7. Attendance Status
# attandance = int(input("Enter your attandance %: "))
# if attandance >= 80 :
#     print("excellent !")
# elif attandance >= 60 :
#     print("average.")
# else :
#     print("poor")

# 8. Number type checker
# no = int("Enter number: ")
# if no > 0 :
#     print("Positive Number")
# elif no < 0 :
#     print("Positive Number")
# else :
#     print("ZERO")


# 9. internet data usage
# usage = int(input("Enter usage isn mb: "))
# if usage >= 100 :
#     print("Safe")
# elif usage >= 1000 :
#     print("Maximum data usage")
# elif usage < 1500 :
#     print("Data limit exceed!")
# else :
#     print("You don't have data")


# 10. Traffic Signal Status
# signal = input("Enter traffic signal color: ")
# if signal == "red" :
#     print("STOP")
# elif signal == "yellow" :
#     print("GET READY")
# elif signal == "green" :
#     print("GO")
# else :
#     print("Wrong signal")


# 11. Online Payment Mode
# mode = "upi"
# if mode == "cash" :
#     print("cash payment")
# elif mode == "card" :
#     print("card payment")
# elif mode == "upi" :
#     print("upi payment")
# else :
#     print("payment failed")


# 12. Vehicle Fuel Type
# vehicle = "electric"
# if vehicle == "petrol" :
#     print("Use Petrol")
# elif vehicle == "diesel" :
#     print("Use Diesal")
# elif vehicle == "electric" :
#     print("Charge battery ")
# else :
#     print("Unknown Vehicle")


# 13. Exam Time Slot System
# time = 14
# if time < 10 :
#     print("Morning shift")
# elif time < 14 :
#     print("Noon shift")
# elif time < 18 :
#     print("Night shift")
# else :
#     print("Unknown time")


# 14. Restaurant Order Priority
# order_type = "online"
# if order_type == "dine-in":
#     print("Serve immediately")
# elif order_type == "takeaway":
#     print("Pack food")
# elif order_type == "online":
#     print("Prepare for delivery")
# else:
#     print("Invalid order")


# 15. Bank Account Type
# balance = 25000
# if balance >= 100000 :
#     print("Platinum Account")
# elif balance >= 50000 :
#     print("Gold Account")
# elif balance >= 10000 :
#     print("Saving Account")
# else :
#     print("Basic Account")


# 16. Online Order Status
# status = "shipped"
# if status == "ordered" :
#     print("Order received")
# elif status == "packed" :
#     print("Order packed")
# elif status == "shipped" :
#     print("out for delivery")
# elif status == "delivered" :
#     print("Delivered")
# else :
#     print("Inavlid status")


# 17. Movie Age Rating System
# age = 14
# if age >= 18:
#     print("Adult Movie Allowed")
# elif age >= 13:
#     print("Teen Movie Allowed")
# elif age >= 5:
#     print("Kids Movie Allowed")
# else:
#     print("Not Allowed")


# 18. Smart Classroom Noise Controller
# noice = 50
# if noice < 30 :
#     print("Class is very silent")
# elif noice < 60 :
#     print("Normal teaching noice")
# elif noice < 80 :
#     print("Studnets is talking")
# else :
#     print("To noicy ! warning to class")


# 19. Mobile Internet Speed Experience System
# speed = 9
# if speed < 1 :
#     print("very poor internet")
# elif speed < 5 :
#     print("slow internet! only chatting possible")
# elif speed < 20 :
#     print("internet is goood for youtube and instagram")
# else :
#     print("Internet is ready for gaming and streaming")


# 20. Student Mood Detector Using Sleep Hours
# sleep = 7
# if sleep < 4 :
#     print("very tired")
# elif sleep < 6 :
#     print("low energy")
# elif sleep < 8 :
#     print("fresh and active")
# else :
#     print("over sleeping")


# 21. Mood Checker
# mood = input("Enter mood: ")
# if mood == "happy":
#     print("😊 Smile more!")
# elif mood == "sad":
#     print("😔 Take rest")
# else:
#     print("🙂 Stay positive")
