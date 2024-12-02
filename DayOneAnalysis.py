import pandas as pd
from FileHandler import FileHandler

class ReportComparisonAnalyzer:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        self.df = pd.DataFrame()  # Initialize an empty DataFrame

    def prepare_data(self):
        """Sort the data and initialize the DataFrame with sorted values."""
        # Load and sort data
        reference_list, target_list = self.file_handler.parse_day_one()
        reference_sorted = sorted(reference_list)
        target_sorted = sorted(target_list)
        
        # Initialize the DataFrame with sorted columns
        self.df = pd.DataFrame({
            "Reference_Sorted": reference_sorted,
            "Target_Sorted": target_sorted
        })

    def add_analysis_columns(self):
        """Add analysis columns based on the sorted data."""
        # Map target counts to reference and calculate similarity scores
        target_counts = pd.Series(self.df["Target_Sorted"]).value_counts()
        self.df["Target_Counts"] = self.df["Reference_Sorted"].map(target_counts).fillna(0)
        self.df["Similarity_Scores"] = self.df["Reference_Sorted"] * self.df["Target_Counts"]
        
        # Calculate absolute distances for each row
        self.df["Distance_Per_Row"] = (self.df["Reference_Sorted"] - self.df["Target_Sorted"]).abs()

    def calculate_results(self):
        """Calculate and return the final similarity score and total distance."""
        similarity_score = self.df["Similarity_Scores"].sum()
        total_distance = self.df["Distance_Per_Row"].sum()
        return similarity_score, total_distance

    def analyze(self):
        """Main entry point to perform analysis."""
        # Prepare data and add analysis columns
        self.prepare_data()
        self.add_analysis_columns()
        
        # Calculate and return final results
        return self.calculate_results()
