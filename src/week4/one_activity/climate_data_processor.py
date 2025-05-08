'''
Activity W4-1: - https://data.niwa.co.nz/pages/clidb-on-datahub
Due date : 9 May 2025 - Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis -  See Link: https://data.niwa.co.nz/pages/clidb-on-datahub
'''
import pandas as pd

class TemperatureDataSet:
    PERIOD = 'PERIOD'
    YEAR = 'YEAR'
    STATS_VALUE = 'STATS_VALUE'
    MONTH_ORDER = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # define a TemperatureDataSet class to maintain weather data from an agent of a city
    def __init__(self, file_path, city, agent, agent_no):
        self.file_path = file_path
        self.city = city
        self.agent = agent
        self.agent_no = agent_no
        self.data = None

class ClimateDataProcessor:
    # to load and compare weather data between two cities
    def __init__(self, temperature_data_set_1, temperature_data_set_2, year):
        self.temperature_data_set_1 = temperature_data_set_1
        self.temperature_data_set_2 = temperature_data_set_2
        self.year = year
        self.merged_temperature_data_frame = None

    def load_data(self):
        temperature_data_set_1 = self.temperature_data_set_1
        temperature_data_set_2 = self.temperature_data_set_2
        # to check if file format is correct
        if temperature_data_set_1.file_path.endswith('.csv') and temperature_data_set_2.file_path.endswith('.csv'):
            temperature_data_set_1.data = pd.read_csv(temperature_data_set_1.file_path)
            temperature_data_set_2.data = pd.read_csv(temperature_data_set_2.file_path)
            # to check if columns exist
            if not set([TemperatureDataSet.PERIOD, TemperatureDataSet.YEAR, TemperatureDataSet.STATS_VALUE]).issubset(temperature_data_set_1.data.columns):
                raise ValueError("Unsupported CSV columns. Columns needed: PERIOD, YEAR, STATS_VALUE.")
            # to filter the DataFrame by year
            temperature_data_set_1.data = temperature_data_set_1.data[temperature_data_set_1.data[TemperatureDataSet.YEAR] == self.year]
            temperature_data_set_2.data = temperature_data_set_2.data[temperature_data_set_2.data[TemperatureDataSet.YEAR] == self.year]
            for df in [temperature_data_set_1.data, temperature_data_set_2.data]:
                # to set PERIOD column categorical
                df[TemperatureDataSet.PERIOD] = pd.Categorical(
                    df[TemperatureDataSet.PERIOD], 
                    categories=TemperatureDataSet.MONTH_ORDER,
                    ordered=True
                )

            self.merged_temperature_data_frame = temperature_data_set_1.data.merge(temperature_data_set_2.data, 
                                                                                 how = 'outer', 
                                                                                 on = [TemperatureDataSet.PERIOD, TemperatureDataSet.YEAR], 
                                                                                 suffixes=('_' + temperature_data_set_1.city, '_' + temperature_data_set_2.city),
                                                                                 sort=False).reset_index(drop=True)
        else:
            raise ValueError("Unsupported file format. Please use CSV.")
        print(f"Data loaded successfully from {temperature_data_set_1.file_path} and {temperature_data_set_2.file_path}")

    def process_data(self):
        city1 = self.temperature_data_set_1.city
        city2 = self.temperature_data_set_2.city
        width = 25

        print(f'{'':<{width}}{city1}({self.year}{')':<{width}}{city2}({self.year})')
        for i, row in self.merged_temperature_data_frame.iterrows():
            month = row[TemperatureDataSet.PERIOD]
            year = row[TemperatureDataSet.YEAR]
            temperature1 = row[TemperatureDataSet.STATS_VALUE + '_' + city1]
            temperature2 = row[TemperatureDataSet.STATS_VALUE + '_' + city2]

            symbol = ''
            if temperature1 > temperature2:
                symbol = '>'
            elif temperature1 < temperature2:
                symbol = '<'
            elif temperature1 == temperature2:
                symbol = '='

            print(f'{month:<{width}}{temperature1:<{width}}{symbol:<{width}}{temperature2}')

def main():
    temperature_data_set_1 = TemperatureDataSet('src/week4/one_activity/41351__monthly__Mean_air_temperature__Deg_C.csv', 'Auckland', 'MOTAT EWS', '41351')
    temperature_data_set_2 = TemperatureDataSet('src/week4/one_activity/44763__monthly__Mean_air_temperature__Deg_C.csv', 'Christchurch', 'Botanic Gardens EWS', '44763')
    year = 2024
    climate_data_processor = ClimateDataProcessor(temperature_data_set_1, temperature_data_set_2, year)
    climate_data_processor.load_data()
    climate_data_processor.process_data()

if __name__ == "__main__":
    main()

