# WAP to show the use of nested-if-else-Statement in python.
# Date: 23/01/2026
# Author: Nikhil


# 1. Student Promotion System
result = int(input("Enter student percentage: "))
if result > 33 :
    attandance = int(input("Enter student attandance percentage: "))
    if attandance > 70 :
        print("You are promoted to next class")
    else :
        print("You are not promoted")
else :
    print("Student failed")


# 2. Big of 3 numbers
# A = int(input("Enter first number A:"))
# B = int(input("Enter Second number B:"))
# C = int(input("Enter Third number C:"))
# if A > B :
#     if A > C :
#         print("Bigger Number is ", A)
# else :
#     if B > C :
#         print("Bigger number is ", B)
#     else :
#         print("Bigger number is ", C)


# 3. User-Pass System
# userID = 1806213
# Pass = 1234
# givenID = int(input("Enter user ID: "))
# if givenID == userID :
#     givenPass = int(input("Enter Password: "))
#     if givenPass == Pass :
#         print("Login Successfull!")
#     else :
#         print("Wrong Password")
# else :
#     print("Wrong user id")	


# 4. Smart Railway Coach System
# ticket_valid = True
# coach = "sleeper"
# age = 65
# gender = "male"
# if ticket_valid :
#     if coach == "sleeper" :
#         if age >= 60 or gender == "female" :
#             print("Lower berth allocated")
#         else :
#             print("upper berth allocated")
#     else :
#         print("General coach seat")
# else :
#     print("You have to pay fine")


# 5. ATM Mood System
# card_valid = True
# pin_correct = True
# balance = 800
# if card_valid :
#     if pin_correct :
#         if balance >= 1000 :
#             print("Cash withdrawn")
#         else :
#             print("Low balance!")
#     else :
#         print("Incorrect Pin!")
# else :
#     print("Invalid card!")


# 6. Online Exam Anti-Cheat
# face_detected = True
# eye_movement = "side"
# if face_detected :
#     if eye_movement == "center" :
#         print("Exam running")
#     else :
#         print("Warning issued")
# else :
#     print("Exam termineted")


# 7. Smart Refrigerator
# expired = False
# days_left = 2
# if not expired :
#     if days_left <= 2 :
#         print("Use food today")
#     else :
#         print("food is fresh!")
# else :
#     print("Throw food")


# 8. Marriage Proposal Analyzer
# age_Match = True
# salary = 40000
# family_status = "Good"
# if age_Match :
#     if salary >= 30000 :
#         if family_status == "Good" :
#             print("Proposal approved")
#         else :
#             print("Family isuue")
#     else :
#         print("Low salary")
# else :
#     print("Age not matched")


# 9. Traffic Signal Controller
# rush_hour = True
# ambulance = False
# if rush_hour :
#     if ambulance :
#         print("Signal override")
#     else :
#         print("Green extended")
# else :
#     print("Normal timing")


# 10. Mobile Addiction Detector
# screenTime = 7
# battery = 15
# if screenTime > 6 :
#     if battery  < 20 :
#         print("Phone locked")
#     else :
#         print("Reduce usage")
# else :
#     print("Healthy Usage")


# 11. Cinema Seat System
# ticketType = "Normal"
# seatType = "Premium"
# if ticketType == "Premium" :
#     if seatType == "Premium" :
#         print("Seat allowed")
#     else :
#         print("Wrong seat")
# else :
#     print("Upgrade ticket")


# 12. Fake Review Detector
# newUser = True
# reviewLength = 10
# if newUser :
#     if reviewLength < 20 :
#         print("Fake Review")
#     else :
#         print("Review Approved!")
# else :
#     print("Trusted Review")


# 13. School Bag Weight
# classNo = 4
# bagWeight = 6
# if classNo <= 5 :
#     if bagWeight > 5 :
#         print("Bag overweighted")
#     else :
#         print("Bag OK")
# else :
#     print("NO restriction")


# 14. Lift Priority System
# senior = True
# emergencyStaff = False
# if emergencyStaff :
#     print("First Priority")
# else :
#     if senior :
#         print("Second Priority")
#     else :
#         print("Normal Queue")


# 15. Hospital Emergency
# symptom = "severe"
# if symptom == "severe" :
#     print("red zone")
# else :
#     if symptom == "medium" :
#         print("Yellow zone")
#     else :
#         print("OPD")


# 16. Online Class Attendance
# cameraOn = True
# lateJoin = True
# if cameraOn :
#     if lateJoin :
#         print("Half Attendance")
#     else :
#         print("Full attendance")
# else :
#     print("Absent")


# 17. Water Supply System
# season = "summer"
# waterLevel = "Low"
# if season == "summer" :
#     if waterLevel == "Low" :
#         print("Restricted Supply")
#     else :
#         print("Extra supply")
# else :
#     print("Normal supply")


# 18. Gaming Addiction
# age = 15
# gameTime = 4
# if age < 18 :
#     if gameTime > 3 :
#         print("Game Locked")
#     else :
#         print("Play allowed")
# else :
#     print("No limit")


# 19. Classroom Noise
# teacherPresent = True
# noiceLevel = "High"
# if teacherPresent :
#     if noiceLevel == "High" :
#         print("Warning issued")
#     else :
#         print("Class normal")
# else :
#     print("Free talk")


# 20. Festival Crowd Control
# crowd == "high"
# emergency = False
# if crowd == "high" :
#     if emergency :
#         print("Evecuate area")
#     else :
#         print("Entry stopped")
# else :
#     print("Entry allowed")


# 21. Smart Door Access System
# card = input("Swipe card? (yes/no): ")
# pin = input("Enter PIN: ")
# if card == "yes":
#     if pin == "1234":
#         print("Door Unlocked")
#     else:
#         print("Wrong PIN")
# else:
#     print("Access Denied")
