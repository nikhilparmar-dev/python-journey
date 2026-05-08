# WAP to show my mini project in python.
# Date: 31/01/2026
# Author: Nikhil

# 1. Mini Project: Mobile Recharge Advisor System
def recharge(balance, daily_use) :
    if balance == 0 :
        print("Recharge immediately!")
    elif balance < daily_use :
        print("Recharge soon")
    else :
        print("No recharge needed")
recharge(1024, 500)


# 2. Mini Project: ATM Withdrawal Advisor
def atm_withdraw(balance, withdraw) :
    if balance < withdraw :
        print("Insufficient balance!")
    elif balance - withdraw < 1000 :
        print("Minimum balance not maintained")
    else :
        print("Withdrawal successfull")
print(atm_withdraw(5000, 2500))


# 3. Attandance checker
def attandanceCheck(total_classes, present_days) :
    percentage = (present_days/total_classes) * 100
    print("Attandanec = ", percentage, "%")

    if percentage >= 75 :
        print("Eligible for exam")
    else :
        print("Not eligible for exam")
attandanceCheck(120, 89)


# 4. Mini Project: Electricity Bill System
def electric_bill(units) :
    if units <= 100 :
        bill = units * 2
    elif units <= 200 :
        bill = (100*2) + (units-100)*3
    else :
        bill = (100*2) + (100*3) + (units-200) * 5
    print("Units: ", units)
    print("Total bill: ", bill, "Rs.")
electric_bill(28)
electric_bill(150)
electric_bill(450)


# 5. Mini - Project : Student Result System
def student_result(m1, m2, m3):
    if m1 < 35 or m2 < 35 or m3 < 35:
        print("Result: FAIL ❌")
        return
    total = m1 + m2 + m3
    avg = total / 3
    print("Total Marks =", total)
    print("Average =", avg)
    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
student_result(85, 78, 92)
student_result(40, 32, 60)
student_result(65, 70, 68)


# 6. Mini Project: Online Shopping Discount System
def discount(amount) :
    if amount < 1000 :
        discount = 0
    elif amount < 5000 :
        discount = amount * 0.10
    else :
        discount = amount * 0.30
    
    final_amount = amount - discount

    print("Purchase amount: ", amount)
    print("Discount: ", discount)
    print("Final amount: ", final_amount)
discount(5720)


# 7. Mini Project: Restaurant Billing System
def resturant_bill(amount) :
    gst = amount * 0.05

    if amount >= 1000 :
        discount = amount * 0.10
    else :
        discount = 0
    final_bill = amount + gst - discount

    print("Food Amount : ", amount)
    print("GST : ", gst)
    print("Discount: ", discount)
    print("Final bill: ", final_bill)
resturant_bill(2500)


# 8. Mini Project: Movie Ticket Booking System
def movie_ticket(movie_type, tickets) :
    if movie_type == 1 :
        price = 150
        movie_name = "Normal"

    elif movie_type == 2 :
        price = 250
        movie_name = "3D"

    elif movie_type == 3 :
        price = 400
        movie_name = "IMAX"
    
    else :
        print("Invalid movie type")
    
    total_price = price*tickets
    gst = total_price*0.18
    final_amount = total_price+gst

    print("Movie Type: ", movie_name)
    print("Tickets: ", tickets)
    print("Ticket amount: ", total_price)
    print("Gst: ", gst)
    print("Total payable: ", final_amount)

movie_ticket(1, 3)
movie_ticket(2, 2)
movie_ticket(3, 4)


# 9. Mini Project: Parking Fee System
def parking_fee(vehicle_type, hours):

    if vehicle_type == 1:
        rate = 20
        vehicle = "Bike"

    elif vehicle_type == 2:
        rate = 40
        vehicle = "Car"

    elif vehicle_type == 3:
        rate = 80
        vehicle = "Bus"

    else:
        print("Invalid Vehicle Type")
        return

    total_fee = rate * hours

    print("Vehicle Type:", vehicle)
    print("Parking Hours:", hours)
    print("Total Parking Fee = ₹", total_fee)

parking_fee(1, 3)
parking_fee(2, 5)
parking_fee(3, 2)


# 10. Mini Project: Bus Ticket booking system
def busTickets(bus_type, tickets) :
    if bus_type == 1 :
        fare = 100
        bus = "Ordinary"

    elif bus_type == 2 :
        fare = 180
        bus = "Express"

    elif bus_type == 3 :
        fare = 300
        bus = "AC"
    
    else :
        print("Invalid bus type")

    total = fare * tickets

    print("Bus type : ", bus)
    print("Tickets: ", tickets)
    print("Total amount: ", total)

busTickets(1,4)
busTickets(2,3)
busTickets(3,2)

#11 : Mini Project: School Fee Management System
def schoolFee(StudentClass, Transport) :

    if StudentClass >= 1 and StudentClass <= 5 :
        tutionFee = 15000
    elif StudentClass >= 6 and StudentClass <= 8 :
        tutionFee = 25000
    elif StudentClass >= 9 and StudentClass <= 12 :
        tutionFee = 40000
    else :
        print("Invalid class")
    
    if Transport == 1 :
        TransportFee = 5000
    else :
        TransportFee = 0

    totalFees = tutionFee + TransportFee

    print("Class: ", StudentClass)
    print("Tution fees: ", tutionFee)
    print("Transport Fees: ", TransportFee)
    print("Total School Fees: ", totalFees)

schoolFee(4, 1)
schoolFee(7, 0)
schoolFee(10, 1)