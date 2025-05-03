'''
Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
Note: You must have main function
Write a full project to do the data file processing for csv, text and etc. file formats.
'''
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_first_line(self):
        infile = open(self.file_path, 'r')
        first_line = infile.readline()
        infile.close()
        print(first_line)
        return first_line
    
def main():
    print('This is main function')
    file_processor = FileProcessor('src/week4/sample_text.txt')
    file_processor.read_first_line()

if __name__ == '__main__':
    main()