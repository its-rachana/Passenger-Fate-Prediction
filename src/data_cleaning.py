import pandas as pd

df = pd.read_csv('../dataset/train.csv')

# checking if the Passenger id is following the correct syntax
pattern = r'^\d{4}_\d{2}$'
df['valid'] = df['PassengerId'].str.match(pattern)
df = df.query('valid').drop(columns='valid')

#checking if HomePlanet has empty values
nulls_before = df['HomePlanet'].isna().sum()
print(f"Null values before: {nulls_before}")
df = df[df['HomePlanet'].notna()].copy()
nulls_after = df['HomePlanet'].isna().sum()
print(f"Null values after: {nulls_after}")

#checking if CryoSleep is either True or False
is_bool = df['CryoSleep'].dropna().isin([True, False]).all()
print(f"All non-null values are boolean: {is_bool}")

#Checking if the cabin follows the regex
pattern = r'^[A-Z]\/\d+\/[PS]$'
print("Count of cabin rows with null values: ",df['Cabin'].isna().sum())
df=df[df['Cabin'].notna()].copy()
df['valid'] = df['Cabin'].str.match(pattern)
df = df.query('valid').drop(columns='valid')
print("Count of cabin rows after cleaning: ",df['Cabin'].isna().sum())

#Checking if Destination has value
print("Count of destination rows with null values: ",df['Destination'].isna().sum())
df = df[df['Destination'].notna()].copy()
print("Count of destination rows after cleaning: ",df['Destination'].isna().sum())
print("Count of passengers whose destination was 55 Cancri e: ",df['Destination'].str.match("55 Cancri e").sum())
df=df[df['Destination'].str.match("55 Cancri e")].copy()
print("Count of passengers whose destination was 55 Cancri e after cleaning: ",df['Destination'].str.match("55 Cancri e").sum())

#Checking if Age is null
print("Count of age is null:", df['Age'].isna().sum())
df = df[df['Age'].notna()].copy()
print("Count of age is null after cleaning:", df['Age'].isna().sum())

#Checking if VIP value is either True or False
is_bool = df['VIP'].dropna().isin([True, False]).all()
print(f"All non-null values are boolean: {is_bool}")

is_bool = df['Transported'].dropna().isin([True, False]).all()
print(f"All non-null values are boolean: {is_bool}")

df.to_csv('../dataset/cleaned_dataset.csv', index=False)