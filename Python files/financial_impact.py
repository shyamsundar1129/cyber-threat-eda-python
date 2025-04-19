import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  
  
class FinancialImpact:  
    def __init__(self, dataframe):  
        self.df = dataframe  
  
    def impact_by_industry(self):  
        try:  
            impact = self.df.groupby('TargetIndustry')['FinancialLoss'].sum().reset_index()  
            print("Financial impact computed by target industry:")  
            print(impact)  
            plt.figure(figsize=(12, 6))  
            sns.barplot(data=impact, x="TargetIndustry", y="FinancialLoss")  
            plt.title("Total Financial Loss by Industry")  
            plt.xticks(rotation=45)  
            plt.tight_layout()  
            plt.show()  
            print("Impact by industry plot displayed successfully.")  
        except Exception as e:  
            print("Error in financial impact analysis:", e)  
  
def run():  
    
    from data_processor import DataProcessor  
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
    impact_analyzer = FinancialImpact(df)  
    impact_analyzer.impact_by_industry()  
  
if __name__ == "__main__":  
    run()  