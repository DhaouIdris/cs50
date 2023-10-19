from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Biconditional(AKnave, Not(AKnight)),
    # A says "I am both a knight and a knave."
    Implication(And(AKnave, AKnight), AKnight),
    Implication(Not(And(AKnave, AKnight)), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    # A says "We are both knaves."
    Implication(And(AKnave,BKnave), AKnight),
    Implication(Not(And(AKnave,BKnave)), AKnave)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    # A says "We are the same kind."
    Biconditional(Or(And(AKnight, BKnight), And(AKnave, BKnave)), AKnight),
    # B says "We are of different kinds."
    Biconditional(Or(And(AKnight, BKnave), And(AKnave, BKnight)), BKnight),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(CKnave, Not(CKnight)),
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnave, AKnight))),
    # B says "A said 'I am a knave'."
    Implication(BKnave, Or(Not(AKnight), Or(AKnight, AKnave))),
    Implication(BKnight, Or(Not(AKnave), Not(Or(AKnave, AKnight)))),
    # B says "C is a knave."
    Implication(Not(CKnave), BKnave),
    # C says "A is a knight."
    Biconditional(AKnight, CKnight)
    
)

 #   Or(AKnight, AKnave),
  #  Or(BKnight, BKnave),
   # Or(CKnight, CKnave),
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
