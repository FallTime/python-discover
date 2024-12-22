"""
Question 3.8: (Pythagorean Triples)
A right triangle can have sides that are all integers. The set of three integer values for the sides of a right
triangle is called a Pythagorean triple. These three sides must satisfy the relationship that the sum of the
squares of two of the sides is equal to the square of the hypotenuse.
Find all Pythagorean triples for side1, side2 and hypotenuse all no larger than 20.
Use a triple-nested for-loop that tries all possibilities.
This is an example of “brute force” computing. You will learn in more advanced computer science courses that
there are many interesting problems for which there is no known algorithmic approach other than sheer brute force.
Formula: a^2 + b^2 = c^2
"""

def list_pythagorean_triples(max_value):
    pythagorean_triples_coordinates = []
    for a in range(1, max_value):
        for b in range(1, max_value):
            for c in range(1, max_value):
                if (a * a + b * b) == (c * c):
                    coordinate = [a, b, c]
                    pythagorean_triples_coordinates.append(coordinate)

    return pythagorean_triples_coordinates

print(list_pythagorean_triples(20))
