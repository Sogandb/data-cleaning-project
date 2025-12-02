import pandas as pd

df = pd.DataFrame({
    "name": ["Ali", "Sara", "Reza", None],
    "age": [21, 19, None, 25],
    "score": [85, 90, 77, 88]
})

# نمایش اولیه
print(df)

# پاکسازی داده
df = df.dropna(subset=["name"])
df["age"] = df["age"].fillna(df["age"].mean())

# تحلیل اولیه
print("\nAverage age:", df["age"].mean())
print("Max score:", df["score"].max())

# خروجی CSV
df.to_csv("cleaned_data.csv", index=False)