from high_scores import HighScores

# Test data
scores = [30, 50, 20, 70, 90]

# Create an instance of HighScores
high_scores = HighScores(scores)

# Test latest score
assert high_scores.latest() == 90, "Latest score should be 90"

# Test personal best
assert high_scores.personal_best() == 90, "Personal best should be 90"

# Test personal top three
assert high_scores.personal_top_three() == [90, 70, 50], "Top three scores should be [90, 70, 50]"

print("All tests passed!")
