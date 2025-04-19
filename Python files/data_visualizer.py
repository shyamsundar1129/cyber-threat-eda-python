import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
class DataVisualizer:  
    def __init__(self, dataframe):  
        self.df = dataframe  
  
    def plot_financial_loss_by_year(self):  
        try:  
            plt.figure(figsize=(10, 6))

                
            loss_by_year = self.df.groupby('Year')['FinancialLoss'].sum()

            
            plt.pie(loss_by_year, labels=loss_by_year.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))

            plt.title("Total Financial Loss by Year")
            plt.show()

            print("Financial loss pie chart displayed successfully.")
 
        except Exception as e:  
            print("Error plotting financial loss:", e)  
  
def run():  
      
    from data_processor import DataProcessor  
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
    visualizer = DataVisualizer(df)  
    visualizer.plot_financial_loss_by_year()  
  
if __name__ == "__main__":  
    run()  