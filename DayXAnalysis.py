import pandas as pd
from FileHandler import FileHandler

class AnalysisClass:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        self.df = pd.DataFrame()
    
    def prepare_data(self):
        raise NotImplementedError("Subclasses must implement `prepare_data`.")
    
    def add_analysis_columns(self):
        raise NotImplementedError("Subclasses must implement `add_analysis_columns`.")
    
    def calculate_results(self):
        raise NotImplementedError("Subclasses must implement `calculate_results`.")
    
    def analyze(self):
        self.prepare_data()
        self.add_analysis_columns()
        return self.calculate_results()
