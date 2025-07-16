#Network Latency Visualizer
#Python application that monitors network latency to a specified external IP address and visualizes the data.

A Python application that monitors and visualizes network latency (round-trip time) to a user-specified IP address or hostname. 
It sends multiple ping requests, calculates statistics (min, max, average RTT, packet loss), and generates a plot of the results

Built using:
- [pythonping](https://pypi.org/project/pythonping/)
- [matplotlib](https://matplotlib.org/)


## Installation

```bash

#Clone the repository:
git clone https://github.com/TFlan90/Network-latency-viz
cd network-latency-visualizer

#Install dependencies
pip install pythonping matplotlib

#Run it
python main.py

#Sample Output
[Screenshot of output](images/sample_run.png)
[Screenshot of graph](images/graph.png)