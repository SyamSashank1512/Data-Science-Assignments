# Data Science Portfolio: Assignments & Projects

This repository contains a collection of Data Science projects and assignments. Each project includes a Jupyter Notebook (`.ipynb`) and its corresponding dataset (`.csv` or `.xlsx`).

## 🚀 Projects Overview

| Project Name | Description | Notebook | Dataset |
| :--- | :--- | :--- | :--- |
| **Toyota Corolla** | Predicting car prices using various regression techniques. | [ToyotaCorolla.ipynb](Assginment_Codes/ToyotaCorolla.ipynb) | [ToyotaCorolla.csv](Assginment_CSV/ToyotaCorolla.csv) |
| **50 Startups** | Predicting startup profits using Multiple Linear Regression. | [Startsups_50.ipynb](Assginment_Codes/Startsups_50.ipynb) | [50_Startups.csv](Assginment_CSV/50_Startups.csv) |
| **CocaCola Sales** | Time series analysis and forecasting of soft drink sales. | [Cola_Sales.ipynb](Assginment_Codes/Cola_Sales.ipynb) | [CocaCola_Sales.csv](Assginment_CSV/CocaCola_Sales.csv) |
| **Fraud Check** | Classifying taxable income as 'Risky' or 'Good' using Decision Trees. | [Fraud_check_decision.ipynb](Assginment_Codes/Fraud_check_decision.ipynb) | [Fraud_check.csv](Assginment_CSV/Fraud_check.csv) |
| **Zoo Classification** | Categorizing animals using K-Nearest Neighbors (KNN). | [KNN_Zoo.ipynb](Assginment_Codes/KNN_Zoo.ipynb) | [Zoo.csv](Assginment_CSV/Zoo.csv) |
| **Airlines** | Clustering passengers for targeted marketing segments. | [AirLines_Problem.ipynb](Assginment_Codes/AirLines_Problem.ipynb) | [EastWestAirlines.csv](Assginment_CSV/EastWestAirlines.csv) |
| **Crime Data** | Identifying crime patterns across states using K-Means and DBSCAN. | [Crime_data.ipynb](Assginment_Codes/Crime_data.ipynb) | [crime_data.csv](Assginment_CSV/crime_data.csv) |
| **Book Recommendation**| Building a recommendation engine using collaborative filtering. | [Recommendation_System_Book.ipynb](Assginment_Codes/Recommendation_System_Book.ipynb) | [book(RS).csv](Assginment_CSV/book(RS).csv) |
| **Salary Data** | Predicting salary categories using Naive Bayes classification. | [Salary_Navies.ipynb](Assginment_Codes/Salary_Navies.ipynb) | [SalaryData_Test.csv](Assginment_CSV/SalaryData_Test_navies.csv) |
| **Fire Forest** | Predicting forest fires using Artificial Neural Networks (ANN). | [Fireforest_neural_network.ipynb](Assginment_Codes/Fireforest_neural_network.ipynb) | [forestfires.csv](Assginment_CSV/forestfires.csv) |
| **Text Mining** | NLP analysis and sentiment mining of Elon Musk's tweets. | [Text_Mining.ipynb](Assginment_Codes/Text_Mining.ipynb) | [Elon_musk.csv](Assginment_CSV/Elon_musk.csv) |

## 🛠️ How to Use This Repository

### Push a Project Pair
You can use the included PowerShell script to push a project and its dataset in one go:
```powershell
.\push_pair.ps1 -Notebook "FileName.ipynb" -CSV "FileName.csv" -Message "Add Project Description"
```

### Setup
1. Clone the repository.
2. Ensure you have Jupyter installed.
3. Install dependencies (e.g., `pandas`, `numpy`, `scikit-learn`, `seaborn`).

---
Developed by [Shyam Sashank](https://github.com/SyamSashank1512)
