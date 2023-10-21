from statistics import mean

def main():
    firstSequence = int(input("First Sequence: "))
    secondSequence = int(input("Second Sequence: "))
    sequences = int(input("Sequences: ")) + 1

    fibonacciSequence(firstSequence, secondSequence, sequences)


def fibonacciSequence(num1, num2, num3=10):
    sequence = [num1, num2]
    ratio = []

    for fibonacci in range(num3):
        sequence.append(sequence[-1] + sequence[-2])

        for _ in range(2, fibonacci): 
            ratio.append(sequence[-1] / sequence[-2])

    goldenRatio = mean(ratio)

    print(f"Fibonacci Sequence: {str(sequence)[1:-1]}")
    print(f"Golden Ratio: {goldenRatio:.5f}")

main()
