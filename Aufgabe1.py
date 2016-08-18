# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# raise error if not possible to create such set

# just a test comment 

import random

def list_of_sets(min_val, max_val, k, l):
	if l > max_val - min_val:
		raise ValueError

	result = []

	for _ in range(k):
		tmp_set = set()

		while len(tmp_set) != l:
			tmp_rand_n = random.randint(min_val, max_val +1) 
			tmp_set.add(tmp_rand_n)

		result.append(tmp_set)
	return result

if __name__ == "__main__":
	print list_of_sets(min_val=1, max_val=3, k=4, l=3)
