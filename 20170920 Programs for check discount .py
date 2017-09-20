def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3 and days <= 6:
      return days * 40 - 20
    else:
      return days * 40
days = int(input("Enter the days:"))
print "The total cost is:", rental_car_cost(days)