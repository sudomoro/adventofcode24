from DayOneAnalysis import ReportComparisonAnalyzer 
from DayTwoAnalysis import ReportSafetyAnalyzer
from DayThreeAnalysis import MultiplicationAnalysis
# Main Logic
if __name__ == "__main__":
    # Day One Analysis
    day_one = ReportComparisonAnalyzer("day_one.txt")
    similarity_score, total_distance = day_one.analyze()

    print("Day One Results:")
    print(f"Similarity score: {similarity_score}")
    print(f"Total distance: {total_distance}")

    # Day Two Analysis
    day_two = ReportSafetyAnalyzer("day_two.txt")
    safe_reports_count, safe_reports_with_dampener_count = day_two.analyze()

    print("\nDay Two Results:")
    print(f"Safe reports without dampener: {safe_reports_count}")
    print(f"Safe reports with dampener: {safe_reports_with_dampener_count}")

    # Day Three Analysis
    day_three = MultiplicationAnalysis("day_three.txt")
    sum_valid_muls, sum_valid_enabled_muls = day_three.analyze()

    print("\nDay Three Results:")
    print(f"Sum of valid multiplications: {sum_valid_muls}")
    print(f"Sum of valid enabled multiplications: {sum_valid_enabled_muls}")
