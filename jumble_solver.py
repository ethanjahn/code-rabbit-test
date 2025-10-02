import sys
from collections import Counter
import urllib.request
import os


def download_words():
    file_path = 'wordlist.txt'
    if os.path.exists(file_path):
        print("Dictionary already exists")
        return True
    
    print("Downloading dictionary...")
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
    try:
        resp = urllib.request.urlopen(url)
        data = resp.read()
        f = open(file_path, 'wb')
        f.write(data)
        f.close()
        print("Download complete!")
        return True
    except:
        print("Failed to download")
        return False


def solve(w):
    words = []
    download_words()
    f = open('words.txt', 'r')
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

