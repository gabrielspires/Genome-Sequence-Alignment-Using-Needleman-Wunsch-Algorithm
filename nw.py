import numpy as np
from utils import BLOSUM62_aminoacids, BLOSUM62_penalties


class nw(object):
    def __init__(self, sequence1, sequence2, gap_penalty=0):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.gap_penalty = gap_penalty
        self.aligned_sequence_1 = ""
        self.aligned_sequence_2 = ""

        self.seq1_length = len(self.sequence1)
        self.seq2_length = len(self.sequence2)

        self.scoring_matrix = np.zeros((self.seq2_length + 1, self.seq1_length + 1))
        self.match_matrix = np.zeros((self.seq2_length, self.seq1_length))
        self.direction_matrix = [
            ["" for _ in range(self.seq1_length + 1)] for _ in range(self.seq2_length + 1)
        ]
        self.complete_matrix = [
            ["" for _ in range(self.seq1_length + 1)] for _ in range(self.seq2_length + 1)
        ]

        self.initializeScoringMatrix()
        self.fillMatchMatrix()
        self.fillScoringMatrix()
        self.fillDirectionMatrix()
        self.createCompleteMatrix()
        self.Traceback()
        self.printCompleteMatrix()

        print(self.aligned_sequence_1)
        print(self.aligned_sequence_2)

    def initializeScoringMatrix(self):
        # Initialize the scoring matrix using the gap penalty
        for i in range(self.seq2_length + 1):
            self.scoring_matrix[i][0] = i * self.gap_penalty
        for j in range(self.seq1_length + 1):
            self.scoring_matrix[0][j] = j * self.gap_penalty

    def fillMatchMatrix(self):
        # Fills the matrix that helps checking for matches later on using the BLOSUM62 matrix
        for i in range(self.seq2_length):
            for j in range(self.seq1_length):
                # Match
                if self.sequence2[i] == self.sequence1[j]:
                    aminoacid_position = BLOSUM62_aminoacids.index(self.sequence2[i])
                    self.match_matrix[i][j] = BLOSUM62_penalties[aminoacid_position][
                        aminoacid_position
                    ]
                # Mismatch
                else:
                    aminoacid_1 = BLOSUM62_aminoacids.index(self.sequence2[i])
                    aminoacid_2 = BLOSUM62_aminoacids.index(self.sequence1[j])
                    self.match_matrix[i][j] = BLOSUM62_penalties[aminoacid_1][aminoacid_2]

    def fillScoringMatrix(self):
        # Fills the scoring matrix
        for i in range(1, self.seq2_length + 1):
            for j in range(1, self.seq1_length + 1):
                score = (
                    self.scoring_matrix[i - 1][j - 1] + self.match_matrix[i - 1][j - 1],
                    self.scoring_matrix[i - 1][j] + self.gap_penalty,
                    self.scoring_matrix[i][j - 1] + self.gap_penalty,
                )
                self.scoring_matrix[i][j] = max(score)

    def fillDirectionMatrix(self):
        # Fills the direction matrix
        for i in range(1, self.seq2_length + 1):
            for j in range(1, self.seq1_length + 1):
                if (
                    self.sequence2[i - 1]
                    == self.sequence1[j - 1]
                    # or self.scoring_matrix[i - 1][j - 1] >= self.scoring_matrix[i - 1][j]
                    # and self.scoring_matrix[i - 1][j - 1] >= self.scoring_matrix[i][j - 1]
                ):
                    self.direction_matrix[i][j] = "\\"
                elif self.scoring_matrix[i - 1][j] > self.scoring_matrix[i][j - 1]:
                    self.direction_matrix[i][j] = "|"
                else:
                    self.direction_matrix[i][j] = "_"

    def Traceback(self):
        i = self.seq2_length
        j = self.seq1_length

        while i > 0 and j > 0:
            if self.complete_matrix[i][j][-1] == "\\":
                # Diagonal
                i -= 1
                j -= 1
                self.aligned_sequence_1 = self.sequence1[j] + self.aligned_sequence_1
                self.aligned_sequence_2 = self.sequence2[i] + self.aligned_sequence_2
            elif self.complete_matrix[i][j][-1] == "_":
                # Horizontal
                j -= 1
                self.aligned_sequence_1 = self.sequence1[j] + self.aligned_sequence_1
                self.aligned_sequence_2 = "-" + self.aligned_sequence_2
            elif self.complete_matrix[i][j][-1] == "|":
                # Vertical
                i -= 1
                self.aligned_sequence_1 = "-" + self.aligned_sequence_1
                self.aligned_sequence_2 = self.sequence2[i] + self.aligned_sequence_2

    def createCompleteMatrix(self):
        # Creates the matrix with the scores and directions
        for i in range(len(self.complete_matrix)):
            for j in range(len(self.complete_matrix[i])):
                if i == 0 and j == 0:
                    self.complete_matrix[i][j] = "0"
                else:
                    self.complete_matrix[i][j] = (
                        str(int(self.scoring_matrix[i][j])) + self.direction_matrix[i][j]
                    )

    def printCompleteMatrix(self):
        self.sequence1_ = "w" + self.sequence1
        self.sequence2_ = "v" + self.sequence2
        print(" ", end="")
        for aminoacid in self.sequence1_:
            print(aminoacid.rjust(4), end="")
        print()
        for i in range(len(self.complete_matrix)):
            print(self.sequence2_[i], end="")
            for j in range(len(self.complete_matrix[i])):
                print(self.complete_matrix[i][j].rjust(4), end="")
            print()
