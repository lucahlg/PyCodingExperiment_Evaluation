from space_age import SpaceAge

# Test data
age_in_seconds = 1_000_000_000
space_age = SpaceAge(age_in_seconds)

# Test ages on different planets
print("Calculated ages:")
print(f"Earth: {space_age.age_on('Earth')}")
print(f"Mercury: {space_age.age_on('Mercury')}")
print(f"Venus: {space_age.age_on('Venus')}")
print(f"Mars: {space_age.age_on('Mars')}")
print(f"Jupiter: {space_age.age_on('Jupiter')}")
print(f"Saturn: {space_age.age_on('Saturn')}")
print(f"Uranus: {space_age.age_on('Uranus')}")
print(f"Neptune: {space_age.age_on('Neptune')}")

# Test ages on different planets with updated expected values
assert space_age.age_on('Earth') == 31.69, "Age on Earth should be 31.69"
assert space_age.age_on('Mercury') == 131.57, "Age on Mercury should be 131.57"
assert space_age.age_on('Venus') == 51.51, "Age on Venus should be 51.51"
assert space_age.age_on('Mars') == 16.85, "Age on Mars should be 16.85"
assert space_age.age_on('Jupiter') == 2.67, "Age on Jupiter should be 2.67"
assert space_age.age_on('Saturn') == 1.08, "Age on Saturn should be 1.08"
assert space_age.age_on('Uranus') == 0.38, "Age on Uranus should be 0.38"
assert space_age.age_on('Neptune') == 0.19, "Age on Neptune should be 0.19"

print("All tests passed!")

