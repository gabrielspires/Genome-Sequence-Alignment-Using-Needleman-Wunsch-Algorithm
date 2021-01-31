import utils
import nw
import sys

sequences = utils.readSequences(sys.argv[1])

scoring_matrix = nw.nw(sequences[0], sequences[1])

utils.printScoringMatrix(sequences[0], sequences[1], scoring_matrix)


# Run with 'python3 main.py Sequences/input1'
# Checking correctness with gtuckerkellogg.github.io/pairwise/demo/