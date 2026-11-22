import sys

scores = list(map(int, sys.argv[1:]))

if len(scores) == 0:
    print("Please provide scores as command-line arguments.")
else:
    total = sum(scores)
    average = total / len(scores)

    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)