import matplotlib.pyplot as plt
import pandas as pd

def plot(locations):
    plt.figure(figsize=(8, 6))
    plt.scatter(locations['x'], locations['y'], c='blue')
    for i, row in locations.iterrows():
        plt.text(row['x']+0.1, row['y']+0.1, str(row['id']))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Customer Locations")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('data/customer_locations.csv')
    plot(df)
