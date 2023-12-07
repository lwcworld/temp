import numpy as np


log_dist_original = []
log_dist_hash = []

num_try = 1000

for i in range(num_try):
    num_bit = 16
    overlab = 2
    band_size = 4

    # create num_bit bit random vector
    a = np.random.randint(0, 2, num_bit)
    b = np.random.randint(0, 2, num_bit)
    # b = a

    # apply LSH (Locality Sensitive Hashing) to the random vector
    # Step 1: Split the vector into smaller bands or chunks. Each band has overlab bits.
    a_split = np.array([a[i:i+band_size] for i in range(0, num_bit-overlab, band_size-overlab)])
    b_split = np.array([b[i:i+band_size] for i in range(0, num_bit-overlab, band_size-overlab)])

    # Step 2: Hash each band to produce a hash value for that band.
    a_hash = np.array([np.sum(x)%(band_size+1) for x in a_split])
    b_hash = np.array([np.sum(x)%(band_size+1) for x in b_split])

    # Step 3: Compare the hash values for each band. If the hash values for each band are equal, then the vectors are similar.
    distance_original = np.sum(np.abs(a-b)) + np.random.normal(0, 0.1)
    distance_hash     = np.sum(np.abs(a_hash-b_hash)) + np.random.normal(0, 0.1)

    log_dist_original.append(distance_original)
    log_dist_hash.append(distance_hash)

    # # print
    # print("original vector a: ", a)
    # print("original vector b: ", b)
    # print("split vector a: ", a_split)
    # print("split vector b: ", b_split)
    # print("hash vector a: ", a_hash)
    # print("hash vector b: ", b_hash)
    # print("distance between original vectors: ", distance_original)
    # print("distance between hash vectors: ", distance_hash)

# plot log_dist_original vs log_dist_hash
import matplotlib.pyplot as plt
plt.scatter(log_dist_original, log_dist_hash, s=2)
plt.xlabel("log_dist_original")
plt.ylabel("log_dist_hash")

# print(log_dist_original)
# print(log_dist_hash)

# plot y=x line
x = np.linspace(0, 20, 100)
y = x
plt.plot(x, y, '-r', label='y=x')

plt.xlim(0, 20)
plt.ylim(0, 20)
plt.show()
