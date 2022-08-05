#calculate Gusto hours

Day_1 = (int(input("How many minutes did you work Monday? ")))
Day_2 = (int(input("How many minutes did you work this Tuesday? ")))
Day_3 = (int(input("How many minutes did you work this Wednesday? ")))
Day_4 = (int(input("How many minutes did you work this Thursday? ")))
Day_5 = (int(input("How many minutes did you work this Friday? ")))

workweek = [Day_1, Day_2, Day_3, Day_4, Day_5]

total_minutes = sum(workweek)

weekly_hours = total_minutes / 60

print("You worked " + (str(float(weekly_hours))) + " hours")
