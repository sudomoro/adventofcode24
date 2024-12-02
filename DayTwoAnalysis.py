import pandas as pd
from FileHandler import FileHandler


class ReportSafetyAnalyzer:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)

    def _calculate_differences(self, report):
        return [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]

    def _is_within_bounds(self, differences):
        return all(1 <= diff <= 3 for diff in differences)

    def _is_monotonic(self, report):
        increasing = all(report[i + 1] > report[i] for i in range(len(report) - 1))
        decreasing = all(report[i + 1] < report[i] for i in range(len(report) - 1))
        return increasing or decreasing

    def is_safe_report(self, report):
        if len(report) < 2:
            return False
        differences = self._calculate_differences(report)
        return self._is_within_bounds(differences) and self._is_monotonic(report)

    def is_safe_with_dampener(self, report):
        if self.is_safe_report(report):
            return True
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if self.is_safe_report(modified_report):
                return True
        return False

    def count_safe_reports(self, reports):
        safe_count = 0
        dampened_safe_count = 0

        for report in reports.values.tolist():
            clean_report = [x for x in report if pd.notna(x)]
            if self.is_safe_report(clean_report):
                safe_count += 1
            if self.is_safe_with_dampener(clean_report):
                dampened_safe_count += 1

        return safe_count, dampened_safe_count

    def analyze(self):
        data = self.file_handler.parse_day_two()
        reports = pd.DataFrame(data)
        safe_reports_count, dampened_safe_reports_count = self.count_safe_reports(reports)
        return safe_reports_count, dampened_safe_reports_count
