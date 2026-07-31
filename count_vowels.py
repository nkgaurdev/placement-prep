def count_vowels():
    s=input()
    count=0
    for ch in s:
        if ch in "aeiou":
            count+=1
    return count

print(count_vowels())