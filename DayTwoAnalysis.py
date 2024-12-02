import pandas as pd
import numpy as np
from FileHandler import FileHandler


class ReportSafetyAnalyzer:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        self.df = pd.DataFrame()  # Initialize an empty DataFrame

    def prepare_data(self):
        """Load and structure the data as a DataFrame with arrays."""
        data = self.file_handler.parse_day_two()
        self.df = pd.DataFrame({"Report": data})

    def add_analysis_columns(self):
        """Add intermediate columns to analyze each report."""
        self.df["Differences"] = self.df["Report"].apply(
            lambda x: np.diff(x)
        )
        
        self.df["Is_Monotonic"] = self.df["Differences"].apply(
            lambda diffs: np.all(diffs > 0) or np.all(diffs < 0)
        )
        
        self.df["Within_Bounds"] = self.df["Differences"].apply(
            lambda diffs: np.all((1 <= np.abs(diffs)) & (np.abs(diffs) <= 3))
        )
        
        self.df["Is_Safe_Report"] = self.df.apply(
            lambda row: row["Within_Bounds"] and row["Is_Monotonic"], axis=1
        )
        
        self.df["Is_Safe_With_Dampener"] = self.df.apply(
            lambda row: self._is_safe_with_dampener(row["Is_Safe_Report"], row["Report"]), axis=1
        )

    def calculate_results(self):
        """Calculate the counts of safe reports and dampened safe reports."""
        safe_reports_count = self.df["Is_Safe_Report"].sum()
        dampened_safe_reports_count = self.df["Is_Safe_With_Dampener"].sum()
        return safe_reports_count, dampened_safe_reports_count

    @staticmethod
    def _is_monotonic_from_differences(diffs):
        """Determine monotonicity directly from differences."""
        return np.all(diffs > 0) or np.all(diffs < 0)

    def _is_safe_with_dampener(self, is_safe_report, report):
        """Determine if a report is safe with a single dampener."""
        if is_safe_report:
            return True
        if len(report) < 3: 
            return False
        
        for i in range(len(report)):
            modified_report = np.delete(np.array(report), i)
            differences = np.diff(modified_report)
            if (
                np.all((1 <= np.abs(differences)) & (np.abs(differences) <= 3)) and 
                self._is_monotonic_from_differences(differences)
            ):
                return True
        return False

    def analyze(self):
        """Main entry point to perform analysis."""
        self.prepare_data()
        self.add_analysis_columns()
        return self.calculate_results()
