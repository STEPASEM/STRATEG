from Modules.СhessBoard import ChessBoard

class Movement:
    def __init__(self, Board: ChessBoard, players_figures: list[list[tuple]], POINTS_USERS: list[int],
                 PRICE_FIGURE: list[int], current_player: int):
        self.Board = Board
        self.matrix_board = [row[:] for row in Board.GetBoard()]
        self.players_figures = players_figures
        self.POINTS_USERS = POINTS_USERS
        self.PRICE_FIGURE = PRICE_FIGURE
        self.current_player = current_player
        self.opponent_player = 1 - current_player
        self.player_colors = {0: "\033[32m", 1: "\033[34m"}  # Зеленый для игрока 0, синий для игрока 1

    def is_valid_move(self, start: tuple, end: tuple) -> bool:
        """Проверяет, является ли ход допустимым для выбранной фигуры."""
        start_row, start_col = start
        end_row, end_col = end
        figure_type = self.matrix_board[start_row][start_col]

        # Проверка, что начальная клетка содержит фигуру текущего игрока
        if (start_row, start_col) not in self.players_figures[self.current_player]:
            print(f"{self.player_colors[self.current_player]}Вы не можете перемещать фигуры противника!\033[0m")
            return False

        # Проверка, что конечная клетка не занята фигурой текущего игрока
        if (end_row, end_col) in self.players_figures[self.current_player]:
            print("Вы не можете перемещать фигуру на клетку, занятую вашей же фигурой!")
            return False

        # Правила перемещения для каждой фигуры (аналогично шахматам)
        if figure_type == 1:  # Пешка
            direction = 1 if self.current_player == 0 else -1
            if start_col == end_col and self.matrix_board[end_row][end_col] == 0:
                if end_row == start_row + direction:
                    return True
                if ((start_row == 1 and self.current_player == 0) or 
                    (start_row == len(self.matrix_board) - 2 and self.current_player == 1)):
                    if end_row == start_row + 2 * direction and self.matrix_board[start_row + direction][start_col] == 0:
                        return True
            elif abs(end_col - start_col) == 1 and end_row == start_row + direction:
                if (end_row, end_col) in self.players_figures[self.opponent_player]:
                    return True
            return False

        elif figure_type == 2:  # Слон
            if abs(end_row - start_row) == abs(end_col - start_col):
                step_row = 1 if end_row > start_row else -1
                step_col = 1 if end_col > start_col else -1
                row, col = start_row + step_row, start_col + step_col
                while row != end_row and col != end_col:
                    if self.matrix_board[row][col] != 0 and self.matrix_board[row][col] != 9:
                        return False
                    row += step_row
                    col += step_col
                return True
            return False

        elif figure_type == 3:  # Конь
            return (abs(end_row - start_row) == 2 and abs(end_col - start_col) == 1) or \
                   (abs(end_row - start_row) == 1 and abs(end_col - start_col) == 2)

        elif figure_type == 4:  # Ладья
            if start_row == end_row:
                step = 1 if end_col > start_col else -1
                for col in range(start_col + step, end_col, step):
                    if self.matrix_board[start_row][col] != 0 and self.matrix_board[start_row][col] != 9:
                        return False
                return True
            elif start_col == end_col:
                step = 1 if end_row > start_row else -1
                for row in range(start_row + step, end_row, step):
                    if self.matrix_board[row][start_col] != 0 and self.matrix_board[row][start_col] != 9:
                        return False
                return True
            return False

        elif figure_type == 5:  # Ферзь
            if start_row == end_row or start_col == end_col:
                # Как ладья
                if start_row == end_row:
                    step = 1 if end_col > start_col else -1
                    for col in range(start_col + step, end_col, step):
                        if self.matrix_board[start_row][col] != 0 and self.matrix_board[start_row][col] != 9:
                            return False
                    return True
                elif start_col == end_col:
                    step = 1 if end_row > start_row else -1
                    for row in range(start_row + step, end_row, step):
                        if self.matrix_board[row][start_col] != 0 and self.matrix_board[row][start_col] != 9:
                            return False
                    return True
            elif abs(end_row - start_row) == abs(end_col - start_col):
                # Как слон
                step_row = 1 if end_row > start_row else -1
                step_col = 1 if end_col > start_col else -1
                row, col = start_row + step_row, start_col + step_col
                while row != end_row and col != end_col:
                    if self.matrix_board[row][col] != 0 and self.matrix_board[row][col] != 9:
                        return False
                    row += step_row
                    col += step_col
                return True
            return False

        return False

    def MoveFigure(self):
        """Перемещает фигуру на доске в выбранную клетку."""
        print(f"{self.player_colors[self.current_player]}Ход игрока {self.current_player + 1}\033[0m")
        self.Board.PrintBoard()

        if len(self.players_figures[self.current_player]) == 0:
            print(f"{self.player_colors[self.current_player]}У вас нет фигур!\033[0m")
            return False

        while True:
            try:
                print("Введите координаты фигуры, которую хотите переместить (строка и столбец через пробел): ", end="")
                start_row, start_col = map(int, input().split())
                
                # Проверка принадлежности фигуры
                if (start_row, start_col) not in self.players_figures[self.current_player]:
                    print(f"{self.player_colors[self.current_player]}Вы выбрали неправильную фигуру! Попробуйте снова.\033[0m")
                    continue

                print("Введите координаты клетки, куда хотите переместить фигуру (строка и столбец через пробел): ", end="")
                end_row, end_col = map(int, input().split())

                if not self.is_valid_move((start_row, start_col), (end_row, end_col)):
                    print("Недопустимый ход. Попробуйте снова.")
                    continue

                # Удаление фигуры противника, если она есть на конечной клетке
                if (end_row, end_col) in self.players_figures[self.opponent_player]:
                    self.players_figures[self.opponent_player].remove((end_row, end_col))
                    self.POINTS_USERS[self.current_player] += self.PRICE_FIGURE[self.matrix_board[end_row][end_col] - 1]
                    print(f"{self.player_colors[self.current_player]}Фигура противника захвачена!\033[0m")

                # Обновление позиции фигуры текущего игрока
                self.players_figures[self.current_player].remove((start_row, start_col))
                self.players_figures[self.current_player].append((end_row, end_col))

                # Обновление доски
                figure_type = self.matrix_board[start_row][start_col]
                self.matrix_board[start_row][start_col] = 0
                self.matrix_board[end_row][end_col] = figure_type
                self.Board.Board = self.matrix_board

                print(f"{self.player_colors[self.current_player]}Ход успешно выполнен.\033[0m")
                self.Board.PrintBoard()
                return True

            except ValueError:
                print("Ошибка ввода. Введите два числа через пробел.")
            except IndexError:
                print("Ошибка: координаты выходят за пределы доски.")