# FitnessData-DSA210Project

## Project Overview
This project focuses on analyzing the impact of daily lifestyle choices on my 1-rep max Bench Press performance over a three-month period. Specifically, I aim to examine how factors such as caloric intake, protein, carbohydrate, and creatine consumption, sleep duration, and sleep quality affect my strength progression. By visualizing trends and performing statistical analyses, I will identify which variables have the most significant influence on my performance and whether adjustments in these factors lead to measurable improvements.

The analysis will include tracking my daily intake and routines and evaluating their correlations with the progression of my Bench Press performance. Additionally, hypothesis testing will be conducted to assess whether changes in specific variables have a statistically significant effect.

---

## Objectives
The primary objectives of this project are:
- **Performance Analysis:** To measure and evaluate the impact of daily caloric, protein, carbohydrate, creatine intake, and sleep patterns on my Bench Press 1-rep max performance.  
- **Key Factor Identification:** To determine the variables with the strongest influence on performance and create a targeted nutrition and training strategy.  
- **Data-Driven Improvement:** To optimize my fitness and strength progression using a data-driven approach.  
- **Applied Data Science:** To apply data analysis and statistical techniques to a real-world problem, enhancing my understanding and skills in data science.

---

## Motivation
The key motivations for selecting this project are:
- **Personal Development:** Fitness is a crucial part of my life, and I strive to continually improve my performance. Understanding how my daily habits influence my physical abilities will help me achieve both short-term and long-term goals.  
- **Data-Driven Approach:** Analyzing the data I collect daily provides a scientific basis for optimizing my fitness and nutrition habits, offering insights into my body’s performance.  
- **DSA 210 Course and Practical Application:** This project allows me to apply theoretical knowledge from the course to a practical problem and gain hands-on experience in data science.  
- **Long-Term Benefits:** The insights and results from this project will serve as a guide for not only Bench Press performance but also for broader fitness goals.

---

## Dataset
The dataset for this project consists of daily records I have maintained over three months. The data includes the following attributes:
- **Date:** The specific day of the record  
- **Calories:** Total caloric intake (kcal)  
- **Protein:** Amount of protein consumed (grams)  
- **Carbohydrates:** Amount of carbohydrates consumed (grams)  
- **Creatine:** Amount of creatine consumed (grams)  
- **Sleep Duration:** Total sleep duration (hours)  
- **Sleep Quality:** Self-rated sleep quality (scale of 1–10)  
- **Bench Press (1RM):** My one-rep max Bench Press performance (kg)

The data is recorded daily in an Excel file, ensuring consistency and accuracy. Before analysis, the dataset will be cleaned to handle any missing or inconsistent entries.

---

## Data Considerations
- Variability in performance due to external factors such as illness or injuries will be noted as potential outliers.  
- The dataset will only include days when the Bench Press was tested to maintain consistency in the dependent variable.  
- I will document any significant changes in workout routines or nutrition plans that may impact the analysis.

---

## Tools and Technologies
- **Python** for data cleaning, analysis, and visualization  
- **Pandas** for data manipulation and preprocessing  
- **Matplotlib** and **Seaborn** for creating visualizations (e.g., correlations between intake and performance)  
- **SciPy** for hypothesis testing (e.g., to evaluate significant predictors of performance)

---

## Analysis Plan
1. **Data Collection:**  
   - The data will be imported from the daily Excel records into a Pandas DataFrame. I will preprocess the data by handling missing values and standardizing units.

2. **Visualization:**  
   - Create scatter plots, heatmaps, and time series plots to visualize relationships between variables. Examples include:  
     - A scatter plot of protein intake vs. Bench Press performance  
     - A heatmap showing correlations between all variables  
     - A time series plot comparing Bench Press performance over the three months  

3. **Hypothesis Testing:**  
   - Test the following hypothesis:  
     - **H₀:** Changes in daily variables have no effect on Bench Press performance.  
     - **Hₐ:** Changes in one or more daily variables significantly impact Bench Press performance.  
   - Use regression analysis to identify which variables are the strongest predictors.  

4. **Trend Analysis:**  
   - Explore trends in performance over time and identify periods of rapid improvement or plateaus.  
   - Determine if sleep quality or a specific macronutrient consistently aligns with performance peaks.

---

## Example Analysis
An example visualization would include a scatter plot showing the relationship between protein intake and Bench Press performance. The x-axis represents protein intake (grams), while the y-axis represents Bench Press 1RM (kg). This will help identify whether higher protein consumption correlates with better performance.

---

## Conclusion
At the conclusion of the project, I aim to determine which lifestyle factors most significantly influence my Bench Press performance. Insights gained can help refine my fitness and nutrition strategies for continued improvement. This project will also serve as a practical demonstration of the application of data science in tracking and optimizing personal fitness progress.
