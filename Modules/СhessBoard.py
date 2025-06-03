from math import sqrt

class ChessBoard:
    def __init__(self, TypeBoard: int, SizeBoard: int):
        self.TypeBoard = TypeBoard # 0 - прямоугольник, 1 - ромб
        self.SizeBoard = SizeBoard # Кол-во клеточек (обязательно из числа
                                   # должен извлекаться ровный квадратный корень)
        self.Board = self.CreateBoard()


    def CreateBoard(self) -> list:
        """Создание доски"""
        Board = [[0 for _ in range(int(sqrt(self.SizeBoard)))] for _ in range(int(sqrt(self.SizeBoard)))]

        if self.TypeBoard == 1:  # Если ромб
            side = len(Board)
            if side % 2 == 0:
                center = (side - 1) / 2
                radius = center

                for i in range(side):
                    for j in range(side):
                        if abs(i - center) + abs(j - center) > radius + 0.5:
                            Board[i][j] = 9

            else:
                center = (side - 1) // 2
                radius = center + 1

                for i in range(side):
                    for j in range(side):
                        if abs(i - center) + abs(j - center) > radius:
                            Board[i][j] = 9

        return Board

    def LengthBoard(self) -> int:
        """Возвращает длину доски"""
        return len(self.Board)

    def GetBoard(self) -> list[list[int]]:
        """Возвращает доску"""
        return self.Board

    def PrintBoard(self):
        """Печать доски"""
        print('  \033[1m', ' '.join(map(str, range(len(self.Board)))), '\033[0m')
        for i in range(len(self.Board)):
            print('\033[1m', i, " ".join(map(str, self.Board[i])), '\033[0m')
        print()