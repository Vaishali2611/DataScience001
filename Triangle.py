# Right-angled triangle pattern
def print_right_angled_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# Equilateral triangle pattern
def print_equilateral_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

number_of_rows = int(input("Enter the number of rows: "))

print("Right-Angled Triangle:")
print_right_angled_triangle(number_of_rows)

print("\nEquilateral Triangle:")
print_equilateral_triangle(number_of_rows)
