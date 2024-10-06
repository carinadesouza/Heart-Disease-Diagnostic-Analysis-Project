# Heart Disease Analysis Project

## Overview

This project is part of my internship at **Unified Mentors**. The project focuses on analyzing heart disease data using Python and visualizing key insights through a Tableau dashboard. The analysis includes exploratory data analysis (EDA), data cleaning, data preprocessing, and visualization of key indicators related to heart disease.

## Internship

As part of my internship at **Unified Mentors**, I am responsible for conducting data analysis projects that contribute to meaningful healthcare insights. This project is one of the key deliverables during my internship and aims to provide valuable analysis on heart disease data using modern data science techniques.

## Dataset Overview

The dataset used in this project contains various medical attributes of patients, focusing on their health conditions related to heart disease. The key attributes are:

- **age**: Age of the patient
- **sex**: Sex of the patient (1 = male, 0 = female)
- **cp**: Chest pain type (4 types: 0, 1, 2, 3)
- **trestbps**: Resting blood pressure (in mm Hg)
- **chol**: Serum cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results (values 0, 1, 2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: The slope of the peak exercise ST segment
- **ca**: Number of major vessels (0-3) colored by fluoroscopy
- **thal**: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
- **target**: Presence of heart disease (0 = no, 1 = yes)

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Tableau

## Data Cleaning

The following data cleaning steps were performed on the dataset:

1. **Duplicate Removal**: Checked for and removed duplicate entries in the dataset.
2. **Handling Missing Values**: Identified and handled missing values appropriately to ensure the integrity of the dataset.
3. **Data Type Conversion**: Converted categorical columns to numeric data types where necessary (e.g., converting the 'sex' column to integer).
4. **Categorical Encoding**: Created categorical variables (e.g., Age Groups) from continuous variables to aid in analysis.

## EDA Insights

### Age Distribution

The age distribution of patients with heart disease is visualized, indicating which age groups are most affected.

### Heart Disease Occurrence

The total cases and percentage breakdown of heart disease occurrences are displayed to provide a clear overview of the situation.

### Gender Analysis

The proportion of males vs. females diagnosed with heart disease is analyzed and visualized.

### Key Indicators

- **Cholesterol Levels**: Distribution of serum cholesterol levels among patients.
- **Blood Pressure**: Overview of resting blood pressure levels in the dataset.

### Main Insights

- **Gender Distribution**: A higher proportion of males are diagnosed with heart disease compared to females.
- **Age Group Insights**: The most affected age group is between 50-60 years.
- **Chest Pain Analysis**: Typical angina is the most reported type of chest pain.
- **Cholesterol and Blood Pressure**: Higher cholesterol and blood pressure levels correlate with an increased risk of heart disease.

### Key Takeaways

- Males are at greater risk of developing heart disease; older age groups show a higher prevalence of the condition.
- Key risk factors for heart disease include the type of chest pain reported, elevated cholesterol levels, and high blood pressure.

## Tableau Dashboard

The Tableau dashboard visualizes the findings from the analysis. It includes the following key sections:

- **Age Distribution**: Shows the age range of patients with heart disease.
- **Heart Disease Occurrence**: Displays total cases and percentage breakdown.
- **Gender Analysis**: Visualizes the proportion of males vs. females diagnosed.
- **Key Indicators**: Cholesterol levels and blood pressure distributions.

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/carinadesouza/heart-disease-analysis.git
   ```
2. Navigate to the project directory:
  ```bash
  cd heart-disease-analysis
 ```
3. nstall the required packages:
```bash
 pip install -r requirements.txt
 ```
4. Run the analysis script:
 ```bash
 python heart_disease_analysis.py
```
5. Open the Tableau dashboard to visualize the results.

## Internship Acknowledgment

This project was completed as part of my internship at Unified Mentors. I would like to extend my gratitude to the mentors and the entire team for their guidance and support throughout the development of this project.

## Conclusion

This project highlights the critical insights derived from heart disease data, aiding in understanding risk factors and facilitating better healthcare decisions.

