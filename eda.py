import pandas as pd

def load_dataset(file_path):
    try:
        # Read the dataset file
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def generate_insights(df):
    insights = []

    # Insight 1: Summary statistics
    summary_stats = df.describe()
    insights.append("Insight 1: Summary Statistics\n" + summary_stats.to_string())

    # Insight 2: Data types
    data_types = df.dtypes
    insights.append("\nInsight 2: Data Types\n" + data_types.to_string())

    # Insight 3: Unique values
    unique_values = df.nunique()
    insights.append("\nInsight 3: Unique Values\n" + unique_values.to_string())

    return insights

def save_insights(insights):
    for i, insight in enumerate(insights, start=1):
        with open(f"eda-in-{i}.txt", "w") as f:
            f.write(insight)

def main():
    # Load dataset
    df = load_dataset("Bank_Target_Marketing_Dataset.csv")
    if df is None:
        return
    
    insights = generate_insights(df)
    
    save_insights(insights)

if __name__ == "__main__":
    main()
