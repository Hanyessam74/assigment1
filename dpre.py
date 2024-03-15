import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.decomposition import PCA
from sklearn.preprocessing import KBinsDiscretizer

def data_preprocessing(df):
    df = df.drop_duplicates()

    imputer = SimpleImputer(strategy='mean')
    df[df.select_dtypes(include=['number']).columns] = imputer.fit_transform(df.select_dtypes(include=['number']))

    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        try:
            df[col] = LabelEncoder().fit_transform(df[col])
        except TypeError:  # Handle columns with mixed data types
            df[col] = df[col].astype(str)  # Convert to string

    discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    df[df.select_dtypes(include=['number']).columns] = discretizer.fit_transform(df.select_dtypes(include=['number']))

    return df  

if __name__ == "__main__":
    df = pd.read_csv("Bank_Target_Marketing_Dataset.csv")
    preprocessed_df = data_preprocessing(df)
    preprocessed_df.to_csv("res_dpre.csv", index=False)
    print("Resulting dataframe saved as res_dpre.csv")
