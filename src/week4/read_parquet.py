import pandas as pd
data_frame = pd.read_parquet('src/week4/Sample_data_2.parquet')
print(data_frame.shape)
print('Available records: ', len(data_frame))