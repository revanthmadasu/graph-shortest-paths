import os
import time
import json
class Logger:
    def __init__(self):
        self.output_dir = "outputs"
        self.timestamp = ""
        self.dir_path = ""
    def start(self):
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.dir_path = os.path.join(self.output_dir, self.timestamp)
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
            print(f"Directory created: {self.dir_path}")
        else:
            print(f"Directory already exists: {self.dir_path}")
    def stop(self):
        self.timestamp = ""
        self.dir_path = ""

    def dumpIntoFile(self, object, file_name):
        with open(f'{self.dir_path}/{file_name}.txt', "w") as f:
            # write the object to the file as a JSON string
            json.dump(object, f)

    def logInput(self, input_dict):
        self.dumpIntoFile(input_dict, "input_dict")

    def logDijkstraOutput(self, dijk_result):
        self.dumpIntoFile(dijk_result, "dijkstra_output")

    def logBellmanOutput(self, bellman_result):
        self.dumpIntoFile(bellman_result, "bellman_ford_output")