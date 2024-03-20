def  anagram_checker(s,t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(anagram_checker(s,t))

    s2 = "rat"
    t2 = "car"
    print(anagram_checker(s2, t2))
