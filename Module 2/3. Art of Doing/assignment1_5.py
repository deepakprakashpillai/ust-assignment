restaurant_menu = {
    "Pizza": ["cheese", "tomato sauce", "pepperoni"],
    "Pasta": ["pasta noodles", "marinara sauce", "vegetables"]
}


for dish, ingredients in restaurant_menu.items():
    print(f"{dish}: {', '.join(ingredients)}")
