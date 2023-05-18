class BoardSquare:
    def __init__(self, column, row, piece = None):
        self.column = column
        self.row = row
        self.piece = piece

    def setPiece(self, x):
        self.piece = x

    def __str__(self):
        return (self.column + str(self.row) + ":" + str(self.piece))
    __repr__=__str__


class Board:
    def __init__(self):
        self.content = []
        for x in range(8):
            column = []
            for y in range(8):
                s = BoardSquare(chr(y+97), x+1)
                column.append(s)
            self.content.append(column)

    def startBoard(self):
        self.placePiece("a1", Piece("wrl"))
        self.placePiece("b1", Piece("wkl"))
        self.placePiece("c1", Piece("wbl"))
        self.placePiece("d1", Piece("wq"))
        self.placePiece("e1", Piece("wk"))
        self.placePiece("f1", Piece("wbr"))
        self.placePiece("g1", Piece("wkr"))
        self.placePiece("h1", Piece("wrr"))
        self.placePiece("a2", Piece("wpa"))
        self.placePiece("b2", Piece("wpb"))
        self.placePiece("c2", Piece("wpc"))
        self.placePiece("d2", Piece("wpd"))
        self.placePiece("e2", Piece("wpe"))
        self.placePiece("f2", Piece("wpf"))
        self.placePiece("g2", Piece("wpg"))
        self.placePiece("h2", Piece("wph"))

        self.placePiece("a7", Piece("bpa"))
        self.placePiece("b7", Piece("bpb"))
        self.placePiece("c7", Piece("bpc"))
        self.placePiece("d7", Piece("bpd"))
        self.placePiece("e7", Piece("bpe"))
        self.placePiece("f7", Piece("bpf"))
        self.placePiece("g7", Piece("bpg"))
        self.placePiece("h7", Piece("bph"))
        self.placePiece("a8", Piece("brl"))
        self.placePiece("b8", Piece("bkl"))
        self.placePiece("c8", Piece("bbl"))
        self.placePiece("d8", Piece("bq"))
        self.placePiece("e8", Piece("bk"))
        self.placePiece("f8", Piece("bbr"))
        self.placePiece("g8", Piece("bkr"))
        self.placePiece("h8", Piece("brr"))

    def placePiece(self, location, piece):
        square = self.content[int(location[1])-1][ord(location[0])-97]
        piece.setLocation(square)
        square.setPiece(piece)
        

    def __str__(self):
        x = ""
        for column in self.content[::-1]:
            x += (str(column)+"\n")
        return (x)

    __repr__=__str__

class Piece:
    def __init__(self, name):
        self.name = name
        self.locationSquare = None

    def setLocation(self, bs):
        self.locationSquare = bs

    def __str__(self):
        return (self.name)

    __repr__=__str__


if __name__=='__main__':
    x = Board()
    x.startBoard()
    print(x)
