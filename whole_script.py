import matplotlib.pyplot as plt

print("""
How to use:
Type comma-separated pressures for each wave crest and trough.
Example:
Crest: 5000, 5200, 6000, 7000, 8000
Trough: 1000, 1500, 2000, 2500, 3000w
""")

# Inputs
pressure_on_crest = input("Enter crest pressures separated by commas: ")
pressure_on_trough = input("Enter trough pressures separated by commas: ")
water_density = float(input("Enter water density (kg/m³): "))
wall_width = float(input("Enter seawall width (m): "))
gravity = 9.8

try:
    # Convert inputs into lists of floats
    crest_values = [float(num.strip()) for num in pressure_on_crest.split(",")]
    trough_values = [float(num.strip()) for num in pressure_on_trough.split(",")]

    # Ensure equal length
    if len(crest_values) != len(trough_values):
        print("Error: Crest and trough lists must have the same number of values.")
        exit()

    # Store crest/trough pairs as tuples
    waves = [(c, t) for c, t in zip(crest_values, trough_values)]

    # Function to calculate wave height from pressure difference
    def wave_height(crest, trough, rho, g):
        delta_p = crest - trough
        return delta_p / (rho * g)

    # Function to calculate force
    def wave_force(crest, trough, rho, g, width):
        h = wave_height(crest, trough, rho, g)
        area = width * h
        return (crest - trough) * area

    # Calculate forces and heights
    forces = []
    heights = []
    for i, (crest, trough) in enumerate(waves, start=1):
        h = wave_height(crest, trough, water_density, gravity)
        area = wall_width * h
        f = wave_force(crest, trough, water_density, gravity, wall_width)
        forces.append(f)
        heights.append(h)
        print(f"Wave {i}: Height = {h:.2f} m, Area = {area:.2f} m², Force = {f:.2f} N")

    # Average values
    avg_force = sum(forces) / len(forces)
    avg_height = sum(heights) / len(heights)
    print(f"\nAverage wave force: {avg_force:.2f} N")
    print(f"Average wave height: {avg_height:.2f} m")

    # Plot forces
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(forces) + 1), forces, marker='o', linestyle='-', color='b', label="Wave Force")
    plt.axhline(avg_force, color='r', linestyle='--', label=f"Avg Force = {avg_force:.2f} N")
    plt.title("Wave Forces on Seawall")
    plt.xlabel("Wave Number")
    plt.ylabel("Force (N)")
    plt.legend()
    plt.grid(True)

    # Plot heights
    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(heights) + 1), heights, marker='s', linestyle='-', color='g', label="Wave Height")
    plt.axhline(avg_height, color='orange', linestyle='--', label=f"Avg Height = {avg_height:.2f} m")
    plt.title("Wave Heights from Pressure Sensors")
    plt.xlabel("Wave Number")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

except ValueError:
    print("Error: Please enter only numbers separated by commas.")
