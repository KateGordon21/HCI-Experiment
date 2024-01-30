import csv
import time


class DataCollector:
    def __init__(self):
        self.data_file = ""
        self.participant_data = []
        self.start_time = 0
        self.end_time = 0

    def create_participant(self, participant_number):
        number = str(participant_number)
        self.data_file = "participant"+number+".csv"
        with open(self.data_file, 'w', newline='') as csvfile:
            pass

    def initial_click(self):
        self.start_time = time.time()

    def target_click(self):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        self.participant_data.append(total_time)
        self.start_time = 0
        self.end_time = 0

    def end_session(self):
        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.participant_data)
        self.participant_data = []

    def get_progress(self):
        return len(self.participant_data)
