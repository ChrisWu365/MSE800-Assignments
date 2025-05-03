import pandas as pd
data_frame = pd.read_table('src/week4/sample_text.txt', header=None)
print(f'First line: {data_frame.head(1).to_string()}')
print('Last line: ', data_frame.tail(1).to_string())