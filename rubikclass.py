from numpy.random import choice

SOLVED_COLOURS = {"B": 0, "D": 1, "L": 2, "F": 3, "U": 4, "R": 5}


class cube2():
    def __init__(self):
        self.puzzleType = "2x2x2 Rubik's cube"
        # For each face, list colours in reading order when looking at the face directly
        # This works out to the following corner assignments:

        # BDL=B[3],D[2],L[2]
        # FDL=F[2],D[0],L[3]
        # BDR=B[2],D[3],R[3]
        # FDR=F[3],D[1],R[2]
        # BUL=B[1],U[0],L[0]
        # FUL=F[0],U[2],L[1]
        # BUR=B[0],U[1],R[1]
        # FUR=F[1],U[3],R[0]

        self.faces = {face: [SOLVED_COLOURS[face]] * 4 for face in SOLVED_COLOURS}

        # hold BDL in space
        # self.actions=["R","R\'","R2","U","U\'","U2","F","F\'","F2"]
        self.actions = ["R", "U", "F"]

    def reset(self):
        self.faces = {face: [SOLVED_COLOURS[face]] * 4 for face in SOLVED_COLOURS}

    def RTurn(self):
        spare = self.faces["R"][0]
        self.faces["R"][0] = self.faces["R"][2]
        self.faces["R"][2] = self.faces["R"][3]
        self.faces["R"][3] = self.faces["R"][1]
        self.faces["R"][1] = spare
        spare = self.faces["F"][1]
        self.faces["F"][1] = self.faces["D"][1]
        self.faces["D"][1] = self.faces["B"][2]
        self.faces["B"][2] = self.faces["U"][1]
        self.faces["U"][1] = spare
        spare = self.faces["F"][3]
        self.faces["F"][3] = self.faces["D"][3]
        self.faces["D"][3] = self.faces["B"][0]
        self.faces["B"][0] = self.faces["U"][3]
        self.faces["U"][3] = spare

    def R(self, amount):
        for _ in range(amount):
            self.RTurn()

    def UTurn(self):
        spare = self.faces["U"][0]
        self.faces["U"][0] = self.faces["U"][2]
        self.faces["U"][2] = self.faces["U"][3]
        self.faces["U"][3] = self.faces["U"][1]
        self.faces["U"][1] = spare
        spare = self.faces["F"][1]
        self.faces["F"][1] = self.faces["R"][1]
        self.faces["R"][1] = self.faces["B"][1]
        self.faces["B"][1] = self.faces["L"][1]
        self.faces["L"][1] = spare
        spare = self.faces["F"][0]
        self.faces["F"][0] = self.faces["R"][0]
        self.faces["R"][0] = self.faces["B"][0]
        self.faces["B"][0] = self.faces["L"][0]
        self.faces["L"][0] = spare

    def U(self, amount):
        for _ in range(amount):
            self.UTurn()

    def FTurn(self):
        spare = self.faces["F"][0]
        self.faces["F"][0] = self.faces["F"][2]
        self.faces["F"][2] = self.faces["F"][3]
        self.faces["F"][3] = self.faces["F"][1]
        self.faces["F"][1] = spare
        spare = self.faces["U"][2]
        self.faces["U"][2] = self.faces["L"][3]
        self.faces["L"][3] = self.faces["D"][1]
        self.faces["D"][1] = self.faces["R"][0]
        self.faces["R"][0] = spare
        spare = self.faces["U"][3]
        self.faces["U"][3] = self.faces["L"][1]
        self.faces["L"][1] = self.faces["D"][0]
        self.faces["D"][0] = self.faces["R"][2]
        self.faces["R"][2] = spare

    def F(self, amount):
        for _ in range(amount):
            self.FTurn()

    def singleMove(self, action, amount):
        if action == "R":
            self.R(amount)
        elif action == "U":
            self.U(amount)
        elif action == "F":
            self.F(amount)
        else:
            print("FATAL")

    def scramble(self, length: int = 0, scrambleSequence=None):
        if scrambleSequence is not None:
            for move, amount in scrambleSequence:
                self.singleMove(move, amount)
        else:
            sequence = choice(self.actions, size=length)
            amounts = choice([1, 2, 3], size=length)
            print(list(zip(sequence, amounts)))
            for move, amount in zip(sequence, amounts):
                self.singleMove(move, amount)

    def nonTrivialScramble(self, length=0):
        previousMove = None
        numMoves = 0
        while numMoves < length:
            candidateAction = choice(self.actions)
            if candidateAction != previousMove:
                previousMove = candidateAction
                amount = choice([1, 2, 3])
                print(candidateAction, amount)
                self.singleMove(candidateAction, amount)
                numMoves = numMoves + 1

    def displayCubeState(self):
        print("F: ", self.faces["F"][0], self.faces["F"][1], self.faces["F"][2], self.faces["F"][3])
        print("U: ", self.faces["U"][0], self.faces["U"][1], self.faces["U"][2], self.faces["U"][3])
        print("R: ", self.faces["R"][0], self.faces["R"][1], self.faces["R"][2], self.faces["R"][3])
        print("B: ", self.faces["B"][0], self.faces["B"][1], self.faces["B"][2], self.faces["B"][3])
        print("D: ", self.faces["D"][0], self.faces["D"][1], self.faces["D"][2], self.faces["D"][3])
        print("L: ", self.faces["L"][0], self.faces["L"][1], self.faces["L"][2], self.faces["L"][3])

    def solvedFace(self, face: str) -> bool:
        """

        :type face: str
        """
        return self.faces[face] == [SOLVED_COLOURS[face]] * 4

    @property
    def solvedCube(self):
        for face in SOLVED_COLOURS:
            if not self.solvedFace(face):
                return False
        return True
