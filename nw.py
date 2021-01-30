import numpy as np
from utils import BLOSUM62_aminoacids, BLOSUM62_penalties


def nw(sequence1, sequence2, match_reward=1, mismatch_penalty=-1, gap_penalty=-2):
    seq1_length = len(sequence1)
    seq2_length = len(sequence2)

    scoring_matrix = np.zeros((seq1_length + 1, seq2_length + 1))
    match_matrix = np.zeros((seq1_length, seq2_length))

    # Fills the matrix that helps checking for matches later on
    for i in range(seq1_length):
        for j in range(seq2_length):
            if sequence1[i] == sequence2[j]:
                aminoacid_position = BLOSUM62_aminoacids.index(sequence1[i])
                match_matrix[i][j] = BLOSUM62_penalties[aminoacid_position][aminoacid_position]
            else:
                match_matrix[i][j] = mismatch_penalty

    # Fills the scoring matrix
    for i in range(1, seq1_length + 1):
        for j in range(1, seq2_length + 1):
            score = (
                scoring_matrix[i - 1][j - 1] + match_matrix[i - 1][j - 1],
                scoring_matrix[i - 1][j] + gap_penalty,
                scoring_matrix[i][j - 1] + gap_penalty,
            )
            scoring_matrix[i][j] = max(score)

    print(scoring_matrix)
    print(BLOSUM62_aminoacids[3], BLOSUM62_penalties[3][3])