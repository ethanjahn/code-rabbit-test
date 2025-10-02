import sys
from collections import Counter


def solve(w):
    words = []
    f = open('/usr/share/dict/words', 'r')
    lines = f.readlines()
    f.close()
    
    for l in lines:
        l = l.strip().lower()
        if len(l) != len(w):
            continue
        x = Counter(l)
        y = Counter(w.lower())
        if x == y:
            words.append(l)
    
    return words


def main():
    if len(sys.argv) < 2:
        print("Usage: python jumble_solver.py <word>")
        sys.exit(1)
    
    w = sys.argv[1]
    print(f"Solving jumble: {w}")
    
    r = solve(w)
    
    if len(r) == 0:
        print("No solutions found!")
    else:
        print(f"Found {len(r)} solution(s):")
        for s in r:
            print(f"  - {s}")


if __name__ == "__main__":
    main()

