#  CSV Cleaner

A lightweight web-based CSV cleaning tool built with **Flask** and **Pandas**. Upload any `.csv` file and get a cleaned version back.

---

##  Features

The CSV Cleaner performs the following automatic data cleaning steps:

###  Column & Row Cleanup
- Removes **completely empty columns**
- Cleans **column names**:
  - Trims leading and trailing whitespace
  - Converts to lowercase
  - Replaces spaces with underscores
- Removes **duplicate rows**

###  Numeric Data Handling
- Replaces missing numeric values with the **column median**
- Removes **outliers** using the **IQR method** 

###  Categorical (Text) Data Handling
- Drops rows with missing **object/string** values
- Cleans text fields: trims whitespace and converts to lowercase

---

##  Tech Stack

| Layer      | Tool        |
|------------|-------------|
| Backend    | Flask       |
| Data       | Pandas      |
| Frontend   | HTML + CSS  |

---

## 📂 Project Structure
```
csv-cleaner/
├── app.py # Flask app
├── cleaner.py # CSV cleaning logic (clean_csv function)
├── templates/
│ └── index.html # Frontend upload form
└── README.md # Project documentation
```
---

##  How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/anna-irene/csv-cleaner.git
cd csv-cleaner

```
### 2. Install dependencies
```bash
pip install flask pandas
```
### 3. Run the Flask app
```bash
python app.py
```
### 4. Open in browser
Go to http://127.0.0.1:5000 in your browser and upload a CSV to clean.

##  Sample Output

The cleaned CSV file will:
-  Have tidy column names and consistent formatting  
-  Be free of missing values and outliers  
-  Be downloadable instantly after cleaning  


## License
This project is open-source. Feel free to use, modify, and improve it!

