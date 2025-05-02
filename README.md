
# 🛒 Task 7: SQLite Sales Summary with Python

A beginner-friendly project to demonstrate how to connect Python with an SQLite database, run SQL queries, analyze data using Pandas, and visualize results using Matplotlib.

---

## 🚀 Features

- ✅ Creates and populates a local SQLite database (`sales_data.db`) with sample sales data
- ✅ Runs SQL queries to calculate total quantity sold and revenue per product
- ✅ Loads SQL results into a Pandas DataFrame
- ✅ Displays results in the console
- ✅ Plots and saves a simple bar chart of product revenue (`sales_chart.png`)

---

## 🛠️ Tech Stack

- **Python 3.x**
- **SQLite3** – lightweight SQL database
- **Pandas** – for data manipulation and analysis
- **Matplotlib** – for data visualization

---

## 📁 Project Structure

```

Task7\_sqlite-sales\_summary/
├── task7.py            # Main Python script (creates DB, runs SQL, plots chart)
├── sales_data.db       # Auto-generated SQLite database
├── sales_chart.png     # Auto-generated bar chart image
└── README.md           # Project overview and usage guide

```

---

## 📊 Sample Output

**Console Summary:**
```

Sales Summary:
product  total\_qty  revenue
0   Apple         15      7.5
1  Banana         30      9.0
2  Orange         25     10.0

````

**Bar Chart:**

![Sales Chart](sales_chart.png)

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GAURIPATIL-2004/Task7_sqlite-sales_summary.git
cd Task7_sqlite-sales_summary
````

### 2️⃣ Install Required Libraries

Make sure you have `pandas` and `matplotlib` installed. You can install them using:

```bash
pip install pandas matplotlib
```

### 3️⃣ Run the Script

```bash
python task7.py
```

The script will:

* Create the database and insert sample data
* Run the sales summary query
* Print the results
* Generate and save a revenue bar chart

---

## 🧠 Key Concepts Demonstrated

* **SQL Integration in Python** using `sqlite3`
* **GROUP BY** and aggregate functions in SQL
* **DataFrame manipulation** using Pandas
* **Basic charting** with Matplotlib
* **Lightweight database design** for beginner-level analytics

---

## 💡 Why This Project?

This is a great starting point to learn how Python can be used for:

* Working with databases
* Performing data analysis
* Generating simple visualizations for business reporting

---

## 📬 Contributing / Questions

If you have any suggestions or issues, feel free to:

* 🐛 [Open an issue](https://github.com/GAURIPATIL-2004/Task7_sqlite-sales_summary/issues)
* 🍴 Fork this repo and submit a pull request


---

## 🙌 Acknowledgements

Thanks to basic Python and data analysis resources that inspired this project.

---

### 🔗 Connect with Me

* GitHub: [@GAURIPATIL-2004](https://github.com/GAURIPATIL-2004)

---
