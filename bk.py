

# # apply LSH (Locality Sensitive Hashing) to the random vector
# # Step 1: Split the vector into smaller bands or chunks. Each band has overlab bits.
# a_split = np.array([a[i:i+band_size] for i in range(0, num_bit-overlab, band_size-overlab)])
# b_split = np.array([b[i:i+band_size] for i in range(0, num_bit-overlab, band_size-overlab)])

# # # Step 2: Hash each band to produce a hash value for that band.
# a_hash = np.array([np.sum(x)%(band_size+1) for x in a_split])
# b_hash = np.array([np.sum(x)%(band_size+1) for x in b_split])

# # # Step 2: toggle hash
# # a_hash = np.array([hash_kernel(x) for x in a_split])
# # b_hash = np.array([hash_kernel(x) for x in b_split])

# # Step 3: Compare the hash values for each band. If the hash values for each band are equal, then the vectors are similar.
# distance_original = np.sum(np.abs(a-b))
# distance_hash = np.sum(np.abs(a_hash-b_hash))
# # distance_hash = np.sum(a_hash != b_hash)

# # # print
# # print("original vector a: ", a)
# # print("original vector b: ", b)
# # print("split vector a: ", a_split)
# # print("split vector b: ", b_split)
# # print("hash vector a: ", a_hash)
# # print("hash vector b: ", b_hash)
# # print("distance between original vectors: ", distance_original)
# # print("distance between hash vectors: ", distance_hash)