import numpy as np
from utils import BLOSUM62_aminoacids, BLOSUM62_penalties


def nw(sequence1, sequence2, gap_penalty=0):
    seq1_length = len(sequence1)
    seq2_length = len(sequence2)

    scoring_matrix = np.zeros((seq2_length + 1, seq1_length + 1))
    match_matrix = np.zeros((seq2_length, seq1_length))
    direction_matrix = [["" for _ in range(seq1_length + 1)] for _ in range(seq2_length + 1)]

    # Initialize the scoring matrix using the gap penalty
    for i in range(seq2_length + 1):
        scoring_matrix[i][0] = i * gap_penalty
    for j in range(seq1_length + 1):
        scoring_matrix[0][j] = j * gap_penalty

    # Fills the matrix that helps checking for matches later on using the BLOSUM62 matrix
    for i in range(seq2_length):
        for j in range(seq1_length):
            # Match
            if sequence2[i] == sequence1[j]:
                aminoacid_position = BLOSUM62_aminoacids.index(sequence2[i])
                match_matrix[i][j] = BLOSUM62_penalties[aminoacid_position][aminoacid_position]
            # Mismatch
            else:
                aminoacid_1 = BLOSUM62_aminoacids.index(sequence2[i])
                aminoacid_2 = BLOSUM62_aminoacids.index(sequence1[j])
                match_matrix[i][j] = BLOSUM62_penalties[aminoacid_1][aminoacid_2]

    # Fills the scoring matrix
    for i in range(1, seq2_length + 1):
        for j in range(1, seq1_length + 1):
            score = (
                scoring_matrix[i - 1][j - 1] + match_matrix[i - 1][j - 1],
                scoring_matrix[i - 1][j] + gap_penalty,
                scoring_matrix[i][j - 1] + gap_penalty,
            )
            scoring_matrix[i][j] = max(score)

    # Fills the direction matrix
    for i in range(1, seq2_length + 1):
        for j in range(1, seq1_length + 1):
            if (
                sequence2[i - 1]
                == sequence1[j - 1]
                # or scoring_matrix[i - 1][j - 1] >= scoring_matrix[i - 1][j]
                # and scoring_matrix[i - 1][j - 1] >= scoring_matrix[i][j - 1]
            ):
                direction_matrix[i][j] = "\\"
            elif scoring_matrix[i - 1][j] > scoring_matrix[i][j - 1]:
                direction_matrix[i][j] = "|"
            else:
                direction_matrix[i][j] = "_"

    # Traceback
    # TODO: Verificar porque a sequencia está diferente do esperado (visto no PDF do TP)
    aligned_sequence_1 = ""
    aligned_sequence_2 = ""

    seq1_characters_left = seq1_length
    seq2_characters_left = seq2_length

    while seq1_characters_left > 0 and seq2_characters_left > 0:
        # Diagonal
        if (
            scoring_matrix[seq2_characters_left][seq1_characters_left]
            == scoring_matrix[seq2_characters_left - 1][seq1_characters_left - 1]
            + match_matrix[seq2_characters_left - 1][seq1_characters_left - 1]
        ):
            aligned_sequence_2 = sequence2[seq2_characters_left - 1] + aligned_sequence_2
            aligned_sequence_1 = sequence1[seq1_characters_left - 1] + aligned_sequence_1

            seq1_characters_left -= 1
            seq2_characters_left -= 1
        # Vertical
        elif (
            scoring_matrix[seq2_characters_left][seq1_characters_left]
            == scoring_matrix[seq2_characters_left - 1][seq1_characters_left] + gap_penalty
        ):
            aligned_sequence_2 = sequence2[seq2_characters_left - 1] + aligned_sequence_2
            aligned_sequence_1 = "-" + aligned_sequence_1

            seq2_characters_left -= 1
        # Horizontal
        else:
            aligned_sequence_2 = "-" + aligned_sequence_2
            aligned_sequence_1 = sequence1[seq1_characters_left - 1] + aligned_sequence_1

            seq1_characters_left -= 1

    # Creates the matrix with the scores and directions
    complete_matrix = [["" for _ in range(seq1_length + 1)] for _ in range(seq2_length + 1)]
    for i in range(len(complete_matrix)):
        for j in range(len(complete_matrix[i])):
            if i == 0 and j == 0:
                complete_matrix[i][j] = "0"
            else:
                complete_matrix[i][j] = str(int(scoring_matrix[i][j])) + direction_matrix[i][j]

    sequence1 = "w" + sequence1
    sequence2 = "v" + sequence2
    print(" ", end="")
    for aminoacid in sequence1:
        print(aminoacid.rjust(4), end="")
    print()
    for i in range(len(complete_matrix)):
        print(sequence2[i], end="")
        for j in range(len(complete_matrix[i])):
            print(complete_matrix[i][j].rjust(4), end="")
        print()

    print(aligned_sequence_1)
    print(aligned_sequence_2)

    return scoring_matrix
