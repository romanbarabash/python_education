from cources.coursera_mipt.week_4.unit_tests.program_under_test import Asteroid

apophis = Asteroid(2099942)

print(f'Name: {apophis.name}')
print(f'Diameter: {apophis.diameter}m')

print(f'Date: {apophis.closest_approach["date"]}')
print(f'Distance: {apophis.closest_approach["distance"]:.2} LD')
