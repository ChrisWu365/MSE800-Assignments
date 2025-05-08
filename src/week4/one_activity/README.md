# Temperature processing activity
This repository contains solutions to compare the temperature between two cities based on the CSV files download from https://data.niwa.co.nz/pages/clidb-on-datahub.

## Activity 1: Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis( climate_data_processor.py )
### Classes
#### 1. TemperatureDataSet Class
Represents a temperature data set loaded from CSV file with:
- Attributes: file_path, city, agent, agent_no

#### 2. ClimateDataProcessor Class
Process the temperature data of two cities in a given year with:
- Attributes: temperature_data_set_1, temperature_data_set_2, year
- Methods:
    - load_data(self): Loads data from CSV file
    - process_data(self): Compare the temperature between two cities

### How to run
Run the program using Python: 
```
python climate_data_processor.py
```