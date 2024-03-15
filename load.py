import argparse
import pandas as pd

def load_dataset(file_path):
    try:
        # Read the dataset file
        df = pd.read_csv(file_path)
        # Perform any operations with the dataframe as needed
        print("Dataset loaded successfully:")
        print(df.head())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    parser = argparse.ArgumentParser(description="Load dataset from a file.")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")
    args = parser.parse_args()

    load_dataset(args.file_path)

if __name__ == "__main__":
    main()
