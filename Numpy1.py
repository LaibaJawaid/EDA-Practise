import numpy as np

# QUESTION 1: STUDENT SCORES ANALYSIS

print("QUESTION 1: STUDENT SCORES MATRIX OPERATIONS \n")

# 1. Create 5x4 array of student scores (50-100)

np.random.seed(42)  # For reproducible results
scores = np.random.randint(50, 101, size=(5, 4))

subjects = ['Math', 'Science', 'English', 'History']
students = ['Student_1', 'Student_2', 'Student_3', 'Student_4', 'Student_5']

print("1. Original Scores Matrix (5 students x 4 subjects):")
print(scores)
print(f"Shape: {scores.shape}, Type: {scores.dtype}")

# 2. Calculations
print("\n2. STATISTICAL CALCULATIONS:")

# Row-wise mean (student average)
student_avg = scores.mean(axis=1)
print(f"Student averages: {student_avg}")
# Column-wise mean (subject average)
subject_avg = scores.mean(axis=0)
print(f"Subject averages: {subject_avg}")

# 3. Normalize scores (z-score normalization)
print("\n3. NORMALIZED SCORES (z-score):")
scores_normalized = (scores - scores.mean(axis=0)) / scores.std(axis=0)
print(scores_normalized.round(2))

# 4. Boolean mask for scores > 85
print("\n4. BOOLEAN MASK (scores > 85):")
high_scores_mask = scores > 85
print(f"High scores count: {high_scores_mask.sum()}")

# 6. Correlation matrix between subjects
print("\n6. CORRELATION MATRIX BETWEEN SUBJECTS:")
correlation_matrix = np.corrcoef(scores, rowvar=False)  # Column-wise correlation
print(correlation_matrix.round(2))

# 7. Scores > 1 std above mean
print("\n7. SCORES > 1 STD ABOVE MEAN:")
high_performance_mask = scores > (scores.mean() + scores.std())
high_performance_scores = scores[high_performance_mask]
print(f"Count: {len(high_performance_scores)}, Values: {high_performance_scores}")

# 10. Create grade categories
print("\n10. GRADE CATEGORIZATION:")
def assign_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

# Vectorized grading
grade_categories = np.vectorize(assign_grade)(scores)
print(grade_categories)

# 11. Weighted scores (different weight for each subject)
print("\n11. WEIGHTED SCORES (Math:0.3, Science:0.3, English:0.2, History:0.2):")
weights = np.array([0.3, 0.3, 0.2, 0.2])
weighted_scores = scores * weights
weighted_totals = weighted_scores.sum(axis=1)
print(f"Weighted totals: {weighted_totals}")