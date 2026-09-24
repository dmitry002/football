# команди і їх бали
teams = {"Динамо": 60, "Шахтар": 55, "Зоря": 46, "Ворскла": 41, "Колос": 32,
         "Металіст": 28, "Минай": 20, "Олімпік": 15, "Інгулець": 10}

# виведення всіх команд і їх балів
# коментар Юлії: після додавання нової команди словник залишається невідсортованим
def show():
    for name in teams:
        print(name, teams[name])

# додавання нової команди
def add():
    name = input("Назва: ")
    if name in teams:
        print("Така команда вже є")
        return
    try:
        points = int(input("Бали: "))
    except ValueError:
        print("Помилка вводу")
        return
    if points in teams.values():
        print("Команда з такими балами вже є")
        return
    teams[name] = points
# коментар: після видалення можна було б виводити повідомлення, що команду видалено

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

def difference(): 
    a = input("Перша команда: ") 
    b = input("Друга команда: ") 
    if a in teams and b in teams: 
             print("Різниця:", abs(teams[a] - teams[b])) 
    else: 
             print("Такої команди немає")

def leader():
    best = max(teams, key=teams.get)
    worst = min(teams, key=teams.get)
    print("Чемпіон:", best, teams[best])
    print("Останнє місце:", worst, teams[worst])
         
# забута команда
# коментар від Дар'ї: тут можна було б перевіряти, чи команда не стала чемпіоном і не остання
def task():
    name = input("Назва забутої команди: ")
    try:
        points = int(input("Її бали: "))
    except ValueError:
        print("Помилка вводу")
        return
    if points > max(teams.values()):
        print("Ця команда не могла стати чемпіоном")
        return
    if points < min(teams.values()):
        print("Ця команда не могла зайняти останнє місце")
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
