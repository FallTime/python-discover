# Question 2.3:
# State the order of evaluation of the operators in each of the following Python statements and
# show the value of x after each statement is performed.
# a) x = 7 + 3 * 6 / 2 - 1 -> 7 + 18 / 2 - 1 -> 7 + 9.0 - 1 -> 15.0
# b) x = 2 % 2 + 2 * 2 - 2 / 2 -> 0 + 4 - 1.0 -> 3.0
# c) x = ( 3 * 9 * ( 3 + ( 9 * 3 / ( 3 ) ) ) ) -> ( 3 * 9 * ( 3 + ( 27 / 3  ) ) ) -> ( 3 * 9 * ( 3 + 9.0 ) ) ->
#        ( 3 * 9 * 12.0 ) -> 324.0

print(7 + 3 * 6 / 2 - 1)
print(2 % 2 + 2 * 2 - 2 / 2)
print((3 * 9 * (3 + (9 * 3 / 3))))
