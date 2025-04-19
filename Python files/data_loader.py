import pandas as pd  
import os  
  
class DataLoader:  
    def __init__(self, Downloads):  
        self.Downloads = Downloads 
  
    def load_data(self):  
        """  
        Load data from a given file path.  
        Returns a pandas DataFrame.  
        """  
        if not os.path.exists(self.Downloads):  
            raise FileNotFoundError("File not found: " + self.Downloads)  
        try:  
            if self.Downloads.endswith('GCST - Python.csv'):  
                df = pd.read_csv(self.file_path)  
            elif self.file_path.endswith('.xlsx'):  
                df = pd.read_excel(self.file_path)  
            elif self.file_path.endswith('.ipynb'):  
                 
                with open(self.file_path, 'r', encoding='utf-8') as f:  
                    content = f.read()  
                df = pd.DataFrame({"content": [content]})  
            else:  
                raise ValueError("Unsupported file format")  
              
            if isinstance(df, pd.DataFrame):  
                df.columns = [c.strip() for c in df.columns]  
            return df  
        except Exception as e:  
            raise ValueError("Error loading data: " + str(e))  
  
if __name__ == "__main__":  
    print("Testing DataLoader")  
    loader = DataLoader("Downloads")  
    try:  
        df = loader.load_data()  
        print("Data Loaded Successfully")  
    except Exception as error:  
        print("Error:", error)  