# SESSION 30 – Wall Following

# Step 1: Input values
desired = 0.5   # desired distance (m)
actual = 0.2    # actual distance (m)

# Step 2: Apply rule
if actual < desired:
    print("Move Away from Wall")
else:
    print("Maintain Distance")

print("\nProgram Executed Successfully")
