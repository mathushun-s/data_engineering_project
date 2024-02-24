import numpy as np
import csv
import matplotlib.pyplot as plt
import statistics as stats
import collections
from scipy.stats import norm

#reads data from csv files and puts it into numpy arrays
#reads data from targetA.csv
with open('targetA.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetA = np.array(data)
f.close()

#reads data from targetB.csv
with open('targetB.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetB = np.array(data)
f.close()

timeA = targetA[1:, 1].astype(float)
infoA = targetA[1:, 6]

seqA = []

#seperating the sequence numbers found in the targetA numpy array into a new array
for i in range(0,len(infoA)):
    m = infoA[i]
    seq = m[m.index("Seq=") + len("Seq="):(m.index("Seq=")+9)]
    seqA.append(int(seq))
  
seqA = np.array(seqA)
#plotting scatter graph of sequence numbers of the packets in targetA against its time
plt.figure(figsize=(10, 6))
plt.scatter(timeA, seqA)
plt.xlabel('Time')
plt.ylabel('Sequence Number')
plt.title('Sequence Number over Time')
plt.show()
plt.close()

packetLength = targetA[1:, 5].astype(int)

#calculates basic statistics(e.g mean, mode etc) of the packet lengths from targetA.csv
mean = np.mean(packetLength)
mode = stats.mode(packetLength)
standardDev = np.std(packetLength)

#displays the calculated statistics on command prompt
print("Statistics for packet lengths: ")
print("Mean - " + str(int(mean)))
print("Mode - " + str(mode))
print("Standard Deviation - " + str(int(standardDev)))

#calculating the probabilities of the packet lengths
c = collections.Counter(packetLength)
packets = []
probabilities = []
for i in packetLength:
    if i not in packets:
        packets.append(i)
        count = c[i]
        probabilities.append(count/len(packetLength))

#plotting bar graph displaying the probabilities of packet length against the actual packet length
plt.figure(figsize=(10, 6))
plt.bar(packets, probabilities)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('Probabilities of packet length')
plt.show()
plt.close()

#calculating and plotting the cumulative distribution function and the probability density function of packet lengths using the data in targetA
N = len(packetLength) 
data = np.random.randn(N) 
count, bins_count = np.histogram(data, bins=10) 

pdf = count/sum(count) 
cdf = np.cumsum(pdf) 

plt.plot(bins_count[1:], pdf, color="red", label="PDF") 
plt.plot(bins_count[1:], cdf, label="CDF")
plt.legend()
plt.show()
plt.close()

timeB = targetB[1:, 1].astype(float)
delays = []

infoB = targetB[1:, 6]
departureA = []
arrivalB = []

#calculating the time delays of the packets departing from targetA and arriving in targetB
#the packets in targetA and targetB are recognised by having the same sequence number 
sequences = []
for i in range(0,len(seqA)):
    for j in range(0, len(infoB)):
        n = infoB[j]
        seqB = n[n.index("Seq=") + len("Seq="):(n.index("Seq=")+9)]
        #checks if the sequence number for the packet in targetA matches with targetB
        if seqA[i] == int(seqB):
            sequences.append(int(seqB))
            delay = abs(timeB[j] - timeA[i])
            delays.append(delay)
            


delays = np.array(delays)
sequences = np.array(sequences)

#plotting the time delays against the sequence number
plt.figure(figsize=(10, 6))
plt.bar(sequences, delays)
plt.xlabel('Sequence number')
plt.ylabel('Time delay')
plt.title('Time Delays of Packets')
plt.show()
plt.close()
