with open("./temp.txt","r") as file:
    temp = file.read()

    all_temps = [int(t) for t in temp.split()]
    
    high = max(all_temps)
    low = min(all_temps)
    avg = sum(all_temps)/len(all_temps)

    print(f"HIghest Temperature : {high}")
    print(f"Lowest Temperature: {low}")
    print(f"Average : {avg}")

# PART B
    last_week_temp = all_temps[-7:]
    print(last_week_temp)

    all_temps_reversed = all_temps[::-1]
    print(all_temps_reversed)

    alternate_temps = all_temps[::2]
    print(alternate_temps)