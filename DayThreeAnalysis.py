import pandas as pd
import numpy as np
import regex as re
from FileHandler import FileHandler

class MultiplicationAnalysis:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        self.df = pd.DataFrame()

    def prepare_data(self):
        """Reads data from the file."""
        self.lines = self.file_handler.read_lines()

    def extract_valid_instructions(self):
        """Extracts valid mul instructions while respecting the latest do/don't state."""
        valid_mul_pattern = r"mul\((\d+),(\d+)\)"
        enable_pattern = r"do\(\)"
        disable_pattern = r"don't\(\)"
        
        data = []
        instructions_enabled = True
        for line in self.lines:
            tokens = re.split(r"(do\(\)|don't\(\))", line)
            for token in tokens:
                if re.match(enable_pattern, token):
                    instructions_enabled = True
                elif re.match(disable_pattern, token):
                    instructions_enabled = False
                else:
                    matches = re.findall(valid_mul_pattern, token)
                    for x, y in matches:
                        data.append((int(x), int(y), instructions_enabled))        
        return data

    def add_analysis_columns(self):
        data = self.extract_valid_instructions()
        self.df = pd.DataFrame(data, columns=["X", "Y", "Enabled"])

    def calculate_results(self):
        self.df['Result'] = self.df['X'] * self.df['Y']
        return self.df['Result'].sum(), self.df[self.df['Enabled']]['Result'].sum()

    def analyze(self):
        self.prepare_data()
        self.add_analysis_columns()
        return self.calculate_results()