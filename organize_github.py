import os
import shutil

# Paths
BASE_DIR = r"C:\Users\SHYAM SASHANK\OneDrive\Desktop\Data_Science"
CODES_DIR = os.path.join(BASE_DIR, "Assginment_Codes")
CSV_DIR = os.path.join(BASE_DIR, "Assginment_CSV")
GITHUB_DIR = os.path.join(BASE_DIR, "GitHub_Portfolio")

# Projects definition
projects = [
    {
        "name": "50_Startups_Prediction",
        "notebook": "Startsups_50.ipynb",
        "csv": "50_Startups.csv",
        "desc": "Predicting startup profits using Multiple Linear Regression based on R&D, Administration, and Marketing spend.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "ToyotaCorolla_Pricing",
        "notebook": "ToyotaCorolla.ipynb",
        "csv": "ToyotaCorolla.csv",
        "desc": "Predicting Toyota Corolla car prices using various regression techniques.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "Airlines_Clustering",
        "notebook": "AirLines_Problem.ipynb",
        "csv": "EastWestAirlines.csv",
        "desc": "Clustering EastWestAirlines passengers into segments for targeted marketing using K-Means and Hierarchical Clustering.",
        "libs": "pandas, numpy, matplotlib, seaborn, scipy, scikit-learn"
    },
    {
        "name": "Fraud_Check_Classification",
        "notebook": "Fraud_check_decision.ipynb",
        "csv": "Fraud_check.csv",
        "desc": "Using Decision Trees to classify whether a person's taxable income is Risky or Good based on multiple attributes.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "CocaCola_Sales_Forecasting",
        "notebook": "Cola_Sales.ipynb",
        "csv": "CocaCola_Sales.csv",
        "desc": "Time series analysis and forecasting of Coca-Cola sales using various statistical and machine learning models.",
        "libs": "pandas, numpy, matplotlib, statsmodels"
    },
    {
        "name": "Zoo_KNN_Classification",
        "notebook": "KNN_Zoo.ipynb",
        "csv": "Zoo.csv",
        "desc": "Classifying zoo animals into their respective categories using the K-Nearest Neighbors (KNN) algorithm.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "Crime_Data_Clustering",
        "notebook": "Crime_data.ipynb",
        "csv": "crime_data.csv",
        "desc": "Clustering US crime data to identify similar crime rates across different states using K-Means and DBSCAN.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "Book_Recommendation_System",
        "notebook": "Recommendation_System_Book.ipynb",
        "csv": "book(RS).csv",
        "desc": "Building a recommendation system for books using collaborative filtering and item-based approaches.",
        "libs": "pandas, numpy, scikit-learn"
    },
    {
        "name": "Salary_Data_Naive_Bayes",
        "notebook": "Salary_Navies.ipynb",
        "csv": "SalaryData_Train_navies.csv",
        "desc": "Predicting salary categories (<=50K or >50K) using Naive Bayes classification.",
        "libs": "pandas, numpy, matplotlib, seaborn, scikit-learn"
    },
    {
        "name": "Forest_Fire_Neural_Network",
        "notebook": "Fireforest_neural_network.ipynb",
        "csv": "forestfires.csv",
        "desc": "Predicting forest fires using Artificial Neural Networks (ANN).",
        "libs": "pandas, numpy, matplotlib, keras, tensorflow, scikit-learn"
    },
    {
        "name": "Text_Mining_NLP",
        "notebook": "Text_Mining.ipynb",
        "csv": "Elon_musk.csv",
        "desc": "Analyzing sentiments and common topics from Elon Musk's tweets using NLP and Text Mining.",
        "libs": "pandas, numpy, matplotlib, seaborn, nltk, spacy, wordcloud"
    },
    {
        "name": "Hypothesis_Testing",
        "notebook": "Assign-3 Hypothesis (1).ipynb",
        "csv": "Cutlets.csv",
        "desc": "Applying various statistical hypothesis tests (t-test, ANOVA, Chi-Square) to data science problems.",
        "libs": "pandas, numpy, scipy, statsmodels"
    }
]

if not os.path.exists(GITHUB_DIR):
    os.makedirs(GITHUB_DIR)

for proj in projects:
    proj_dir = os.path.join(GITHUB_DIR, proj["name"])
    if not os.path.exists(proj_dir):
        os.makedirs(proj_dir)
    
    # Files
    src_notebook = os.path.join(CODES_DIR, proj["notebook"])
    src_csv = os.path.join(CSV_DIR, proj["csv"])
    
    # Copy Notebook
    if os.path.exists(src_notebook):
        shutil.copy(src_notebook, os.path.join(proj_dir, proj["notebook"]))
    
    # Copy CSV
    if os.path.exists(src_csv):
        shutil.copy(src_csv, os.path.join(proj_dir, proj["csv"]))

    # Create README
    readme_content = f"""# {proj['name'].replace('_', ' ')}

## Description
{proj['desc']}

## Dataset
- **File**: `{proj['csv']}`
- **Source**: Included in the repository.

## Libraries Used
{proj['libs']}

## How to Run
1. Install the required libraries: `pip install -r requirements.txt`
2. Open the notebook `{proj['notebook']}` in Jupyter or Colab.
3. Ensure the CSV file is in the same directory.
"""
    with open(os.path.join(proj_dir, "README.md"), "w") as f:
        f.write(readme_content)
    
    # Create requirements.txt
    req_content = proj["libs"].replace(", ", "\n")
    with open(os.path.join(proj_dir, "requirements.txt"), "w") as f:
        f.write(req_content)

print("Organization complete! Files are ready in GitHub_Portfolio.")
