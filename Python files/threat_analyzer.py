import pandas as pd  
  
class ThreatAnalyzer:  
    def __init__(self, dataframe):  
        self.df = dataframe  
  
    def analyze_attack_types(self):  
        try:  
            attack_counts = self.df['AttackType'].value_counts()  
            print("Attack type analysis completed:")  
            print(attack_counts)  
            return attack_counts  
        except Exception as e:  
            print("Error analyzing attack types:", e)  
            return None  
  
def run():  
      
    from data_processor import DataProcessor  
    filepath = "GCST - Python.csv"  
    processor = DataProcessor(filepath)  
    df = processor.load_data()  
    df = processor.clean_data()  
    threat_analyzer = ThreatAnalyzer(df)  
    threat_analyzer.analyze_attack_types()  
  
if __name__ == "__main__":  
    run()  