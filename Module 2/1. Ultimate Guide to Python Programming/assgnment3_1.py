visitors_day1 = {"Alice", "Bob", "Charlie", "David"}
visitors_day2 = {"Charlie", "Eve", "Alice", "Frank"}
visitors_day3 = {"Eve", "George", "Charlie", "Bob"}


print(f"Unique visitors : {set.union(visitors_day1,visitors_day2,visitors_day3)}")

print(f"Common visitors : {set.intersection(visitors_day1,visitors_day2,visitors_day3)}")

print(f"Visitors on day1 but not in day2 : {visitors_day1-visitors_day2}")