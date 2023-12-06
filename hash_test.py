import numpy as np

def kl_divergence(means_p, stds_p, means_q, stds_q):
    num_elem_p = len(means_p)
    num_elem_q = len(means_q)

    kl_div = 0.0
    weight_p = 1
    weight_q = 1
    for mean_p, std_p in zip(means_p, stds_p):
        for mean_q, std_q in zip(means_q, stds_q):
            # # KL divergence
            # kl_div += weight_p * weight_q * (
            #     np.log(std_q / std_p) +
            #     ((std_p ** 2 + (mean_p - mean_q) ** 2) / (2 * std_q ** 2)) -
            #     0.5
            # )

            # Earth Mover's Distance (EMD) 
            kl_div += weight_p * weight_q * (
                np.abs(mean_p - mean_q)
            )

            # # Bhattacharyya distance
            # kl_div += weight_p * weight_q * (
            #     np.log(std_p * std_q / (std_p ** 2 + std_q ** 2) ** 0.5) +
            #     0.25 * (mean_p - mean_q) ** 2 / (std_p ** 2 + std_q ** 2)
            # )

    kl_div = kl_div / (len(means_p) * len(means_q))
    return kl_div

def hash_gaussian(x:np.array):
    # x is 1-d binary vector
    # get start and end indexes of 1s
    start_indexes = []
    end_indexes   = []

    for i in range(len(x)):
        if x[i] == 1:
            if i == 0 or x[i-1] == 0:
                start_indexes.append(i)

            if i == len(x)-1 or x[i+1] == 0:
                end_indexes.append(i)

    means = []
    stds = []
    for start_index, end_index in zip(start_indexes, end_indexes):
        # get the mean & length of cluster
        mean = (start_index + end_index) / 2.0
        length = end_index - start_index + 1
        
        means.append(mean)
        stds.append(length*1.0)

    return means, stds


log_dist_original = []
log_dist_hash = []

num_try = 100

for i in range(num_try):
    num_bit = 16
    # overlab = 0
    # band_size = 1

    # create num_bit bit random vector
    a = np.random.randint(0, 2, num_bit)
    b = np.random.randint(0, 2, num_bit)

    # a = np.array([1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0])
    # b = np.array([1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0])

    distance_original = np.sum(np.abs(a-b))

    a_means, a_stds = hash_gaussian(a)
    b_means, b_stds = hash_gaussian(b)

    # KL divergence between a_gaussians and b_gaussians
    distance_hash   = 0
    num_combination = 0
    for a_mean, a_std in zip(a_means, a_stds):
        for b_mean, b_std in zip(b_means, b_stds):
            # gaussian distance
            # distance_hash += np.exp(-0.5*((a_mean-b_mean)**2)/(a_std**2 + b_std**2))

            distance_hash = kl_divergence(a_means, a_stds, b_means, b_stds)

            num_combination = num_combination + 1

            # # KL divergence
            # distance_hash += (a_std**2 + (a_mean-b_mean)**2)/(2*b_std**2) + np.log(b_std/a_std)

    if num_combination > 0:
        distance_hash = distance_hash / num_combination

    print(distance_original, " || ", a_means, " ** ", b_means, " |||| " , distance_hash)
    log_dist_original.append(distance_original)
    log_dist_hash.append(distance_hash)

# plot log_dist_original vs log_dist_hash
import matplotlib.pyplot as plt
plt.scatter(log_dist_original, log_dist_hash)
plt.xlabel("original distance")
plt.ylabel("hash distance")
plt.show()
