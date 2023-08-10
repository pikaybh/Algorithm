A, B = map(int, input().split())
assert - 1_000 <= A or - 1_000 <= B or A <= 1_000 or B <= 1_000
print('<' if A < B else '>' if A > B else '==')