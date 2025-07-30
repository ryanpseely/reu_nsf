To-Do List

Starting list from my powerpoint
- [ ] Perfect visualizations
- [ ] re-run the TF-IDF mann-whitney pairwise U-tests
- [ ] Regression model for lexical change
- [ ] Regression model for predicting year
- [ ] Poster stuff
- [X] Two-sample t-tests/ANOVA on year to year differences in average funding amounts (inflation adjusted)
- [X] Edit the non-textual analysis code for full dataset (6 months each from 16 to 25)

Code for reading in the cleaned yearly data files:
```
# read in data
folder_path = "cleaned_yearly_data"
years = list(range(2016, 2026))  # 2016 to 2025 inclusive

# Read and stack all yearly files
dataframes = []

for year in years:
    file_path = os.path.join(folder_path, f"awards_{year}.csv")

    df = spark.read \
        .option("header", True) \
        .option("multiLine", True) \
        .option("quote", '"') \
        .option("escape", '"') \
        .option("delimiter", ",") \
        .csv(file_path)

    dataframes.append(df)

# Stack (union) all DataFrames
awards_data = dataframes[0]
for df in dataframes[1:]:
    awards_data = awards_data.unionByName(df)
```
