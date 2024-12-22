"""
Question 3.7:
Write a program that prints the following patterns separately, one below the other each pattern separated from
the next by one blank line. Use for loops to generate the patterns. All asterisks (*) should be printed by a
single statement of the form

    print '*',

(which causes the asterisks to print side by side separated by a space).
(Hint: The last two patterns require that each line begin with an appropriate number of blanks.)
Extra credit: Combine your code from the four separate problems into a single program that prints all four
patterns side by side by making clever use of nested for loops.
For all parts of this program—minimize the numbers of asterisks and spaces and the number of statements that
print these characters.

Pattern A            Pattern B            Pattern C            Pattern D
*                    * * * * * * * * * *  * * * * * * * * * *                    *
* *                  * * * * * * * * *      * * * * * * * * *                  * *
* * *                * * * * * * * *          * * * * * * * *                * * *
* * * *              * * * * * * *              * * * * * * *              * * * *
* * * * *            * * * * * *                  * * * * * *            * * * * *
* * * * * *          * * * * *                      * * * * *          * * * * * *
* * * * * * *        * * * *                          * * * *        * * * * * * *
* * * * * * * *      * * *                              * * *      * * * * * * * *
* * * * * * * * *    * *                                  * *    * * * * * * * * *
* * * * * * * * * *  *                                      *  * * * * * * * * * *

"""

def print_pattern(pattern_letter):
    space_count = -1
    match pattern_letter:
        case 'A':
            count = 0
        case 'B':
            count = 10
        case 'C':
            count = 10
            space_count = 0
        case 'D':
            count = 0
            space_count = 9
        case _:
            print(f"Pattern {pattern_letter} don't exist!")
            return -1

    for i in range(10):
        if count == 0:
            if space_count == 9:
                while i < space_count:
                    print(" ", end=' ')
                    space_count -= 1
                space_count = 9
            while count <= i:
                print('*', end=' ')
                count += 1
            count = 0
        else:
            if space_count == 0:
                while i > space_count:
                    print(" ", end=' ')
                    space_count += 1
                space_count = 0
            while i < count:
                print('*', end=' ')
                count -= 1
            count = 10

        print()
    print()


print_pattern('A')
print_pattern('B')
print_pattern('C')
print_pattern('D')
print_pattern('E')

'''
Initial Logic of Patterns

def pattern_a():
    count = 0
    for i in range(10):
        while count <= i:
            print('*', end=' ')
            count += 1
        count = 0
        print()

def pattern_b():
    count = 10
    for i in range(10):
        while i < count:
            print('*', end=' ')
            count -= 1
        count = 10
        print()

def pattern_c():
    count = 10
    space_count = 0
    for i in range(10):
        while i > space_count:
            print(" ", end=' ')
            space_count += 1
        while i < count:
            print('*', end=' ')
            count -= 1
        space_count = 0
        count = 10
        print()

def pattern_d():
    count = 0
    space_count = 9
    for i in range(10):
        while i < space_count:
            print(" ", end=' ')
            space_count -= 1
        while i >= count:
            print('*', end=' ')
            count += 1
        space_count = 9
        count = 0
        print()
'''