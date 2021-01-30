import utils
import nw
import sys

sequences = utils.readSequences(sys.argv[1])

print(sequences)

nw.nw(sequences[0], sequences[1])
