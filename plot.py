import csv
import matplotlib.pyplot as plt


def main():
    # Load Y-values (vertical position) from the CSV
    y_values = []

    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            y = float(row[1])  # assuming Y is in 3rd column (index 2)
            y_values.append(y)

    # Convert positions to displacements

    y_values = [y_values[i] - y_values[0] for i in range(len(y_values))]

    # Time vector (assuming 100 fps)
    print(len(y_values))
    frame_count = len(y_values)
    fps = 115.2 # 100
    time = [i / fps for i in range(frame_count)]


    # Fit to the model y(t) = 0.5 * a * t^2
    def model(t, a):
        return 0.5 * a * t**2

    from scipy.optimize import curve_fit
    # Convert to meters first
    meters = [x / 1000 for x in y_values]
    popt, pcov = curve_fit(model, time, meters)
    estimated_g = popt[0]

    print(f"Estimated acceleration a ≈ {estimated_g:.4f} m/s²")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(time, y_values, 'bo-', label='Measured position')
    # plt.plot(time, model(time, estimated_g), 'r--', label=f'Fit: y=½·{estimated_g:.2f}·t²')
    plt.xlabel('Time (s)')
    plt.ylabel('Vertical position (mm)')
    plt.title('Free Fall: Position vs. Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("plotting.eps", format="eps", dpi=1000)
    plt.show()

if __name__=="__main__":
    main()
    exit(0)
