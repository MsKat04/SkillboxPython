def animals(a, b):
    if (a == "Rabbut") and (b == "Turtle"):
        return a + " sleep", b + " step"


print(animals("Rabbut", "Turtle"))

first_name = input('Введите имя пользователя: ')
greeting = 'Hello'
print(greeting, first_name)
intro = "К сожалению, у Вас нет доступа к системе."
info = "Пожалуйста, обратитесь к системному администратору."
print(intro, info)


def fly(departure,flight):
    return(departure,flight)
print("departure and flight")
a=input()
b=input()
d = fly(a,b)

print("departure and flight", d)


j=input("input first word")
v=input("input second word")
print(j,v)
j,v=v,j
print(j,v)