# Carbon Footprint Estimator

## Overview
The Carbon Footprint Estimator is a minimalist command-line application designed to provide users with a quick, simplified estimate of their personal annual carbon footprint (CO2e) based on common activities like home energy consumption, vehicle usage, and air travel.

This project focuses on applying fundamental programming concepts, data structures (dictionaries), modular design (functions), and effective error handling in a real-world context focused on environmental sustainability.

## Features
- **Annualized Calculation**: Converts monthly input values (e.g., electricity, fuel) into annual estimates for a comprehensive report.
- **Modular Input Handling**: Utilizes a dedicated function to robustly handle user input, ensuring only positive numerical values or explicit 'no' responses are accepted.
- **Emission Factor Storage**: Uses a dictionary (`FACTORS`) to store CO2 equivalent (CO2e) emission rates, making factors easy to view and update.
- **Stylized Reporting**: Presents the total annual footprint and a detailed category breakdown (Electricity, Vehicle Fuel, Flights) in a clear, formatted console report.
- **Contextual Feedback**: Provides a simple, humanized sustainability rating based on the calculated total footprint compared to global averages.

## Technologies/Tools Used

| Category     | Tool / Language                  | Purpose                                                                 |
|--------------|----------------------------------|-------------------------------------------------------------------------|
| Language     | Python 3.6+                      | Core programming language for logic and execution.                      |
| Modules      | Standard Library (csv module for loading factors) | Focuses on core concepts and basic file I/O.                            |

Since this is a single, self-contained Python script, setup is straightforward.

## Steps to Install & Run the Project

### Prerequisites
- You must have Python 3.6+ installed on your system.

### Running Instructions
1. **Save the Code**: Save the Python code (the main application script) into a file named `carbon_estimator.py`.
2. **Execute the Script**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

   python carbon_estimator.py

3. **Follow Instructions**: The application will ask you to enter your average monthly or annual consumption for the three categories. Enter a numerical value (e.g., `500` for 500 kWh) or type `no` or `n` to skip a category.

## Instructions for Testing

The application relies on internal logic checks and user input validation to ensure stability.

### Input Testing
Test the robustness of the function by entering the following inputs:

| Input   | Expected Behaviour                                                                 |
|---------|------------------------------------------------------------------------------------|
| `120.5` | Accepts the float value and continues.                                             |
| `no` or `n` | Returns `0.0` and continues.                                                       |
| `-50`   | Rejects the negative number and asks to try again.                                 |
| `abc`   | Displays the error message `"Oops! Please enter a number or 'no'."` and retries.   |

### Calculation Validation
Verify the core arithmetic by manually calculating a simple scenario:

**Scenario:**
- Monthly Electricity: 100 kWh
- Monthly Fuel: 0 Litres
- Annual Flights: 0 km

**Expected Calculation:**
- Total (g CO2e) = (100 kWh/month * 12 months) * 450 g/kWh = 540,000 g
- Total (kg CO2e) = 540 kg CO2e

**Test Result**: Run the script with these inputs and confirm the final Grand Total matches **540 kg CO2e**.


## Usage
Copy the Markdown above into a file named `README.md` in your GitHub repository root. This will render beautifully on GitHub with proper tables, lists, code blocks, and formatting. If you have the actual Python script (`carbon_estimator.py`), commit it alongside this README for a complete repo!
