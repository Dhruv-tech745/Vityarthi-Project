
# Project Statement: Carbon Footprint Estimator

## Problem Statement
The general public often lacks a simple, accessible tool to quickly understand and quantify their personal contribution to carbon emissions. Many existing carbon footprint calculators are overly complex, require extensive data input, or are hidden behind paywalls. This lack of clear, immediate feedback makes it difficult for individuals to identify their most impactful areas for reduction (e.g., electricity, driving, or flying).

The problem addressed is the need for a simple, focused, and free command-line application that provides an understandable annual carbon footprint estimate based on common consumption metrics, thereby empowering users with awareness.

## Scope of the Project
The scope of this initial command-line application is strictly limited to the following key annual emission sources:
1. **Home Energy**: Calculating CO2e from monthly electricity consumption.
2. **Transportation**: Calculating CO2e from monthly vehicle fuel consumption.
3. **Air Travel**: Calculating CO2e from annual flight distance.

The project will **not** include calculations for emissions related to food consumption, waste generation, purchasing habits (embodied carbon), or public transport. It is designed to be a minimalist proof-of-concept focused on core calculation logic, user input handling, and clear reporting.

## Target Users
The primary target users for the Carbon Footprint Estimator are:
- **Students/Academics**: Individuals interested in applying mathematical and computational models to real-world sustainability issues.
- **Eco-Conscious Individuals**: People seeking a quick, numerical estimate of their environmental impact without needing an elaborate web-based tool.
- **Developers/Learners**: Users who want to review or modify a simple, well-structured Python script focused on modular programming and data handling.

## High-Level Features
- **Guided Input**: User-friendly prompts guide the user through entering consumption data.
- **Automated Annualization**: All monthly inputs are automatically multiplied by 12 to generate a full annual figure.
- **Real-Time Breakdown**: The application provides a clear, calculated breakdown of emissions per category.
- **Final Report**: A summary report displays the total estimated annual footprint in kilograms (kg) and tonnes.
- **Feedback Mechanism**: A simple textual message provides context and feedback on the calculated footprint (e.g., "Doing Great!" or "Needs control on usage").



