import sys
from collections import Counter
import urllib.request
import os


def get_dict():
    p = 'words.txt'
    if not os.path.exists(p):
        print("Dictionary not found, downloading...")
        url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
        try:
            resp = urllib.request.urlopen(url)
            data = resp.read()
            f = open(p, 'wb')
            f.write(data)
            f.close()
            print("Downloaded!")
        except:
            print("Download failed, trying backup...")
            url2 = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt'
            resp = urllib.request.urlopen(url2)
            data = resp.read()
            f = open(p, 'wb')
            f.write(data)
            f.close()
    return p


def solve(w):
    words = []
    dict_path = get_dict()
    f = open(dict_path, 'r')
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

