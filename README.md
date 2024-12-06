## Student Aid Pipeline

This project processes and analyzes data related to student financial aid and benefits. The dataset focuses on recipients of student aid and the amounts paid, sourced from the Finnish Social Insurance Institution (Kela). The goal is to clean the data using Python in VS Code, transfer it to Snowflake, perform SQL queries to filter the data, save the results as .csv files, and visualize them in Tableau. 

 ## Note

The dataset used in this project is from 2024. However, it does not cover the entire year, as December data is not yet included.

## Pipeline Steps

* Data Cleaning

The `process_aid_data.py` script:
1. Loads the dataset.
2. Filters for universities and universities of applied sciences.
3. Excludes "Opintolainan valtiontakaus".
4. Handles missing values.
5. Converts and filters payment data.
6. Aggregates data by key attributes.
7. Saves the cleaned data to `processed_opintotuki.csv`.

* Data Upload

The `upload_to_snowflake.py` script:
1. Loads credentials and connects to Snowflake.
2. Reads the cleaned CSV file.
3. Converts payment data for compatibility.
4. Uploads to the `PROCESSED_OPINTOTUKI` table.

* Visualization

Tableau was used to create visualizations:
* **Municipalities with the Lowest Student Aid and Housing Benefits**: Highlights municipalities with the lowest combined payments for student aid and housing benefits.
* **Student Aid Payments by Municipality and Age Group in Finland (Highest to Lowest)**: Displays student aid payments ranked from highest to lowest by municipality and age group. Note: The title is misleading as it suggests data is categorized strictly by age groups, but it includes all students regardless of age.
* **Top Municipalities for Student Aid Payments (Ages 20-24)**: Focuses on municipalities with the highest student aid payments for young adults aged 20–24.

## Tools

Tools: 
* Python (Pandas, SQLAlchemy, dotenv, Snowflake-SQLAlchemy)
* Snowflake
* Tableau

## Repository Structure

student_aid_pipeline/
* **process_aid_data.py** - Data cleaning script
* **upload_to_snowflake.py** - Upload script
* **opintotuki_data.csv** - The original dataset was named data_2024.csv, but it has been renamed to opintotuki_data.csv for clarity and to better reflect its contents.
* **processed_opintotuki.csv** - Cleaned data

## How to Run

1. Install dependencies:

* `pip install pandas sqlalchemy dotenv snowflake-sqlalchemy`

2. Configure Snowflake credentials:

* Add them to a .env file.

3. Run scripts:

* Cleaning: `python process_aid_data.py`
* Upload: `python upload_to_snowflake.py`

## License

This project is under the MIT License.

The dataset *Opintotuen saajat ja maksetut tuet* is published by Kela under the *Creative Commons Attribution 4.0 International License*. Dataset: [https://www.avoindata.fi/data/fi/dataset/opintotuen-saajat-ja-maksetut-tuet](https://www.avoindata.fi/data/fi/dataset/opintotuen-saajat-ja-maksetut-tuet).

