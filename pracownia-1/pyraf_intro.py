import sys
from pyraf import iraf
import matplotlib.pyplot as plt


def get_stat_from_files(input, stat):
	iraf.images()
	result = []
	for image in input:
		result.append(float(iraf.imstat(image, fields = stat, format = 0, Stdout = 1)[0]))
	return result


means = get_stat_from_files(sys.argv[1:], "mean")
stddev = get_stat_from_files(sys.argv[1:], "stddev")
plt.subplot(121)
plt.plot(means, 'o')
plt.xlabel('Image no.')
plt.ylabel('Mean')
plt.subplot(122)
plt.plot(means, stddev, 'o')
plt.xlabel('Mean')
plt.ylabel('Standard deviation')
plt.show()