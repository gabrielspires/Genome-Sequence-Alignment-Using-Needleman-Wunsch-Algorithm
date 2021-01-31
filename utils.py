import numpy as np

BLOSUM62_aminoacids = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "Q",
    "E",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
    "B",
    "Z",
    "X",
    "*",
]
BLOSUM62_penalties = np.loadtxt("BLOSUM62.txt", dtype="i", delimiter=" ")


def printScoringMatrix(sequence1, sequence2, scoring_matrix):
    sequence1 = "w" + sequence1
    sequence2 = "v" + sequence2

    print("", end="")
    for aminoacid in sequence1:
        print(aminoacid.rjust(4), end="")
    print()

    for i in range(len(scoring_matrix)):
        print(sequence2[i], end="")
        for j in range(len(scoring_matrix[i])):
            print(str(int(scoring_matrix[i][j])).rjust(3), end=" ")
        print()


def readSequences(input_file):
    sequences = []
    with open(input_file) as sequence_file:
        sequence_number = -1
        for line in sequence_file:
            if line[0] == ">":
                sequence_number += 1
                sequences.append("")
            else:
                if line[-1] == "\n":
                    line = line[:-1]
                sequences[sequence_number] += "".join(line)

    return sequences
