import sys


def get_grade(marks):
    """Return a letter grade for marks out of 100."""
    if marks >= 90:
        return "A"
    elif marks >= 78:
        return "B"
    elif marks >= 65:
        return "C"
    elif marks >= 45:
        return "D"
    return "F"


def main():
    if len(sys.argv) != 2:
        print("Usage: python grade.py <marks>")
        return
    marks = float(sys.argv[1])
    print("Marks:", marks, "-> Grade:", get_grade(marks))


if __name__ == "__main__":
    main()
