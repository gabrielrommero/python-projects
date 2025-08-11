# Student Grade Calculator

This Python program collects a student’s full name, three exam scores, and attendance percentage. It:

- Validates that scores are between 0 and 100
- Calculates the average score and GPA
- Determines the final letter grade based on scores and attendance
- Extracts and displays the student’s name initials

## How to Run

Clone the repository:

   ```bash
git clone https://github.com/gabrielrommero/python-projects.git
cd python-projects
python grade-calculator.py
```

Example Output
````
Full name: John Smith
Score 1st Exam: 80
Score 2nd Exam: 75
Score 3rd Exam: 90
Attendance Percentage: 85
Average = 81.66666666666667
Initial: JS
SMITH
Grade: B
GPA: 3.2666666666666666
````
# Weather Data Analyzer
This Python program generates simulated daily temperature and rainfall data for 30 days, then analyzes it to:

- Identify days with the highest and lowest temperatures
- List days with temperatures above 20°C and below 10°C
- Track days where temperature increased compared to the previous day
- Detect days hotter than all previous days
- Count days with bad, average, and good weather based on temperature and rainfall thresholds

## How to Run

```bash
git clone https://github.com/gabrielrommero/python-projects.git
cd python-projects
python weather-analysis.py
```
Example Output
```csharp
[17, 35, 4, 9, 33, 34, 6, 35, 1, 32, 23, 5, 8, 3, 15, 30, 3, 33, 32, 10, 33, 16, 6, 30, 35, 25, 6, 15, 9, 33]
The day 2 presented the highest temperature, hiting a peak of 35 Cº.
The day 8 presented the highest temperature, hiting a peak of 35 Cº.
The day 9 presented the lowest temperature, marking the a minimum of 1 Cº.
The day 25 presented the highest temperature, hiting a peak of 35 Cº.
The following days had temperatures higher than 20Cº:  [2, 5, 6, 8, 10, 11, 16, 18, 19, 21, 24, 25, 26, 30]
The following days presented temperatures lower than 10Cº: [3, 4, 7, 9, 12, 13, 14, 17, 23, 27, 29]
Temperature increased on the following days:  [2, 4, 5, 6, 8, 10, 13, 15, 16, 18, 21, 24, 25, 28, 30]
Days hotter than the previous: [2, 5, 6, 8, 10, 11, 16, 18, 19, 21, 24, 25, 26, 30]
[4, 4, 2, 7, 6, 10, 10, 2, 5, 4, 4, 6, 7, 2, 9, 3, 2, 7, 3, 5, 8, 10, 5, 10, 9, 1, 9, 9, 4, 6]
Days with Bad Weather:  8
Days with Average Weather:  0
Days with Bad Weather:  1
```

# Patient Record Management
This Python program manages patient health data including:

Personal info (name, age, gender)

Diagnoses, medications, allergies

Blood pressure tracking and average calculations

Appointment dates handling

Medication addition/removal with allergy checks

## How to Run
```bash
git clone https://github.com/gabrielrommero/python-projects.git
cd python-projects
python doctor-interface.py

Example Output
```
Enter Patient ID or 'exit': P12345
John Doe , 35 , Male
Diagnosis:  Hypertension
Medications:  2 ['Lisinopril', 'Hydrochlorothiazide']
Allergies:  1 ['Penicillin']
Average Blood Pressure:  135.5 , 89.75
Patient's Blood Pressure is High.
2022-05-20 00:00:00
2023-11-15 00:00:00
544 days, 0:00:00
...
```
