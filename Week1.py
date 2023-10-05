print('1 ---------------------------------------------------------')
print('hello world')
print('2 ---------------------------------------------------------')
print('hello riaz')

print('3 ---------------------------------------------------------')

celsius = 38.4
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit")

print('4 ---------------------------------------------------------')

total_matches = 609
total_innings = 1014
times_not_out = 162
total_runs = 48426

batting_average = total_runs / (total_innings - times_not_out)

print(f"Geoffrey Boycott's batting average is: {batting_average:.2f}")

print('5 ---------------------------------------------------------')

students = [113,175,12]
labGroup = 24

for num_students in students:
    full_groups = num_students // labGroup
    left_over = num_students % labGroup

    print(f"For {num_students} students:")
    print(f"   Full groups: {full_groups}")
    print(f"   Left over students in smaller group: {left_over}")









