import numpy as np 

#Integer Array Indexing - Select arbitrary elements by providing an array of indicies . This is like picking specific items from alist using their positions 

# Perfect for sampling specific data points

scores=np.array([85,92,78,95,88,76.91,89,84,93,87,90,82])
positions=[3,7,12]
selected_scores=scores[positions]

#Boolean array Indexing (Masking) - select elements based on conditions.Create a "mask " of Ture/False values, then use it to filter the array . 

# Ideal for filtering and conditional selections.

passing=scores>=80
passing_scores=scores[passing]

x = np.arange(10, 0, -1)
print("Array for integer indexing:", x)


selected_elements = x[np.array([3, 3, 1, 8])]
print("Selected elements with integer array:", selected_elements)



y = np.array([1., -1., -2., 3.])
print("\nArray for boolean indexing:", y)

mask = y < 0
print("Boolean mask (y < 0):", mask)


negative_elements = y[mask]
print("Elements where y < 0:", negative_elements)