# Based on Fig. 3.18: fig03_18.py
# Counter-controlled repetition with the
# for structure and range function.

for counter in range(10):
    print(counter, end=', ')
    # Output : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

# The Range function can be initialized with more than one argument in the other cases.
# Its syntax is: range(start=0, stop, step=1)
# range(10) -> start=0, stop=10, step=1 >> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 - 10 elements
# range(1, 10) -> start=1, stop=10, step=1 >> 1, 2, 3, 4, 5, 6, 7, 8, 9 - 9 elements
# range(10, 0, -1) -> start=10, stop=0, step=-1 >> 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 - 10 elements
# range(0, 10, 2) -> start=0, stop=10, step=2 >> 0, 2, 4, 6, 8 - 5 elements
# if you want use step, you need define start and stop.

print('\n')
word = "apple"
for index in range(len(word)):
    print(index, word[index])

print('\n')
for index, char in enumerate("apple"):
    print(index, char)

print('\n')
for _ in range(3):
    print("Ding-dong")

print('\n')
max_days = 31
for week in range(5):
    for day in range(1, 8):
        date = day + (7 * week)
        if date > max_days:
            continue
        print(f"{day+(7 * week):>4d}", end="")
    print()
