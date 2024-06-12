import numpy as np
import csv
import matplotlib.pyplot as plt
import statistics as stats
import collections
from scipy.stats import norm

with open('targetA.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetA = np.array(data)
f.close()

with open('targetB.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    targetB = np.array(data)
f.close()

timeA = targetA[1:, 1].astype(float)
infoA = targetA[1:, 6]

seqA = []

for i in range(0,len(infoA)):
    m = infoA[i]
    seq = m[m.index("Seq=") + len("Seq="):(m.index("Seq=")+9)]
    seqA.append(int(seq))
  
seqA = np.array(seqA)

plt.figure(figsize=(10, 6))
plt.scatter(timeA, seqA)
plt.xlabel('Time')
plt.ylabel('Sequence Number')
plt.title('Sequence Number over Time')
plt.show()
plt.close()

packetLength = targetA[1:, 5].astype(int)

mean = np.mean(packetLength)
mode = stats.mode(packetLength)
standardDev = np.std(packetLength)

print("Statistics for packet lengths: ")
print("Mean - " + str(int(mean)))
print("Mode - " + str(mode))
print("Standard Deviation - " + str(int(standardDev)))

c = collections.Counter(packetLength)
packets = []
probabilities = []
for i in packetLength:
    if i not in packets:
        packets.append(i)
        count = c[i]
        probabilities.append(count/len(packetLength))

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

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('PDF')
plt.show()
plt.close()


cdf = np.cumsum(probabilities)

plt.figure(figsize=(10, 6))
plt.plot(x, cdf)
plt.xlabel('Packet Length')
plt.ylabel('Probability')
plt.title('CDF')
plt.show()
plt.close()

timeB = targetB[1:, 1].astype(float)
delays = []

infoB = targetB[1:, 6]
departureA = []
arrivalB = []

'''seqB = []

for j in range(len(targetB)-1):
    n = infoB[j]
    seq = n[n.index("Seq=") + len("Seq="):(n.index("Seq=")+9)]
    seqB.append(int(seq))
    times = np.where(seqA == int(seq))
    departureA.append(timeA[times[0][0]])

seqB = np.array(seqB)

for l in range(len(targetA)-1):
    times = np.where(seqB == seqA[l])
    print(seqB[times[0][0]])
    print(seqA[l])
    #arrivalB.append(timeB[times[0][0]])

print(len(departureA))
print(len(arrivalB))   
'''
sequences = []
for i in range(0,len(seqA)):
    for j in range(0, len(infoB)):
        n = infoB[j]
        seqB = n[n.index("Seq=") + len("Seq="):(n.index("Seq=")+9)]
        if seqA[i] == int(seqB):
            sequences.append(int(seqB))
            delay = abs(timeB[j] - timeA[i])
            delays.append(delay)
            


delays = np.array(delays)
sequences = np.array(sequences)

plt.figure(figsize=(10, 6))
plt.bar(sequences, delays)
plt.xlabel('Sequence number')
plt.ylabel('Time delay')
plt.title('Time Delays of Packets')
plt.show()
plt.close()
