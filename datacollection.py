import csv
import time


class DataCollector:
    def __init__(self):
        self.data_file = ""
        self.participant_data = []
        self.start_time = 0
        self.end_time = 0
        self.error_count = 0

    def create_participant(self, participant_number):
        number = str(participant_number)
        self.data_file = "participant" + number + ".csv"
        with open(self.data_file, 'w', newline='') as csvfile:
            pass

    def initial_click(self):
        self.start_time = time.time()

    def target_click(self, error_count):
        self.end_time = time.time()
        self.error_count = error_count
        total_time = self.end_time - self.start_time

        self.participant_data.append(total_time)
        self.participant_data.append(self.error_count)

        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.participant_data)

        self.start_time = 0
        self.end_time = 0
        self.error_count = 0
        self.participant_data = []

    def end_session(self):
        self.data_file = ""

    def get_progress(self):
        with open(self.data_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader)
        return row_count
