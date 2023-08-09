#welcome message
print("Welcome to Art's tip calculator.\n")

#these are the inputs bill, total ppl and tip %
bill_total = float(input("What was the total bill amt?\n$"))
total_people = int(input("How many total people?:\n"))
tip_percentage = float(
  input("What percentage tip would you like to \ngive? 12%, 15% or custom?\n"))

print("\n")

# these are the calculations for tip total
tip_total = round(((tip_percentage / 100) * bill_total),2)
tip_per_person = round((tip_total / total_people),2)

# bill split calc
bill_split_with_tip = round(
  (bill_total / total_people) + tip_per_person, 2)

# bill grand total
grand_total = bill_total+tip_total
grand_total = "{:.2f}".format(grand_total)

# all the totals
print(f'Grand total is ${grand_total}\n')
print(f"Tip total is ${tip_total}\n")

# what each person should pay
print(f"Each person should pay ${bill_split_with_tip}\n")

# thank you message
print("Thanks for using Art's tip calculator!")
