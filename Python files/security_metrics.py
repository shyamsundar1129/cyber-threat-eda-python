import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
class SecurityMetrics:  
    def __init__(self, dataframe):  
        self.df = dataframe  
          
    def resolution_time_stats(self):  
        try:  
            stats = self.df['IncidentResolutionTime'].describe()  
            print("Resolution time metrics calculated:")  
            print(stats)  
            return stats  
        except Exception as e:  
            print("Error in security metrics analysis:", e)  
            return None  
              
    def vulnerability_analysis(self):  
        try:  
            vuln_counts = self.df['SecurityVulnerabilityType'].value_counts()  
            
            plt.figure(figsize=(10, 6))  
            plt.pie(vuln_counts, labels=vuln_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"), wedgeprops=     {'edgecolor': 'black'})  
    
            
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')  
            plt.gca().add_artist(centre_circle)  
    
            plt.title('Distribution of Security Vulnerability Types')  
            plt.show()  
    
        except Exception as e:  
            print("Error in vulnerability analysis:", e)

def run():  
    from data_processor import DataProcessor  
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
    metrics = SecurityMetrics(df)  
    metrics.resolution_time_stats()  
    metrics.vulnerability_analysis()  
  
if __name__ == "__main__":  
    run()  