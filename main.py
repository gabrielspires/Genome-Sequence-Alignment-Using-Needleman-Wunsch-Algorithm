import utils
import nw
import sys

sequences = utils.readSequences(sys.argv[1])

nw.nw(sequences[0], sequences[1])

# Run with 'python3 main.py Sequences/input3'
# Checking correctness with gtuckerkellogg.github.io/pairwise/demo/