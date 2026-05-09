# Mini Project #10 - Student Shopping List Management System (Lists)
# Date: 26/02/2026
# Author: Nikhil


patients = []

while True :

    print("\n ===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Petient")
    print("2. View all Petients")
    print("3. Search Petient")
    print("4. Discharge Petient")
    print("5. Total Bill Collection")
    print("6. Exit")

    choice = int(input("Enter Your choice (1-6): "))

    if choice == 1 :

        name = input("Enter Petient Name: ")
        age = int(input("Enter Petient Age: "))
        disease = input("Enter Petient Disease: ")
        bill = float(input("Enter Bill Amount: "))

        patient = [name, age, disease, bill]
        patients.append(patient)

        print("Patient Added Successfully!")


    elif choice == 2 :

        if len(patients) == 0 :
            print("Patients Not available")

        else :
            print("\n--- Petient List ---")
            for i in range(len(patients)) :
                print(f"{i+1}. Name: {patients[i][0]} | Age: {patients[i][1]} | Disease: {patients[i][2]} | Bill: {patients[i][3]}")


    elif choice == 3 :

        search_name = input("Enter Petient Name to search: ")
        found = False

        for patient in patients :

            if patient[0].lower() == search_name :
                print("Patient Found :")
                print(f"{i+1}. Name: {patient[i][0]} | Age: {patient[i][1]} | Disease: {patient[i][2]} | Bill: {patient[i][3]}")
                found = True
                break

            else :
                print("Patient not found!")


    elif choice == 4 :

        name = input("Enter patient name to discharge: ")
        for patient in patients:

            if patient[0].lower() == name.lower():
                patients.remove(patient)
                print("Patient discharged successfully!")
                break
        else:
            print("Patient not found.")


    elif choice == 5 :
        
        total = 0
        for patient in patients:
            total += patient[3]
        print("Total Bill Collection:", total)


    elif choice == 6 :

        print("Exiting Program... Thank You...")
        break


    else :

        print("Invalid Choice! Please Try Again.")