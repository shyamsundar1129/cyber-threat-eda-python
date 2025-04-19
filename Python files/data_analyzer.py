import pandas as pd  
  
class DataAnalyzer:  
    def __init__(self, dataframe):  
        self.df = dataframe  
  
    def basic_statistics(self):  
        try:  
            stats = self.df.describe()  
            print("Basic statistics calculated:")  
            print(stats)  
            return stats  
        except Exception as e:  
            print("Error calculating statistics:", e)  
            return None  
  
    def analyze_by_year(self):  
        try:  
            analysis = self.df.groupby('Year').agg({'FinancialLoss': 'sum',   
                                                      'NumberofAffectedUsers': 'sum'})  
            print("Yearly analysis completed:")  
            print(analysis)  
            return analysis  
        except Exception as e:  
            print("Error in analysis by year:", e)  
            return None  
  
def run():  
      
    from data_processor import DataProcessor  
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
  
    analyzer = DataAnalyzer(df)  
    analyzer.basic_statistics()  
    analyzer.analyze_by_year()  
  
if __name__ == "__main__":  
    run()  