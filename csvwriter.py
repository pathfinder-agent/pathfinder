import os
import csv

class CSVWriter:
    def __init__(self, directory, filename, max_writes):
        self.directory = directory
        self.base_filename = filename
        self.max_writes = max_writes
        self.current_writes = 0
        self.current_file_index = 0
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def get_current_filename(self):
        return os.path.join(self.directory, f"{self.base_filename}_{self.current_file_index}.csv")

    def rotate_file(self):
        self.current_writes = 0
        self.current_file_index += 1

    def write_row(self, data):
        if self.current_writes >= self.max_writes:
            self.rotate_file()
        current_filename = self.get_current_filename()
        file_exists = os.path.exists(current_filename)
        with open(current_filename, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(data.keys())
            writer.writerow(data.values())
        self.current_writes += 1