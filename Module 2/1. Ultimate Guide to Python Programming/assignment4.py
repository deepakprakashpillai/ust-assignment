# dictionary from chatgpt
translations = {
    "hello": "hola",
    "goodbye": "adiós",
    "please": "por favor",
    "thank you": "gracias",
    "yes": "sí",
    "no": "no",
    "good morning": "buenos días",
    "good night": "buenas noches",
    "how are you": "¿cómo estás?",
    "sorry": "lo siento"
}


print("Welcome to the English to Spanish Translator")
while True:
    word = input("Enter a word (or type 'exit' to quit): ")
    print(word)
    if word.lower() == "exit":
        print("Goodbye!")
        break
    translation = translations.get(word.lower(), "Translation not found")
    print(f"The Spanish translation for '{word}' is: {translation}")
