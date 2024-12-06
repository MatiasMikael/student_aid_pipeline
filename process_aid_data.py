import pandas as pd

# Step 1: Load the dataset
print("Step 1: Loading the dataset...")
data = pd.read_csv("opintotuki.csv", encoding="utf-8")

# Step 2: Filter for only universities and universities of applied sciences
print("Step 2: Filtering for universities and universities of applied sciences...")
data = data[data["oppilaitosaste"].isin(["Ammattikorkeakoulut", "Yliopistot"])]

# Step 3: Remove rows where 'etuus' is 'Opintolainan valtiontakaus'
print("Step 3: Removing rows with 'Opintolainan valtiontakaus' in 'etuus'...")
data = data[data["etuus"] != "Opintolainan valtiontakaus"]

# Step 4: Rename 'Tieto puuttuu' to 'Määrittelemätön'
print("Step 4: Handling rows with 'Tieto puuttuu' in 'ikaryhma'...")
data["ikaryhma"] = data["ikaryhma"].replace("Tieto puuttuu", "Määrittelemätön")

# Step 5: Convert 'maksettu_eur' to numeric and remove rows with 0.00
print("Step 5: Converting 'maksettu_eur' to numeric and removing rows with 0.00 payments...")
data["maksettu_eur"] = data["maksettu_eur"].astype(str).str.replace(",", ".").str.replace(" ", "").astype(float)
data = data[data["maksettu_eur"] > 0]

# Step 6: Group the data by municipality, age group, benefit type, and institution level
print("Step 6: Grouping data by municipality, age group, benefit type, and institution level...")
grouped_data = data.groupby(["kunta_nimi", "ikaryhma", "etuus", "oppilaitosaste"], as_index=False).agg({
    "saaja_lkm": "sum",        # Sum of recipients
    "maksettu_eur": "sum"      # Sum of payments in euros
})

# Step 7: Format the "maksettu_eur" column to add thousand separators and round to the nearest integer
print("Step 7: Formatting 'maksettu_eur' with thousand separators without decimals...")
grouped_data["maksettu_eur"] = grouped_data["maksettu_eur"].apply(
    lambda x: f"{int(round(x)):,}".replace(",", " ")  # Thousand separator in Finnish format, rounded to nearest integer
)

# Ensure quotes are correct
grouped_data["maksettu_eur"] = grouped_data["maksettu_eur"].str.replace('"""', '"')

# Step 8: Save the processed data
print("Step 8: Saving the processed data to 'processed_opintotuki.csv'...")
grouped_data.to_csv("processed_opintotuki.csv", index=False, encoding="utf-8-sig")