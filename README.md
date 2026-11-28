
# BurnFluid — Burn Fluid Resuscitation Support Tool

## 1. Project Information

- Course: HIM 2213 — Intermediate Programming
- Semester: Fall 202610
- CRN: 12794
- Project Type: Python Console Application
- Team Members: Bothainah Mohamed and Shamma
- Development Environment: GitHub Codespaces
- Version Control: GitHub

## 2. Project Overview

BurnFluid is a Python-based educational console application designed to simulate burn fluid estimation for fictional adult patients with major burns.

The project demonstrates how programming concepts can be applied to healthcare-related calculations, input validation, structured data management, and educational safety alerts.

## 3. Problem and Purpose

Manual burn fluid calculations may involve calculation errors, inconsistent measurement units, and confusion regarding the time elapsed since injury.

BurnFluid aims to demonstrate how a structured software application can simplify educational calculations, reduce input errors, and organize fictional patient information.

## 4. Intended Users

The intended users in the simulated healthcare scenario are:

- Emergency Department physicians
- Emergency Department nurses
- Burn Unit healthcare professionals
- Healthcare students

The application is designed for educational simulation only.

## 5. Main Features

### Implemented Calculation Features

- Fictional adult patient data collection
- Patient input validation
- Educational first 24-hour fluid estimation
- Fluid administration phase identification
- Remaining phase volume calculation
- Remaining phase time calculation
- Educational hourly fluid estimation
- Unknown fluid phase detection
- Fluid phase mismatch detection
- Excess recorded fluid volume detection
- Educational inhalation injury alerts
- Floating-point boundary protection
- Formatted console results display

### Planned Record Management Features

- Save fictional patient records
- Load previously saved records
- View saved records
- Search by fictional Emirates ID
- Sort records by TBSA percentage
- Duplicate record detection

Record management and full application integration are pending final verification.

## 6. Project File Structure

| File | Purpose | Status |
|---|---|---|
| burn_calculations.py | Patient input, validation, calculations, alerts, and results display | Implemented and individually tested |
| record_manager.py | Fictional patient record management | Pending final verification |
| main.py | Main menu and module integration | Pending integration |
| burn_records.csv | Planned fictional patient data storage | Pending integration |
| prompt_log.txt | AI prompt summaries and development outcomes | Individual section uploaded |
| README.md | Project documentation | In progress |

## 7. How to Run

### Individual Calculation Module

Python 3 is required.

Run the following command in the terminal:

    python burn_calculations.py

Follow the console instructions and enter fictional patient information only.

### Full Application

The planned entry point for the integrated application is:

    python main.py

Full application execution will be verified after module integration.

## 8. Required Programming Concepts

The project is designed to demonstrate the following required programming concepts:

| Programming Concept | Implementation Area |
|---|---|
| Variables and data types | Fictional patient information and calculation values |
| Strings and string methods | Patient information and input processing |
| Conditional statements | Input validation, phase identification, and review conditions |
| For and while loops | Input validation, alerts, and planned record processing |
| Lists | Educational alerts and planned patient records |
| Dictionaries | Structured patient data and calculation results |
| Functions with parameters and return values | Modular calculation and record management functions |
| Try and except | Invalid input and planned file error handling |
| File handling | Planned CSV record storage and retrieval |

The final concept mapping, including verified filenames and function names, will be completed after reviewing both modules.

## 9. Main Calculation Functions

| Function | Purpose |
|---|---|
| collect_patient_data() | Collects and validates fictional patient information |
| estimate_burn_fluids() | Performs educational fluid estimation and phase calculations |
| generate_safety_alerts() | Generates educational alerts based on patient information and calculation results |
| display_estimation_results() | Displays structured educational results |
| is_at_or_below_classroom_time_threshold() | Handles numerical boundary comparisons |

## 10. Advanced Programming Concepts

The planned advanced programming concepts include:

- Sets for duplicate record detection
- Searching for fictional patient records
- Sorting records by TBSA percentage

The final implementation and function locations will be verified after completing the record management module.

## 11. Team Contributions

### Bothainah Mohamed — Team Leader

GitHub Username: bothainah506

Responsibilities:

- Patient input and validation
- Educational burn fluid calculation logic
- Educational safety alerts
- Floating-point boundary debugging
- Formatted results display
- Individual module testing
- GitHub repository coordination
- Main menu and final integration

### Shamma — Team Member

Responsibilities:

- Fictional patient record management
- CSV file handling
- Record searching and sorting
- Duplicate record detection
- Individual module testing

Final contributions will be updated after integration.

## 12. Testing and Debugging

The burn calculation module was tested using eight fictional patient scenarios.

| Test | Scenario | Result |
|---|---|---|
| 01 | Valid first-phase calculation | Pass |
| 02 | Invalid input and recovery | Pass |
| 03 | Unknown fluid phase | Pass |
| 04 | Fluid phase mismatch | Pass |
| 05 | Excess recorded fluid volume | Pass |
| 06 | Inhalation injury alert | Pass |
| 07 | Valid second-phase calculation | Pass |
| 08 | Time boundary and numerical safeguard | Pass |

Individual module testing results:

- Total tests: 8
- Passed: 8
- Failed: 0

A floating-point precision issue was addressed using math.isclose() to improve numerical boundary handling.

Exact boundary verification and integrated application testing remain pending.

## 13. AI-Assisted Development

ChatGPT and GitHub Copilot were used to support development, debugging, and documentation.

The AI-assisted development process is documented in prompt_log.txt.

AI-generated suggestions are reviewed and tested before being accepted.

## 14. Educational Disclaimer

BurnFluid is an educational simulation tool and is not intended for clinical use.

The illustrative calculations, educational alerts, and numerical safeguards must not be interpreted as clinical treatment recommendations.

The application does not replace professional clinical judgment or approved hospital treatment protocols.

All patient information must be fictional.

## 15. Project Status

Development in progress.

The calculation module has been implemented and individually tested. Record management, full application integration, and final system verification are pending.
