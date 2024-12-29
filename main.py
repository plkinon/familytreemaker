import argparse
from familytreemaker import Family

"""Entry point of the program when called as a script.

"""
# Parse command line options
parser = argparse.ArgumentParser(
    description="Generates a family tree graph from a simple text file"
)
parser.add_argument(
    "-a",
    dest="ancestor",
    help="make the family tree from an ancestor (if "
    + "omitted, the program will try to find an ancestor)",
)
parser.add_argument(
    "input", metavar="INPUTFILE", help="the formatted text file representing the family"
)
args = parser.parse_args()

# Create the family
family = Family()

# Populate the family
f = open(args.input, "r", encoding="utf-8")
family.populate(f)
f.close()

# Find the ancestor from whom the tree is built
if args.ancestor:
    ancestor = family.find_person(args.ancestor)
    if not ancestor:
        raise Exception('Cannot find person "' + args.ancestor + '"')
else:
    ancestor = family.find_first_ancestor()

# Output the graph descriptor, in DOT format
family.output_descending_tree(ancestor)
