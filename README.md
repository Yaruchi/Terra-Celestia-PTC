# Terra-Celestia-Planetary-Time-Converter

## Introduction
The **Planetary Time Converter** is a tool designed to calculate and display time conversions across different planets in a fictional planetary system. Each planet has its unique rotation period, calendar system, and time divisions. This program allows users to input time values based on a selected planet and receive converted time values for other planets in the system.

## Features
- Convert time across multiple planets with unique rotational periods.
- Input time values in years, months, weeks, days, hours, minutes, and seconds.
- Display converted time for all planets in a structured format.
- Shows time-of-day phases (Morning, Noon, Afternoon, Evening, Midnight) based on planetary rotation.
- Graphical User Interface (GUI) for user-friendly interaction.

## Planetary Time System
Each planet follows a unique time system, including:

| Planet  | Hours per Day | Days per Week | Days per Month | Months per Year | Days per Year |
|---------|-------------|--------------|--------------|---------------|--------------|
| Ignis   | 15          | 6            | 30           | 5             | 150          |
| Pyros   | 19          | 6            | 30           | 8             | 240          |
| Eos     | 24          | 6            | 30           | 12            | 360          |
| Astraea | 24          | 6            | 30           | 15            | 450          |
| Cryon   | 34          | 6            | 30           | 20            | 600          |
| Glacius | 42          | 6            | 30           | 26            | 780          |

## Usage
1. Select a base planet from the dropdown menu.
2. Enter the time values (Years, Months, Weeks, Days, Hours, Minutes, Seconds).
3. Click the **Convert** button.
4. View the converted time across all planets in the result box.

## Time of Day Calculation
Since each planet has a different rotational period, the program determines time-of-day phases as follows:

- **Midnight** (0% - 20% of the planetary day cycle)
- **Morning** (20% - 40%)
- **Noon** (40% - 60%)
- **Afternoon** (60% - 80%)
- **Evening** (80% - 100%)

## License
This project is open-source. Feel free to modify and enhance as needed.
