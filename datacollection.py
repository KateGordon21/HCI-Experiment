import csv
import time
from random import shuffle


class DataCollector:
    def __init__(self):
        self.data_file = ""
        self.participant_data = []
        self.start_time = 0
        self.end_time = 0
        self.error_count = 0
        self.diameters = [20, 40, 80, 160]
        self.distances = [50, 100, 200, 400]
        self.directions = [-1, 1]
        self.final_array = []

    def create_participant(self, participant_number):
        number = str(participant_number)
        self.data_file = "participant" + number + ".csv"
        with open(self.data_file, 'w', newline='') as csvfile:
            pass

    def pass_values(self):
        return self.final_array.pop()

    def create_target_list(self):
        for i in range(len(self.diameters)):
            for j in range(len(self.distances)):
                for k in range(len(self.directions)):
                    self.final_array.append([self.diameters[i], self.distances[j], self.directions[k]])
        shuffle(self.final_array)


    def initial_click(self):
        self.start_time = time.time()

    def target_click(self, error_count):
        self.end_time = time.time()
        self.error_count = error_count
        total_time = self.end_time - self.start_time

        self.participant_data.append(total_time)
        self.participant_data.append(self.error_count)
        self.participant_data.append(self.diameter)
        self.participant_data.append(self.distance)

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
