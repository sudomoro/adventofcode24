class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path


    def read_lines(self):
        """Reads lines from the file."""
        with open(self.file_path, 'r') as file:
            return file.readlines()

    def parse_day_one(self):
        """Parses Day One file into two separate lists: left_list and right_list."""
        left_list, right_list = [], []
        for line in self.read_lines():
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        return left_list, right_list

    def parse_day_two(self):
        """Parses Day Two file into a list of lists of integers."""
        return [list(map(int, line.strip().split())) for line in self.read_lines()]
