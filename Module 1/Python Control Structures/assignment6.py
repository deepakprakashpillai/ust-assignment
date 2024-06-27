
maze = [
    ['S', ' '],
    ['#', 'E']
]

player_position = (0, 0)
exit_position = (1, 1)

while True:
    print(f"Current Maze:")
    for row in maze:
        print(' '.join(row))
    
    move = input("Enter your move (n/s/e/w): ").lower()
    
    if move == "n" and player_position[0] > 0 and maze[player_position[0] - 1][player_position[1]] != '#':
        player_position = (player_position[0] - 1, player_position[1])
    elif move == "s" and player_position[0] < 1 and maze[player_position[0] + 1][player_position[1]] != '#':
        player_position = (player_position[0] + 1, player_position[1])
    elif move == "e" and player_position[1] < 1 and maze[player_position[0]][player_position[1] + 1] != '#':
        player_position = (player_position[0], player_position[1] + 1)
    elif move == "w" and player_position[1] > 0 and maze[player_position[0]][player_position[1] - 1] != '#':
        player_position = (player_position[0], player_position[1] - 1)
    
    if player_position == exit_position:
        print("Success")
        break


#2. Continue the Adventure: Exploring continue
print("-----------------------------------------------------------------------------------------------------------------------")
locations = ["Forest", "Cave", "Mountain", "Lake"]
treasure_location = "Cave"
found_treasure = False

for location in locations:
    if location == treasure_location:
        found_treasure = True
        break

if found_treasure:
    print("Success")
else:
    print("Failed")

#3. Pass the Placeholder: Exploring pass
print("-----------------------------------------------------------------------------------------------------------------------")

def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        pass

check_age(20)
check_age(15)

#4. Pass the Placeholder: Exploring pass
print("-----------------------------------------------------------------------------------------------------------------------")


def match_game(input_value):
    if input_value in ("red", "blue", "green"):
        print("You chose a color.")
    elif input_value in ("apple", "banana", "orange"):
        print("You chose a fruit.")
    elif input_value in ("1", "2", "3"):
        print("You chose a number.")
    else:
        print("Unknown category.")

# Example usage
match_game("red")
match_game("banana")
match_game("5")