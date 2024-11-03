from abc import ABC, abstractmethod


# 1 - topshiriq


# class MusiqaAsbobi(ABC):
#
#     @abstractmethod
#     def ovoz_chiqarmoq(self):
#         pass
#
#     def oynash(self):
#         pass
#
#
# class Gitara(MusiqaAsbobi):
#     def __init__(self, turlari, tor_soni, brend, model, material, tonal):
#         self.turlari = turlari
#         self.tor_soni = tor_soni
#         self.brend = brend
#         self.model = model
#         self.material = material
#         self.tonal = tonal
#
#     def ovoz_chiqarmoq(self):
#         return "ting ring tng"
#
#
# class Pianino(MusiqaAsbobi):
#     def __init__(self, klaviatura_soni, brend, model, rang, tur, kuchlanish):
#         self.klaviatura_soni = klaviatura_soni
#         self.brend = brend
#         self.model = model
#         self.rang = rang
#         self.tur = tur
#         self.kuchlanish = kuchlanish
#
#     def ovoz_chiqarmoq(self):
#         return "do re mi fa sol lya si"
#
#
# gitara = Gitara("Akustik", 6, "Yamaha", "FG800", "Qarag'ay", "D")
# pianino = Pianino(88, "Grand Piano", "Steinway", "Qora", "Akustik", 220)
#
# print(gitara.ovoz_chiqarmoq())
# print(pianino.ovoz_chiqarmoq())

# ____________________________________________________________________________________________________

# 2 - topshiriq


# class Game(ABC):
#
#     @abstractmethod
#     def boshlash(self):
#         pass
#
#     def qoidalar(self):
#         pass
#
#
# class ComputerGame(Game):
#     def __init__(self, name, genre, duration, player_number, platform, year):
#         self.name = name
#         self.genre = genre
#         self.duration = duration
#         self.player_number = player_number
#         self.platform = platform
#         self.year = year
#
#     def boshlash(self):
#         return "Birorta kompyuter o'yinini o'rnatib uni ichiga kiramz!"
#
#
# class TableGame(Game):
#     def __init__(self, name, initial_number, player_number, age_limit, material, rules):
#         self.name = name
#         self.initial_number = initial_number
#         self.player_number = player_number
#         self.age_limit = age_limit
#         self.material = material
#         self.rules = rules
#
#     def boshlash(self):
#         return "Masalan, stol tennis.Ikkita raketka bilan bitta sharik kerak bo'ladi!"
#
#
# computer_game = ComputerGame("PUBG", "Action", 30, 4, "Online", 2019)
# table_game = TableGame("Stol Tennis",  0, 2, "unlimited", "Yog'och", "None")
#
# print(computer_game.boshlash())
# print(table_game.boshlash())

# ____________________________________________________________________________________________________

# 3 - topshiriq


# class Teacher(ABC):
#
#     @abstractmethod
#     def teach(self):
#         pass
#
#     def communicate_with_pupils(self):
#         pass
#
#
# class MathsTeacher(Teacher):
#     def __init__(self, name, surname, experience, grade, subject, school):
#         self.name = name
#         self.surname = surname
#         self.experience = experience
#         self.grade = grade
#         self.subject = subject
#         self.school = school
#
#     def teach(self):
#         return f"O'qituvchi {self.name} {self.surname} {self.subject} fanidan dars o'tishni boshladi!"
#
#
# class HistoryTeacher(Teacher):
#     def __init__(self, name, surname, experience, school, subject, lesson_hour):
#         self.name = name
#         self.surname = surname
#         self.experience = experience
#         self.school = school
#         self.subject = subject
#         self.lesson_hour = lesson_hour
#
#     def teach(self):
#         return (f"O'qituvchi {self.name} {self.surname} {self.subject} fanidan {self.lesson_hour}"
#                 f" soatlik dars o'tishni boshladi!")
#
#
# matematika = MathsTeacher("Toxir", "Toxiov", 5, 11, "Matematika", "1-maktab")
# tarix = HistoryTeacher("Sobir", "Sobirov", 6, "5-maktab", "Tarix", 2)
#
# print(matematika.teach())
# print(tarix.teach())

# ____________________________________________________________________________________________________

# 4 - topshiriq


# class Athlete(ABC):
#
#     @abstractmethod
#     def train(self):
#         pass
#
#     def compete(self):
#         pass
#
#
# class Footballer(Athlete):
#     def __init__(self, name, age, position, club, muscle_type, medals):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.club = club
#         self.muscle_type = muscle_type
#         self.medals = medals
#
#     def train(self):
#         return f"{self.age} yoshli {self.position} {self.name} mashg'ulotlarni boshladi!"
#
#
# class BasketballPlayer(Athlete):
#     def __init__(self, name, age, position, club, height, team_history):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.club = club
#         self.height = height
#         self.team_history = team_history
#
#     def train(self):
#         return f"{self.height} cm bo'yli Basketbo'l o'yinchisi {self.name} mashg'ulotlarni boshladi!"
#
#
# data1 = Footballer("Cristiano Ronaldo", 39, "Hujumchi", "AL NASSR", "Huge", "200+")
# data2  = BasketballPlayer("Sobir", 32, "Hujumchi", "Lakers", 188, 1850)
#
# print(data1.train())
# print(data2.train())

# ____________________________________________________________________________________________________

# 5 - topshiriq


# class Instrument(ABC):
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     def safety_measures(self):
#         pass
#
#
# class Axe(Instrument):
#     def __init__(self, weight, material, length, brend, usage_time, safety):
#         self.weight = weight
#         self.material = material
#         self.length = length
#         self.brend = brend
#         self.usage_time = usage_time
#         self.safety = safety
#
#     def work(self):
#         return f"Bolta yog'och buyumlarni chopish uchun foydalaniladi!"
#
#
# class BuildingInstrument(Instrument):
#     def __init__(self, kind, brand, weight, size, power, produced_year):
#         self.kind = kind
#         self.brand = brand
#         self.weight = weight
#         self.size = size
#         self.power = power
#         self.produced_year = produced_year
#
#     def work(self):
#         return f"{self.kind} yog'och va temir mahsulotlarini qirqish uchun qurilishda foydalaniladi!"
#
#
# object1 = Axe(1, "Yog'och va temir", 35, "AXE UZ", "Unlimited", "Very Safe")
# object2 = BuildingInstrument("Arra", "ARRA UZ", 200, "Middle", "Juda kuchli", 2019)
#
# print(object1.work())
# print(object2.work())

# ____________________________________________________________________________________________________

# 6 - topshiriq


# class StringUtils:
#
#     @staticmethod
#     def to_uppercase(string):
#         return string.upper()
#
#     @staticmethod
#     def to_lowercase(string):
#         return string.lower()
#
#     @staticmethod
#     def capitalize(string):
#         return string.capitalize()
#
#     @staticmethod
#     def reverse(string):
#         return string[::-1]
#
#
# print(StringUtils.to_uppercase("bu uppercase matn"))
# print(StringUtils.to_lowercase("BU LOWERCASE MATN"))
# print(StringUtils.capitalize("bu BOsh harfDA boshLANGAN MAtN"))
# print(StringUtils.reverse("bu teskari ogirilgan matn"))

# ____________________________________________________________________________________________________

# 7 - topshiriq


# class User:
#     list_users = []
#
#     @staticmethod
#     def add_user(name, age):
#         User.list_users.append({"Ism": name, "Yosh": age})
#
#     @staticmethod
#     def get_users():
#         return User.list_users
#
#     @staticmethod
#     def clear_users():
#         User.list_users.clear()
#         return "Foydalanuvchilar ro'yxati tozalandi!"
#
#     @staticmethod
#     def find_user(name):
#         for i in User.list_users:
#             if i["Ism"] == name:
#                 return i
#         return "Bunday ismli foydalanuvchi mavjud emas!"
#
#
# User.add_user("Sobir", 17)
# User.add_user("Toxir", 25)
# print(User.get_users())
# print(User.find_user('Toxir'))
# print(User.clear_users())
# print(User.get_users())
