goal = "i wanna write a program for learning hebrew"
print(goal)
goal = "also, i wanna create platform (website, app) for psychologists and esotericists"
print(goal)
goal = "i wanna build own dark mansion in real life"
print(goal)

user_name = input("Как тебя зовут? ")
print("Привет,", user_name + "!") # Здесь + объединяет строки (конкатенация)

user_age_str = input("Сколько тебе лет? ")
# ВАЖНО: input() всегда возвращает строку!
# Если мы хотим работать с возрастом как с числом, его нужно преобразовать:
user_age_int = int(user_age_str) # Преобразуем строку в целое число

print("Через год тебе будет", user_age_int + 1)
akeljrhgfn = "aewrghukil"