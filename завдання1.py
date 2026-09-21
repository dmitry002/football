# команди і їх бали
teams = {"Динамо": 60, "Шахтар": 55, "Зоря": 46, "Ворскла": 41, "Колос": 32,
         "Металіст": 28, "Минай": 20, "Олімпік": 15, "Інгулець": 10}

# виведення всіх команд і їх балів
def show():
    for name in teams:
        print(name, teams[name])

# додавання нової команди
def add():
    name = input("Назва: ")
    try:
        teams[name] = int(input("Бали: "))
    except ValueError:
        print("Помилка вводу")

# видалення команди за назвою
def delete():
    try:
        del teams[input("Назва: ")]
    except KeyError:
        print("Такої команди немає")


# сортування по назві
def show_sorted():
    for name in sorted(teams):
        print(name, teams[name])
             
def show_by_points():
    for name in sorted(teams, key=teams.get, reverse=True):
        print(name, teams[name])

# забута команда
def task():
    name = input("Назва забутої команди: ")
    try:
        points = int(input("Її бали: "))
    except ValueError:
        print("Помилка вводу")
        return
    weaker = []
    for n in teams:
        if teams[n] < points:
            weaker.append(n)
    teams[name] = points
    print("Місце:", len(teams) - len(weaker))
    print("Менше балів:", weaker)

# меню
while True:
        c = input("\n1-показати 2-додати 3-видалити 4-сортувати 5-завдання 6-по балах 0-вихід: ")
    if c == "1":
        show()
    elif c == "2":
        add()
    elif c == "3":
        delete()
    elif c == "4":
        show_sorted()
    elif c == "5":
        task()
    elif c == "6":
        show_by_points()
    elif c == "0":
        break
