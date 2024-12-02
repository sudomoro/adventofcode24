import pandas as pd
from FileHandler import FileHandler


class ReportComparisonAnalyzer:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)

    def calculate_similarity_score(self, reference_series, target_series):
        target_counts = target_series.value_counts()
        similarity_scores = reference_series * reference_series.map(target_counts).fillna(0)
        return similarity_scores.sum()

    def calculate_total_distance(self, reference_series, target_series):
        reference_sorted = reference_series.sort_values(ignore_index=True)
        target_sorted = target_series.sort_values(ignore_index=True)
        total_distance = (reference_sorted - target_sorted).abs()
        return total_distance.sum()

    def analyze(self):
        reference_list, target_list = self.file_handler.parse_day_one()
        reference_series = pd.Series(reference_list)
        target_series = pd.Series(target_list)
        
        similarity_score = self.calculate_similarity_score(reference_series, target_series)
        total_distance = self.calculate_total_distance(reference_series, target_series)
        
        return similarity_score, total_distance
