import sys
from pyraf import iraf
from pyraf_runs import run_zerocombine

images = sys.argv[1]

try:
	# for image in images:
	run_zerocombine(images, 'MasterBias.fits')
	iraf.imheader(images, longheader='yes')
	iraf.hselect(images=images, fields='data-typ', expr='yes')
except iraf.IrafError as err:
	print("Iraf Error!")
	print(err)
# run_darkcombine(images, output)
