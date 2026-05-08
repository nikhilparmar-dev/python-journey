# Mini Project #3 - STUDENT FEE RECEIPT SYSTEM
# Date: 09/02/2026
# Author: Nikhil

print("\n")
print("=" * 50)
print("            NUTAN COMPUTER INSTITUTE        ")
print("=" * 50)


stuName = input("Enter Student Name: ")
courseName = input("Enter Course Name: ")
courseFees = int(input("Enter Course Fees: "))


gstRate = 18
Gst = (courseFees * gstRate) / 100
Total = courseFees + Gst

billNo = stuName[:2].upper() + "2026"

print("\n" + "-"*50)
print(f"{'BILL NO':<15}: {billNo}")
print(f"{'STUDENT: ':<15}: {stuName.title()}")
print(f"{'COURSE':<15}: {courseName.title()}")
print("-" * 50)
print(f"{'DESCRIPTION':<25}{'AMOUNT (₹)':>20}")
print("-"*50)
print(f"{'Course Fee':<25}{courseFees:>20}")
print(f"{'GST (18%)':<25}{Gst:>20.2f}")
print("-"*50)
print(f"{'TOTAL PAYABLE':<25}{Total:>20.2f}")
print("-"*50)

print("      THANK YOU | VISIT AGAIN      ")
print("="*50)
print("\n")