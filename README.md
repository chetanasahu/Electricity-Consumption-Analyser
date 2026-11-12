# Electricity Consumption Analyzer

A Python-based project that analyzes monthly electricity consumption
data from CSV files using **Pandas**, **NumPy**, and **Matplotlib**. It
calculates statistical measures, identifies the highest- and
lowest-consumption months, detects months above average, and visualizes
consumption trends.

------------------------------------------------------------------------

## Student Details

  Field                       Details
  --------------------------- ----------------------------------------
  **Name**                    Chetana Sahu
  **ERP No.**                 RU-26-01354
  **Programme**               Bachelor of Computer Application (BCA)
  **Semester**                1st Semester
  **Section**                 1C
  **Project Statement No.**   22
  **Project Title**           Electricity Consumption Analyzer

## Project Mentor

**Mentored by:** [Mr. Satyaprakash
Sethy](https://github.com/SATYAPRAKASHSETHY)\
**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)\
**Role:** Python Mentor / Technical Guide

------------------------------------------------------------------------

## 1. Project Overview

The Electricity Consumption Analyzer analyzes monthly electricity usage
recorded in CSV files. The program reads the data, checks and handles
invalid entries, and uses numerical calculations to summarize
electricity consumption.

The project supports four separate test cases. Each test case has its
own CSV file, allowing the user to test normal input, minimum input,
invalid input, and another valid scenario without repeatedly editing a
single CSV file.

For the fourth test case, the program identifies months whose
consumption is above the average and displays graphical representations
of the data.

## 2. Project Objectives

-   To read monthly electricity consumption data from CSV files.
-   To use Pandas for loading and handling tabular data.
-   To use NumPy to calculate statistical values.
-   To identify the months with the highest and lowest electricity
    consumption.
-   To find months with consumption above the average.
-   To handle invalid or negative unit values.
-   To visualize monthly consumption using Matplotlib bar and line
    charts.
-   To test the program using all four given test cases.

## 3. Features

-   **CSV File Handling:** Reads data from four separate CSV files.
-   **Input Validation:** Detects invalid and negative electricity
    consumption values.
-   **Statistical Analysis:** Calculates total, average, maximum,
    minimum, and population standard deviation.
-   **Highest and Lowest Consumption:** Identifies the months with the
    highest and lowest usage.
-   **Above-Average Analysis:** Finds months with consumption greater
    than the average.
-   **Data Visualization:** Displays a bar chart and a line chart for
    monthly consumption.
-   **Multiple Test Cases:** Allows the user to select any of the four
    test cases using a number.

## 4. Technologies and Requirements

### Programming Language

-   Python 3

### Libraries Used

  Library          Purpose
  ---------------- -------------------------------------------------
  **Pandas**       Reading and handling CSV data
  **NumPy**        Numerical calculations and statistical analysis
  **Matplotlib**   Creating bar and line charts

### Software Requirements

-   Python 3 installed on the computer.
-   Visual Studio Code (VS Code) or another Python-supported editor.
-   The required Python libraries installed.
-   All project files stored in the same folder.

## 5. Project File Structure

Keep the following files together in one project folder:

``` text
Electricity Analyser/
│
├── one.py
├── usage_test1.csv
├── usage_test2.csv
├── usage_test3.csv
└── usage_test4.csv
```

  File                Description
  ------------------- --------------------------
  `one.py`            Main Python program
  `usage_test1.csv`   CSV data for Test Case 1
  `usage_test2.csv`   CSV data for Test Case 2
  `usage_test3.csv`   CSV data for Test Case 3
  `usage_test4.csv`   CSV data for Test Case 4

## 6. CSV Input Format

Each CSV file contains two columns:

  Column    Description
  --------- ----------------------------------
  `Month`   Name or label of the month
  `Units`   Electricity consumption in units

Example:

``` csv
Month,Units
Jan,200
Feb,250
Mar,300
```

The four CSV files contain the input data specified in the given project
test cases.

## 7. Installation Instructions

Open the VS Code terminal in the project folder and install the required
libraries:

``` bash
pip install pandas numpy matplotlib
```

These libraries only need to be installed once in the Python environment
being used.

## 8. Execution Instructions

1.  Open the `Electricity Analyser` project folder in Visual Studio
    Code.

2.  Open the `one.py` file.

3.  Open the integrated terminal.

4.  Run the program using:

    ``` bash
    python one.py
    ```

5.  When the program waits for input, enter the required test case
    number.

### Test Case Selection

  User Input   CSV File            Test Case
  ------------ ------------------- --------------------------
  `1`          `usage_test1.csv`   Normal Input
  `2`          `usage_test2.csv`   Boundary / Minimum Input
  `3`          `usage_test3.csv`   Invalid Input
  `4`          `usage_test4.csv`   Different Valid Scenario

Run `python one.py` again to execute another test case if the program
has finished.

## 9. Test Cases and Expected Results

### Test Case 1: Normal Input

**Input file:** `usage_test1.csv`

  Month     Units
  ------- -------
  Jan         200
  Feb         250
  Mar         300

**Expected output:**

``` text
Total: 750 units | Average: 250.00
Highest: Mar (300) | Lowest: Jan (200)
Std Dev: 40.82
```

### Test Case 2: Boundary / Minimum Input

**Input file:** `usage_test2.csv`

  Month     Units
  ------- -------
  Jan         150

**Expected output:**

``` text
Total: 150 units | Average: 150.00
Highest: Jan (150) | Lowest: Jan (150)
Std Dev: 0.00
```

### Test Case 3: Invalid Input

**Input file:** `usage_test3.csv`

  Month     Units
  ------- -------
  Jan         200
  Feb         abc
  Mar         -30

**Expected output:**

``` text
Row 2 skipped: invalid Units 'abc'.
Row 3 skipped: Units cannot be negative.
Valid rows: 1 | Total: 200 units
```

### Test Case 4: Different Valid Scenario

**Input file:** `usage_test4.csv`

This test case uses the same valid data as Test Case 1.

**Expected output:**

``` text
Months above average (250.00): Mar (300)
Bar chart 'Monthly Consumption' displayed
```

The program also displays the line chart titled **Monthly Consumption
Trend**.

## 10. Statistical Calculations

The program uses NumPy to calculate:

-   **Total:** Sum of all valid electricity consumption values.
-   **Average:** Mean of the valid consumption values.
-   **Highest:** Maximum consumption value.
-   **Lowest:** Minimum consumption value.
-   **Standard Deviation:** Population standard deviation, using NumPy's
    default `np.std()` calculation.

Invalid and negative unit values are excluded from the valid data used
for calculations.

## 11. Data Visualization

For Test Case 4, the program creates two charts:

1.  **Bar Chart -- Monthly Consumption:** Compares electricity
    consumption across the months.
2.  **Line Chart -- Monthly Consumption Trend:** Shows the change in
    electricity consumption across the months.

Both charts include suitable titles and axis labels.

## 12. Conclusion

The Electricity Consumption Analyzer demonstrates how Python libraries
can be used to read, validate, analyze, and visualize data. It applies
Pandas for CSV handling, NumPy for statistical calculations, and
Matplotlib for graphical representation. The four test cases demonstrate
the program's ability to process normal, minimum, invalid, and different
valid input scenarios.

------------------------------------------------------------------------

**Submitted by:** Chetana Sahu\
**ERP No.:** RU-26-01354\
**BCA -- 1st Semester, Section 1C**
