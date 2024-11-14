# Given values
v_i_kmh = 310  # Initial velocity in km/h
d = 1000       # Distance in meters
v_f = 0        # Final velocity (jet stops)

# Convert initial velocity from km/h to m/s
v_i = v_i_kmh * (5 / 18)

# Using the equation: a = (v_f^2 - v_i^2) / (2 * d)
a = (v_f**2 - v_i**2) / (2 * d)

# Output the result
print(f"Required constant acceleration: {a} m/s^2")
