from Modules.Movement import Movement
from Modules.СhessBoard import ChessBoard
from Modules.Placement import Placement

PRICE_FIGURE =[2, 5, 5, 7, 10]

Hello_massage = ('''=====Добро пожаловать в Игру стратег!=====


===============Правила игры===============
Для начала вам необходимо выбрать режим поля, который вы хотите.
Далее вам надо выбрать количество игровых клеток.
Вы также можете покупать фигуры за определенную стоимость.
Первый игрок ставит фигуры в верхней части, а второй в нижней.

Зеленый - первый игрок
Синий - второй игрок

Выберите тип поля и кол-во клеточек [квадрат(0) ромб(1)]
Пример (0 25)
: ''')

Store_massage = (f'''========Магазин========

Меню
1. Пешка - 2 балла
2. Слон - 5 баллов
3. Конь - 5 баллов
4. Ладья - 7 баллов
5. Ферзь - 10 баллов

0. Выход из Магазина
''')"\033[34m"

class Menu:
    def __init__(self):
        self.Board = None
        self.players_current = {0: "\033[32m", 1: }
        self.POINTS_USERS = [25, 25]
        self.players_figure = [[],[]]

    def Start(self):
        """Запуск игры"""
        print(Hello_massage, end='')
        TypeBoard, SizeBoard = map(int, input().split())
        self.Board = self.ChoiceBoard(TypeBoard, SizeBoard)
        self.Store(0)
        self.Store(1)
        self.PlayGame()


    def ChoiceBoard(self, TypeBoard: int, SizeBoard: int) -> list:
        """Создание доски"""
        Board = ChessBoard(TypeBoard, SizeBoard, self.players_figure)
        Board.PrintBoard()
        return Board

    def Store(self, i: int):
        """Вывод магазина для покупки фигур"""
        print(f'{self.players_current[i]}Покупает игрок {i+1}\033[0m \n')
        while True:
            print(Store_massage)
            print(f'Баланс очков: {self.POINTS_USERS[i]}\nНапишите номер фигуры которую хотите купить\n: ', end='')
            type_figure = int(input())
            if PRICE_FIGURE[type_figure - 1] > self.POINTS_USERS[i] and (6 > type_figure > 0):
                print('\nНедостаточно очков\n')
            else:
                match type_figure:
                    case 1:
                        self.POINTS_USERS[i] -= PRICE_FIGURE[0]
                    case 2:
                        self.POINTS_USERS[i] -= PRICE_FIGURE[1]
                    case 3:
                        self.POINTS_USERS[i] -= PRICE_FIGURE[2]
                    case 4:
                        self.POINTS_USERS[i] -= PRICE_FIGURE[3]
                    case 5:
                        self.POINTS_USERS[i] -= PRICE_FIGURE[4]
                    case 0:
                        break
                    case _:
                        print('\nФигура введена неверно\n')
                self.Board = Placement(self.Board, self.players_figure, type_figure, i).place_figure()

    def PlayGame(self):
        """Запуск ходьбы"""
        Movement(self.Board, self.players_figure, self.POINTS_USERS, PRICE_FIGURE, 0).MoveFigure()
        Movement(self.Board, self.players_figure, self.POINTS_USERS, PRICE_FIGURE, 1).MoveFigure()
        while True:
            for i in range(2):
                if self.POINTS_USERS[i] >= 2:
                    self.Store(i)
                while not Movement(self.Board, self.players_figure, self.POINTS_USERS, PRICE_FIGURE, i).MoveFigure():
                    if self.POINTS_USERS[i] < 2:
                        print(f'У вас нет денег!\n{self.players_current[i]}Игрок {i+1} проиграл!\033[0m')
                        return True
                    self.Store(i)