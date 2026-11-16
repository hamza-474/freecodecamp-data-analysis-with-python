# freeCodeCamp — Data Analysis with Python Projects

These are Hamza Madni's five projects for the [freeCodeCamp Data Analysis with Python Developer Certification](https://www.freecodecamp.org/certification/fcc-e2b594ad-6279-46f6-b5e7-f344e25e0c82/data-analysis-with-python-v7).

## Projects

| Project | File | What it does |
| --- | --- | --- |
| Mean-Variance-Standard Deviation Calculator | `mean_var_std.py` | Calculates the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix, row-wise, column-wise, and overall, using NumPy. |
| Demographic Data Analyzer | `demographic_data_analyzer.py` | Analyzes the UCI Adult census dataset with Pandas — demographics, education, income, occupations, and countries. |
| Medical Data Visualizer | `medical_data_visualizer.py` | Builds a categorical plot and a correlation heatmap from medical examination data with Seaborn and Matplotlib. |
| Page View Time Series Visualizer | `time_series_visualizer.py` | Draws line, bar, and box plots of freeCodeCamp forum page views over time. |
| Sea Level Predictor | `sea_level_predictor.py` | Plots historical sea-level data and two lines of best fit predicting the rise through 2050. |

> **Note:** `demographic_data_analyzer.py` is not in this repository yet — its OneCompiler source link (https://onecompiler.com/python/459c9g4xr) returns "Not Found", so the code could not be copied. Its dataset (`data/adult.data.csv`) is already included, so the file can be added once the source is available.

## Datasets

The datasets live in `data/` (offline copies from freeCodeCamp's official boilerplate repositories):

| Dataset | Used by |
| --- | --- |
| `data/adult.data.csv` | Demographic Data Analyzer |
| `data/medical_examination.csv` | Medical Data Visualizer |
| `data/fcc-forum-pageviews.csv` | Page View Time Series Visualizer |
| `data/epa-sea-level.csv` | Sea Level Predictor |

`mean_var_std.py` needs no data file.

## Skills and tools

Python, Pandas, NumPy, Matplotlib, Seaborn (and SciPy for the sea-level regression).

## How to run

```bash
git clone https://github.com/hamza-474/freecodecamp-data-analysis-with-python.git
cd freecodecamp-data-analysis-with-python
pip install pandas numpy matplotlib seaborn scipy
python mean_var_std.py
python medical_data_visualizer.py
python time_series_visualizer.py
python sea_level_predictor.py
```

Each script loads its dataset from a local copy first — a CSV sitting next to the script, or the copy in `data/` — and otherwise downloads it automatically from the official freeCodeCamp dataset URL, so the projects run anywhere with an internet connection.

## Data-loading fix

The original project code reads its CSV from a file next to the script, which does not exist in online sandboxes such as OneCompiler, so running the code there fails with a file-not-found error. In this repository, each data-loading line was changed to a robust fallback: use the local file if it exists (next to the script or in `data/`), otherwise download the dataset from the official freeCodeCamp URL. No other logic was changed — the code is otherwise exactly as submitted to freeCodeCamp. The OneCompiler copies remain view-only because that sandbox has no data files.

## Certificate

[Data Analysis with Python (v7) — freeCodeCamp certification](https://www.freecodecamp.org/certification/fcc-e2b594ad-6279-46f6-b5e7-f344e25e0c82/data-analysis-with-python-v7)
