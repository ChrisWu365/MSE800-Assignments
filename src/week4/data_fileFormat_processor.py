import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        file_path = self.file_path
        if file_path.endswith('.csv'):
            self.data = pd.read_csv(file_path)
        elif file_path.endswith('.txt'):
            self.data = pd.read_table(file_path, header=None)
        elif file_path.endswith('.parquet'):
            self.data = pd.read_parquet(file_path)
        elif 'cifar10' in self.file_path:
            self.data = tf.keras.datasets.cifar10.load_data()
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")

    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        if 'cifar10' in self.file_path:
            (x_train, y_train), (x_test, y_test) = self.data
            print(x_train.shape)
            print(y_train.shape)
            print(x_test.shape)
            print(y_test.shape)
        else:
            print("Initial Data Summary:")
            print(self.data.info())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.data.describe())

    def process_data(self):
        if 'cifar10' in self.file_path:
            (x_train, y_train), (x_test, y_test) = self.data
            # show the first n_rows * n_cols images of train dataset
            n_rows = 4
            n_cols = 8
            plt.figure(figsize=(n_cols * 2, n_rows * 2))
            for row in range(n_rows): # loop row
                for col in range(n_cols): # loop column
                    index = n_cols * row + col
                    plt.subplot(n_rows, n_cols, index + 1) # to generate n_rows and n_cols images, this is the (index + 1)th image
                    plt.imshow(x_train[index], cmap="binary", interpolation="nearest")
                    plt.axis('off')

            plt.subplots_adjust(wspace=0.2, hspace=0.5) # to adjust layout
            plt.show()
        else:
            print(self.data)

def main():
    
    # file_path = 'src/Week4/sample_junk_mail.csv'
    # file_path = 'src/Week4/sample_text.txt' 
    # file_path = 'src/Week4/Sample_data_2.parquet' 
    file_path = 'cifar10'
    processor = DataFileFormat_Processor(file_path)
    processor.load_data()
    processor.initial_processing()
    processor.process_data()

if __name__ == "__main__":
    main()
