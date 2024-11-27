# FitnessData-DSA210Project

## Project Overview
Over the next three months, I’ll be analyzing how my daily lifestyle choices impact my one-rep max Bench Press performance. My focus is on understanding the role of factors like caloric intake, protein, carbohydrate, and creatine consumption, as well as sleep duration and quality, in driving my strength gains. By visualizing patterns and running statistical analyses, I hope to pinpoint which of these variables have the greatest influence on my progress—and determine if tweaking them leads to measurable improvements.

To carry out this analysis, I’ll track my daily routines and intake, then evaluate how they correlate with changes in my Bench Press performance. I also plan to test hypotheses to see if specific adjustments in these areas have a statistically significant effect on my results.

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
Performance variability caused by external factors like illness or injuries will be flagged as potential outliers.

- To ensure consistency in the dependent variable, the dataset will only include days when Bench Press performance was tested.
- I’ll also record any significant changes to workout routines or nutrition plans that could influence the analysis.


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
By the end of this project, I hope to identify which lifestyle factors have the greatest impact on my Bench Press performance. The insights I gain will help me fine-tune my fitness and nutrition strategies to keep making progress. Beyond that, this project will also showcase how data science can be used to track and optimize personal fitness goals in a practical, real-world setting.
