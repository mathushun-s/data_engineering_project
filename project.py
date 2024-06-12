import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
import collections

#Saves the contents of targetA to a numpy array
with open('targetA.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetA = np.array(data)
f.close()

#Saves the contents of targetB to a numpy array
with open('targetB.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetB = np.array(data)
f.close()

#Assigns times in column B of targetA to an array
timeA = targetA[1:, 1].astype(float)
infoA = targetA[1:, 6]

#Parses for sequence numbers in targetA and assigns to numpy array
seqA = []

for i in range(0,len(infoA)):
    m = infoA[i]
    seq = m[m.index("Seq=") + len("Seq="):(m.index("Seq=")+9)]
    seqA.append(int(seq))
  
seqA = np.array(seqA)

#Plotting sequence number over time graph
plt.figure(figsize=(10, 6))
plt.scatter(timeA, seqA)
plt.xlabel('Time')
plt.ylabel('Sequence Number')
plt.title('Sequence Number over Time')
plt.show()
plt.close()

packetLength = targetA[1:, 5].astype(int)

#Here the statistics on packet length data is calculated
mean = np.mean(packetLength)
mode = stats.mode(packetLength)
standardDev = np.std(packetLength)

#The statistics are displayed to the user
print("Statistics for packet lengths: ")
print("Mean - " + str(int(mean)))
print("Mode - " + str(mode))
print("Standard Deviation - " + str(int(standardDev)))

#Calculates probabilites for each packet length
c = collections.Counter(packetLength)
packets = []
probabilities = []
for i in packetLength:
    if i not in packets:
        packets.append(i)
        count = c[i]
        probabilities.append(count/len(packetLength))

#Plotting the packet length probability graph
plt.figure(figsize=(10, 6))
plt.bar(packets, probabilities)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('Probabilities of packet length')
plt.show()
plt.close()

x = np.array(packets)
y = np.array(probabilities)

combination = np.column_stack((x,y))
combination = np.array(sorted(combination, key=lambda x: x[0], reverse=False))
x, y = np.split(combination,2,axis=1)

#Plotting the PDF graph
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('PDF')
plt.show()
plt.close()


cdf = np.cumsum(probabilities)

#Plotting the CDF graph
plt.figure(figsize=(10, 6))
plt.plot(x, cdf)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('CDF')
plt.show()
plt.close()

timeB = targetB[1:, 1].astype(float)
infoB = targetB[1:, 6]
seqB = []

#Parses for sequence numbers in targetB
for i in range(0,len(infoB)):
    m = infoB[i]
    seq = m[m.index("Seq=") + len("Seq="):(m.index("Seq=")+9)]
    seqB.append(int(seq))
  
seqB = np.array(seqB)

#This function removes any duplicate sequence numbers and leaves only the first instance in the array
def removeDuplicates(seqs, times):
    #Combining the times and sequence numbers into one 2D array
    combo = np.column_stack((seqs,times))
    combo = np.array(sorted(combo, key=lambda x: x[0], reverse=False))
    _, indices = np.unique(combo[:, 0], return_index=True)
    return combo[indices, :]

#Splitting the 2D array produced by the above function back to individual arrays
seqA, timeA = np.split(removeDuplicates(seqA, timeA),2,axis=1)
seqB, timeB = np.split(removeDuplicates(seqB, timeB),2,axis=1)

#These arrays will store the data for the x-axis and y-axis, respectively, for the plot
sequences = []
delays = []

print('The plot for the packet delays takes a while...')
#Finding the packets in both targetA and targetB of the same sequence number
for i in range(0, len(seqA)):
    for j in range(0, len(seqB)):
        if seqA[i] == seqB[j]:
            sequences.append(seqA[i])
            #Delay is calculated
            delays.append(timeA[j] - timeB[i])
            break

#Plotting the packet delay graph
plt.figure(figsize=(10, 6))
plt.plot(sequences, delays, marker='o', linestyle='', markersize=4)
plt.title('Packet Delays from A to B')
plt.xlabel('Sequence Number')
plt.ylabel('Delay')
plt.grid(True)
plt.show()
