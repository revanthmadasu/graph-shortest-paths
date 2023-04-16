import os
import time
import json
import matplotlib.pyplot as plt
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

    # dumps directly json into file
    def dumpIntoFile(self, object, file_name):
        with open(f'{self.dir_path}/{file_name}.txt', "w") as f:
            # write the object to the file as a JSON string
            json.dump(object, f)

    def logInput(self, input_dict):
        self.dumpIntoFile(input_dict, "input_dict")

    def logBfsOutput(self, bfs_result):
        self.dumpIntoFile(bfs_result, "bfs_output")

    def logDijkstraOutput(self, dijk_result):
        self.dumpIntoFile(dijk_result, "dijkstra_output")

    def logBellmanOutput(self, bellman_result):
        self.dumpIntoFile(bellman_result, "bellman_ford_output")

    def logShortestPathRuntimes(self, dijkstra_result, bellman_result):

        bellman_time = bellman_result['runtime']
        dijkstra_time = dijkstra_result['runtime']

        # Generate a comparison chart between the runtimes of Bellman-Ford and Dijkstra algorithms
        plt.bar(['Bellman-Ford', 'Dijkstra'], [bellman_time, dijkstra_time])
        plt.title('Comparison of Bellman-Ford and Dijkstra Runtimes')
        plt.xlabel('Algorithm')
        plt.ylabel('Runtime (seconds)')
        # plt.show()
        plt.savefig(f'{self.dir_path}/shortpath_runtimes.png')
        plt.close()

    def logAnalyseRuntimes(self, runtimes, algorithm):
        # Create a bar chart of runtimes
        plt.bar(range(len(runtimes)), runtimes)

        # Add labels and title to the chart
        plt.xlabel('Test case')
        plt.ylabel('Runtime (seconds)')
        plt.title('Runtimes for test cases')

        # Save the chart
        plt.savefig(f'{self.dir_path}/{algorithm}.png')


    def logAllRuntimes(self, bfs_result, dijkstra_result, bellman_result):

        bellman_time = bellman_result['runtime']
        dijkstra_time = dijkstra_result['runtime']
        bfs_time = bfs_result['runtime']

        # Generate a comparison chart between the runtimes of Bellman-Ford and Dijkstra algorithms
        plt.bar(['BFS', 'Bellman-Ford', 'Dijkstra'], [bfs_time, bellman_time, dijkstra_time])
        plt.title('Comparison of BFS, Bellman-Ford and Dijkstra Runtimes')
        plt.xlabel('Algorithm')
        plt.ylabel('Runtime (seconds)')
        # plt.show()
        plt.savefig(f'{self.dir_path}/all_runtimes.png')
        plt.close()