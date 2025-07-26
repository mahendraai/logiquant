import matplotlib.pyplot as plt
import pandas as pd

def plot(locations):
    plt.figure(figsize=(10, 8))
    plt.scatter(locations['x'], locations['y'], c='blue')
    for i, row in locations.iterrows():
        plt.text(row['x']+0.001, row['y']+0.001, str(row['id']), fontsize=9)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Customer Locations (Real Coordinates)")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('data/customer_locations.csv')
    plot(df)
