import pandas as pd  
  
class DataProcessor:  
    def __init__(self, filepath):  
        self.filepath = filepath  
        self.df = None  
  
    def load_data(self):  
        try:  
            self.df = pd.read_csv(self.filepath)  
            print("Data loaded successfully.")  
        except Exception as e:  
            print("Error loading data:", e)  
        return self.df  
  
    def clean_data(self):  
        if self.df is None:  
            print("No data loaded. Call load_data() first.")  
            return None  
          
        self.df.dropna(subset=['Country'], inplace=True)  
        self.df.columns = [col.strip() for col in self.df.columns]  
        print("Data cleaned successfully.")  
        return self.df  
  
    def get_data(self):  
        return self.df  
  
def run():  
    
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
    print("DataProcessor module executed. Here's the head of the cleaned dataframe:")  
    print(df.head())  
  
if __name__ == "__main__":  
    run()  