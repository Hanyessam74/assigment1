import matplotlib.pyplot as plt
import numpy as np

def create_visualization():
    # Generate random data
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    sizes = np.random.randint(1, 100, size=len(categories))

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Random Data Distribution')

    # Save the plot as a PNG file
    plt.savefig('vis.png')
    plt.close()

def main():
    # Create the visualization
    create_visualization()

if __name__ == "__main__":
    main()
