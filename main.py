from recommend.preprocessing import preprocess_data
from recommend.train_model import train_model
from recommend.session_based_recommend import recommend_products
import kagglehub
import pandas as pd
import os
import pickle
from sklearn.preprocessing import LabelEncoder

# Step 1: Specify the CSV file path directly
csv_file_path = "part-00000-782d7740-2eee-412f-9c1e-98a0ef8c80fe-c000.csv"
df = pd.read_csv(csv_file_path, nrows=1000000)
enc = LabelEncoder()
df["product_id"] = enc.fit_transform(df["product_id"])
df["user_id"] = enc.fit_transform(df["user_id"])
df["user_session"] = enc.fit_transform(df["user_session"])

if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"Dataset file not found at {csv_file_path}")

# # Step 2: Preprocess data
# print("Preprocessing data...")
# df, df_weighted = preprocess_data(csv_file_path)

# Step 3: Train model only if it doesn't already exist
model_file = "model.pkl"

# if not os.path.exists(model_file):
#     print("Training model...")
#     train_model(df_weighted, model_file)
# else:
#     print(f"Model already exists at {model_file}. Skipping training.")

# Step 4: Generate recommendations
print("Generating recommendations...")
target_user_id = 10
target_product_id = 7

# Use the preprocessed dataframe for recommendations
recommendations = recommend_products(model_file, df, target_user_id, target_product_id)

# Display recommendations
print("Top 10 Recommendations:")
print(recommendations)