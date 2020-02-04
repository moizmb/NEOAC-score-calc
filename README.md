# NEOAC-score-calc
NEO 5 Factor inventory profile calculator

# Setup
Requires python 3. No external pip dependencies

# Data folders
The responses are stored in `data/Male` and `data/Female` for male and female responses respectively. Excel files are named by the convention `ID_initials_age_education_occupation.xlsx`.

The 3 test scores are saved in 3 tabs in the excel sheet.
- Tab named Sheet1 must contain the Internet Addiction Test with 20 responses
- Tab named Sheet2 must contain the Psychological Entitlement Scale with 9 responses
- Tab named Sheet3 must contain the NEO 5 factor inventory profile with 60 responses

All responses must be in the 1st column with the first response on the first row and so on

# Results
Results can be calculated by running

```python
python app.py
```

This generates 2 files called `male.csv` and `female.csv` in `data/Results`.
