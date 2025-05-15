# 🏠 Bengaluru House Real Estate Price Prediction

This project aims to predict residential property prices in Bengaluru, India, using features such as location, number of bedrooms, square footage, number of bathrooms, and more. By applying machine learning techniques, we developed an application with a predictive model to help buyers, sellers, and real estate professionals make informed, data-driven decisions.

## 📌 Table of Contents

- [🔍 About the Project](#-about-the-project)  
- [📁 Project Structure](#-project-structure)  
- [🔧 Technologies Used](#-technologies-used)  
- [📊 Modeling Pipeline](#-modeling-pipeline)  
- [📈 Results](#-results)  
- [▶️ How to Run](#️-how-to-run)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)  
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🔍 About the Project

The Bengaluru real estate market is vast and complex. This project leverages historical housing data to build a regression model that predicts the estimated price of a property based on its characteristics.

Main goals:

- Provide an estimated market price for residential properties  
- Identify key factors influencing house prices  
- Explore the housing market through data analysis

---

## 📁 Project Structure

📦 Bengaluru-House-Real-Estate-Price-Prediction
├── client/      # Front-end web application  
├── data/        # Raw and processed datasets  
├── model/       # Jupyter notebooks for EDA, modeling, training, and artifact generation  
├── server/      # Back-end application in Python  
└── README.md    # Project documentation

---

## 🔧 Technologies Used

- Jupyter Notebook
- Python 3 
-   Pandas  
-   NumPy  
-   Scikit-learn  
-   Matplotlib & Seaborn
-   Pickle
-   Flask  
- HTML 5
- CSS
- JavaScript

---

## 📊 Modeling Pipeline

1. **Data Collection**: Dataset sourced from [Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data);
2. **Exploratory Data Analysis (EDA)**: Data visualization and statistical analysis;
3. **Data Cleaning**: Handling missing values, removing outliers, data type conversions;
4. **Feature Engineering**: Creating and selecting relevant features;
5. **Model Training**: Testing algorithms like Linear Regression, Lasso and Decision Tree;

---

## 📈 Results

- Best performing model: **Linear Regression Model**  
- Score: **0.71**  

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Bengaluru-House-Real-Estate-Price-Prediction.git
```

2. Install the dependencies

3. Run the server:
```bash
py .\server\server.py
```
4. Double-Click app.html on client folder

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with suggestions and improvements.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more details.

## 🙏 Acknowledgments

This project was originally inspired by the Bangalore Home Prices Prediction tutorial by Dhaval Patel from the [codebasics](https://www.youtube.com/@codebasics) YouTube channel. 

[Original Project Playlist](https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg&index=1)

I have extended and modified the original work significantly to include my own data cleaning processes, feature engineering techniques, model improvements, and full documentation. This version reflects my learning journey and is part of my personal portfolio.
