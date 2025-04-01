# Formula 1 Championship Data Analysis

## Dataset
- Source: [Kaggle - Formula 1 World Championship (1950-2020)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
- Files used: `results.csv`, `drivers.csv`, `constructors.csv`, `races.csv`, `circuits.csv`,`pit_stops.csv`,`qualifying.csv`


### 1. Top 10 Drivers by Race Wins
- **Query:** SQL used to count how many times each driver finished 1st (`positionOrder = 1`).
- **Insight:** Lewis Hamilton, Michael Schumacher, and Sebastian Vettel lead by wins.
- **Interactive Slider:** Users can filter drivers by minimum win count.

### 2. Top 10 Constructors
- Ferrari, Mercedes, McLaren dominate across eras.
- Data visualized with bar chart and table.

### 3. Most Frequent Circuits
- Silverstone, Monza, and Spa-Francorchamps have hosted the most races.
- Shown with a chart of race counts per circuit.


## Tools Used
- Preswald Studio
- Python (via `hello.py`)
- Plotly for visualizations
