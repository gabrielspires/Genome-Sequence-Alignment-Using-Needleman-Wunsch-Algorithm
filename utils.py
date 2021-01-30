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
