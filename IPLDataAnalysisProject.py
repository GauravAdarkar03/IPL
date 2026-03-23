import pandas as pd

# ==============================
# LOAD DATA
# ==============================
deliveries = pd.read_csv("/Users/gauravadarkar/Downloads/AI_Projects/deliveries.csv")
matches = pd.read_csv("/Users/gauravadarkar/Downloads/AI_Projects/matches.csv")

# ==============================
# TASK 1: DEATH OVER ANALYSIS
# ==============================

# Filter overs 16–20
death_overs = deliveries[deliveries['over'].isin([16,17,18,19,20])]

# Group by batsman
batsman_stats = death_overs.groupby('batter').agg(
    total_runs=('batsman_runs', 'sum'),
    balls_faced=('batsman_runs', 'count')
).reset_index()

# Strike rate
batsman_stats['strike_rate'] = (batsman_stats['total_runs'] / batsman_stats['balls_faced']) * 100

# Filter batsmen with >= 200 balls
qualified = batsman_stats[batsman_stats['balls_faced'] >= 200]['batter']
filtered_stats = batsman_stats[batsman_stats['batter'].isin(qualified)]

# Top 10
top_10_death = filtered_stats.sort_values(by='strike_rate', ascending=False).head(10)

print("\n Top 10 Death Over Batsmen:")
print(top_10_death)


# ==============================
# TASK 2: ORANGE CAP ANALYSIS
# ==============================

# Merge datasets
merged_df = deliveries.merge(matches[['id', 'season']], left_on='match_id', right_on='id', how='left')

# Group by season and batsman
season_runs = merged_df.groupby(['season', 'batter'])['batsman_runs'].sum().reset_index()

# Sort and get top scorer per season
season_runs_sorted = season_runs.sort_values(['season', 'batsman_runs'], ascending=[True, False])
orange_cap = season_runs_sorted.drop_duplicates(subset=['season'])

print("\n Orange Cap Winners:")
print(orange_cap)


# ==============================
# TASK 3: MISSING VALUES
# ==============================

# Missing values count
print("\n Missing Values:")
print(matches.isnull().sum())

# Drop rows where all values are null
matches = matches.dropna(how='all')

# Fill missing values
matches['city'] = matches['city'].fillna("Unknown")
matches['winner'] = matches['winner'].fillna("No Result")

# Verify
print("\n After Cleaning:")
print(matches[['city', 'winner']].isnull().sum())

# City distribution
print("\n City Distribution:")
print(matches['city'].value_counts())