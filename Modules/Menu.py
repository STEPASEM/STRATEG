from Modules.СhessBoard import ChessBoard

PRICE_FIGURE =[2, 5, 5, 7, 10]

Hello_massage = ('''=====Добро пожаловать в Игру стратег!=====


===============Правила игры===============
Для начала вам необходимо выбрать режим поля, в котором вы хотите.
Далее вам надо выбрать количество игровых клеток(должен быть квадрат какого то числа) 
Вы также можете покупать фигуры за определенную стоимость

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
''')

class Menu:
    def __init__(self):
        pass

    def Hello(self):
        """Пишет приветствие"""
        print(Hello_massage, end='')
        TypeBoard, SizeBoard = map(int, input().split())
        Board = self.ChoiceBoard(TypeBoard, SizeBoard)
        self.Store()


    def ChoiceBoard(self, TypeBoard: int, SizeBoard: int) -> list:
        """Создание доски"""
        Board = ChessBoard(TypeBoard, SizeBoard)
        Board.PrintBoard()
        return Board

    def Store(self):
        """Вывод магазина для покупки фигур"""
        POINTS = 25
        while True:
            print(Store_massage)
            print(f'Баланс очков: {POINTS}\nНапишите номер фигуры которую хотите купить\n: ', end='')
            match int(input()):
                case 1:
                    POINTS -= PRICE_FIGURE[0]
                case 2:
                    POINTS -= PRICE_FIGURE[1]
                case 3:
                    POINTS -= PRICE_FIGURE[2]
                case 4:
                    POINTS -= PRICE_FIGURE[3]
                case 5:
                    POINTS -= PRICE_FIGURE[4]
                case 0:
                    break
                case _:
                    print('\nНедостаточно очков или фигура введена неверно\n')

Menu().Hello()