# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Guns():
   def __init__(self, puli: object, ak47: object = 1) -> object:
      self.puli = puli
      self.ak47 = ak47

class Soldier(Guns):
   def __init__(self) -> object:
       super().__init__(puli, ak47)
       self.puli = puli
       self.ak47 = 47

class Act_of_Shooting(Soldier):
    def __init__(self):
        super().__init__()

    def shooting(self):
       def perezaryadka(self):
          self.puli = 100
       while self.puli > 0:
          self.puli -= 1
          print("тиги-тигитиш")
          if self.puli == 0:
              perezaryadka()
              print("Перезаряжает")


soldat1 = Act_of_Shooting()
soldat1.shooting()


# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

class Furniture():
   def __init__(self, spalnya = 4, garderob = 2, stol = 1.5):
      self.spalnya = spalnya
      self.garderob = garderob
      self.stol = stol

class Dom(Furniture):
   def __init__(self, type, ploshad):
      super().__init__(spalnya = 4, garderob = 2, stol = 1.5)
      self.type = type
      self.ploshad = ploshad

   def print_info(self):
      print(f"Тип дома: {self.type}, общая площадь: {self.ploshad}, оставшаяся площадь:", (self.ploshad-(self.spalnya + self.garderob + self.stol))," список названий мебели: спальня, стол, гардероб")

dom1 = Dom('частный', 135)
dom1.print_info()

# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Student:
    ENG = 'abcdefghijklmnopqrstvwxyz'
    ENG_UPPER = ENG.upper()

    def __init__(self, fio, old, subj):
        self.fio = fio
        self.old = old
        self.subj = subj

    @classmethod
    def check_old(cls, old):
        if type(old) != int or old < 17:
                raise TypeError('Возраст дб целым числом и от 17')
    @classmethod
    def check_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО дб только из букв')

        f = fio.split(' ')
        if len(f) != 2:
            raise TypeError('ФИО дб из 2х элементов')

        letter = cls.ENG + cls.ENG_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО дб больше чем 1 буква')
            if len(s.strip(letter)) != 0:
                raise TypeError('В ФИО дб исп буквы английскими')


    @classmethod
    def check_subj(cls, subj):
        if type(subj) != str:
            raise TypeError('специальность дб только из букв')
        ss = subj
        letter = cls.ENG + cls.ENG_UPPER
        for s in ss:
            if len(s) < 1:
                raise TypeError('В специальности дб больше чем 1 буква')
            if len(s.strip(letter)) != 0:
                raise TypeError('В ФИО дб исп буквы английскими')


    @property
    def fio(self):
        return self.__fio


    @fio.setter
    def fio(self, new_fio):
        self.__fio = new_fio


    @fio.deleter
    def fio(self):
        del self.__fio


    @property
    def old(self):
        return self.__old


    @old.setter
    def old(self, new_old):
        self.__old = new_old


    @old.deleter
    def old(self):
        del self.__old



steve = Student("Steven Schultz", 23, "English")

print(f"name: {steve.fio}, age: {steve.old}, major: {steve.subj}")
steve.fio = 'Steven Schultz'
steve.old = 23
steve.ps = 'English'


# # 4 
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3



# # 5  
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle


import random
from random import shuffle

class Card():
    def __init__(self, koloda = ['черви A','черви K','черви Q','черви J','черви 10','черви 9','черви 8','черви 7','черви 6','черви 5','черви 4','черви 3','черви 2', 'бубны A','бубны K','бубны Q','бубны J','бубны 10','бубны 9','бубны 8','бубны 7','бубны 6','бубны 5','бубны 4','бубны 3','бубны 2','трефы A','трефы K','трефы Q','трефы J','трефы 10','трефы 9','трефы 8','трефы 7','трефы 6','трефы 5','трефы 4','трефы 3','трефы 2','пики A','пики K','пики Q','пики J','пики 10','пики 9','пики 8','пики 7','пики 6','пики 5','пики 4','пики 3','пики 2']):
        self.koloda = koloda

class Deck(Card):
    def __init__(self):
        super().__init__(koloda = ['черви A','черви K','черви Q','черви J','черви 10','черви 9','черви 8','черви 7','черви 6','черви 5','черви 4','черви 3','черви 2', 'бубны A','бубны K','бубны Q','бубны J','бубны 10','бубны 9','бубны 8','бубны 7','бубны 6','бубны 5','бубны 4','бубны 3','бубны 2','трефы A','трефы K','трефы Q','трефы J','трефы 10','трефы 9','трефы 8','трефы 7','трефы 6','трефы 5','трефы 4','трефы 3','трефы 2','пики A','пики K','пики Q','пики J','пики 10','пики 9','пики 8','пики 7','пики 6','пики 5','пики 4','пики 3','пики 2'])

    def shuffle(self):
        if len(self.koloda) == 52:
            print("Смешиваю:", random.shuffle(self.koloda))
        else:
            print("В колоде не 52 карты")

    def razdacha(self):
        r = random.choice(self.koloda)
        print(r)
        self.koloda.remove(r)

c = Deck()
c.razdacha()
c.shuffle()



# # 6 
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название 
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv

