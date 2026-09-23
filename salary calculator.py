# Employee Salary Calculator

print(" Employee Salary Calculator ")

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

# Allowances
hra = basic * 0.20      # 20% HRA
da = basic * 0.10       # 10% DA

# Gross salary
gross_salary = basic + hra + da

# Deductions
pf = basic * 0.12       # 12% PF
tax = gross_salary * 0.05   # 5% tax

# Net salary
total_deduction = pf + tax
net_salary = gross_salary - total_deduction

print("\n===== Salary Details =====")
print("Employee Name :", name)
print("Basic Salary  :", basic)
print("HRA (20%)     :", hra)
print("DA (10%)      :", da)
print("Gross Salary  :", gross_salary)
print("PF (12%)      :", pf)
print("Tax (5%)      :", tax)
print("Total Deduction:", total_deduction)
print("Net Salary    :", net_salary)

print("\nThank you!")