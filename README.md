# Text-to-SQL Retrieval

This repository enables text-to-SQL conversion and retrieval using PostgreSQL. The project includes data generation, database setup, and a Streamlit app for easy interaction.

## Prerequisites

Ensure you have the following installed:
- Python 3.7 or later
- PostgreSQL

## Setup

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/harshit2408/text-2-sql_retreival.git>
   cd <https://github.com/harshit2408/text-2-sql_retreival.git>
   ```

2. **Install required dependencies**:
   Use the provided `requirements.txt` file to install the necessary Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**:
   Ensure you have a running PostgreSQL instance. Create a database for this project if not already done:
   ```bash
   psql -U <username> -c "CREATE DATABASE inv_mng;"
   ```
   Replace `<username>` with your PostgreSQL username.

4. **Generate data and populate PostgreSQL**:
   Run the `datagen.py` script to generate data and populate the PostgreSQL database.
   ```bash
   python datagen.py
   ```

5. **Run the Streamlit app**:
   Launch the application using the `app.py` file.
   ```bash
   streamlit run app.py
   ```

## Features

- **Text-to-SQL Conversion**: Convert natural language queries into SQL statements.
- **Interactive UI**: User-friendly interface powered by Streamlit.
- **Data Generation**: Automatically populate the PostgreSQL database for testing and demonstration.

## Notes

- Ensure your PostgreSQL credentials and database configurations in `datagen.py` and `app.py` are correct before running the scripts.
- The app assumes a default database setup as per `datagen.py`. Adjust as needed for custom data.

## Example Usage

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <https://github.com/harshit2408/text-2-sql_retreival.git>
   cd <https://github.com/harshit2408/text-2-sql_retreival.git>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create and configure the PostgreSQL database:
   ```bash
   psql -U <username> -c "CREATE DATABASE inv_mng;"
   ```

4. Generate and populate data:
   ```bash
   python datagen.py
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   