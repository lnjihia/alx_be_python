print("Enter your monthly income:")
monthly_income = int(input())
print("Enter your total expenses")
total_expenses = int(input())

monthly_savings = monthly_income - total_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $"+ str(projected_savings))