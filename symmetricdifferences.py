n = int(input())
english_sub = set(map(int, input().split()))
b = int(input())
french_sub = set(map(int, input().split()))

print(len(english_sub.symmetric_difference(french_sub)))
