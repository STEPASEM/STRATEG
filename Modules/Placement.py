from Modules.СhessBoard import ChessBoard


class Placement:
    def __init__(self, Board: ChessBoard, TypeFigure: int):
        self.Board = Board
        self.matrix_board = [row[:] for row in Board.GetBoard()]
        self.TypeFigure = TypeFigure

    def show_available_cells(self):
        """Проверяет наличие доступных клеток."""
        available_cells = []
        side = self.Board.LengthBoard()
        for i in range(side):
            for j in range(side):
                if self.matrix_board[i][j] == 0:
                    available_cells.append((i, j))
        return available_cells

    def place_figure(self):
        """Размещает фигуру на доске в выбранной пользователем клетке."""
        available_cells = self.show_available_cells()
        if not available_cells:
            print("Нет доступных клеток для размещения фигуры.")
            return False

        while True:
            try:
                print("Введите координаты клетки (строка и столбец через пробел): ", end="")
                row, col = map(int, input().split())
                if (row, col) in available_cells:
                    self.matrix_board[row][col] = self.TypeFigure
                    print(f"Фигура {self.TypeFigure} успешно размещена на клетке ({row}, {col}).")
                    self.Board.Board = self.matrix_board
                    self.Board.PrintBoard()
                    return self.Board
                else:
                    print("Выбранная клетка недоступна. Попробуйте снова.")
            except ValueError:
                print("Ошибка ввода. Введите два числа через пробел.")
            except IndexError:
                print("Ошибка: координаты выходят за пределы доски.")