#Description explaining the data sets can be found in 'data_description_problem1.pdf'

The code read the contents of both data sets from 'targetA.csv' and 'targetB.csv' and make these available
in two seperate numpy arrays.
▪ Graph1: sequence numbers over time. In this graph time values (from
column B) are on the x-axis, and the sequence numbers are
be on the y-axis. The sequence numbers can be found in column G of
the datasets.
▪ Graph2: probabilities of packet lengths. You will notice that packets
listed in the targetA.csv file take one of a limited number of
possible packet length (packet length is given in column F). For this
graph you can create a scatterplot, or use a bar chart, or use a
standard plot. The x-axis should contain the possible packet lengths,
and the y-axis should contain the calculated probability of that
particular packet length over the whole packet set.
- The code calculates and prints the following values, using the data in
targetA.csv file: the mean, the mode and the standard deviation of packet
length
- The code plots the distribution of the packet lengths using the data
in targetA.csv file – both the cumulative distribution function and the probability
density function
- The code calculates and plots the delay between each packet departure time at
node A (time in column B in targetA.csv) and the arrival time at node B (time in
column B in targetB.csv). Please note that each packet is uniquely identified by
the sequence number, which is given in column G of each dataset, so the delay
is calculated by subtracting the arrival and departure times for each 
packet, where packet is uniquely identified by its sequence number. The packet
delays are plotted on a single graph.
