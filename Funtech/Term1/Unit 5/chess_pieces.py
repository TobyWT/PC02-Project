class ChessPiece:
    def __init__(self, syb: str, colour: str, r: int, c: int):
        self.symbol = syb
        self.colour = colour
        self._position = Position(r, c)  # protected

    def get_row(self):
        return self._position.row

    def get_column(self):
        return self._position.column


class Pawn(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "P", col, r, c)


class Rook(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "R", col, r, c)


class Knight(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "K", col, r, c)


class Bishop(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "B", col, r, c)


class Queen(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "Q", col, r, c)


class King(ChessPiece):
    def __init__(self, col: str, r: int, c: int):
        ChessPiece.__init__(self, "C", col, r, c)


class Position:
    def __init__(self, r: int, c: int):
        self.__row = r
        self.__column = c

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def set_row(self, r):
        if 0 <= r <= 7:
            self.__row = r

    def set_column(self, c):
        if 0 <= c <= 7:
            self.__column = c
