import numpy as np
from utils import BLOSUM62_aminoacids, BLOSUM62_penalties


def nw(sequence1, sequence2, gap_penalty=-4):
    seq1_length = len(sequence1)
    seq2_length = len(sequence2)

    scoring_matrix = np.zeros((seq2_length + 1, seq1_length + 1))
    match_matrix = np.zeros((seq2_length, seq1_length))

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

    # Traceback
    # TODO

    return scoring_matrix
