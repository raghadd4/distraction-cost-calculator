# Distraction Cost Calculator
A Python-based command-line application that analyzes the real cost of distractions by weighting time wasted against task importance.
The program stores data persistently and provides summary insights such as total, average, and highest-impact distractions.

## What it does
- Allows users to enter multiple distractions
- Collects user-reported distractions
- Assigns an importance level (1–5) to each distraction
- Calculates a cost score using time × importance
- Displays a summary and total distraction cost
- Identifies the highest-cost distraction based on impact
- Handles invalid user input safely using error handling
- Stores distraction data persistently using file I/O
- Displays total, average, and highest-cost distractions


## Why this project
Time-based tracking alone doesn’t reflect real productivity loss.  
This project focuses on **impact**, not just duration.

## Technologies Used
- Python
- Functions and control flow
- Lists and dictionaries
- File I/O (persistent data storage)
- Git & GitHub (version control)

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run the program using:
   python main.py

## Example
Task name: YouTube
Importance (1–5): 3
Time wasted (minutes): 40

Task name: Instagram
Importance (1–5): 2
Time wasted (minutes): 20

Do you want to add another distraction? (y/n): n

--- Distraction Summary ---
YouTube → Cost Score: 120
Instagram → Cost Score: 40

Total Distraction Cost: 160
