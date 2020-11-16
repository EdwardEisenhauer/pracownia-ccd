from pyraf import iraf

def run_imarith(input_1, operator, input_2, result):
	iraf.imutil(_doprint=0)
	iraf.imarith(operand1=input_1 , op=operator, operand2=input_2, result=result,\
				 title='', divzero=0.0, hparams='', pixtype='', calctype='',\
				 verbose="No", noact="No", mode="al")


def run_hedit(images, fields, value, result):
	iraf.imutil(_doprint=0)
	iraf.hedit(images=images, fields=fields, value=value, add="Yes", addonly="No",\
			   delete="No", verify="Yes", show="Yes", update="Yes", mode="al")


def run_darkcombine(images, output):
	iraf.imred(_doprint=0)
	iraf.ccdred(_doprint=0)
	iraf.darkcombine(input=images, output=output, combine="average", reject="minmax", \
					 ccdtype="none", process="Yes", delete="No", clobber="No", scale="exposure", \
					 statsec='', nlow=0, nhigh=1, nkeep=1, mclip="Yes", lsigma=3.0, hsigma=3.0, \
					 rdnoise=0., gain=1., snoise=0., pclip=-0.5, blank=0.0, mode="al")


def run_flatcombine(images, ccdtype="none"):
	iraf.imred(_doprint=0)
	iraf.ccdred(_doprint=0)
	iraf.flatcombine(images, ccdtype=ccdtype, nlow=0, nhigh=0, nkeep=0)


def run_zerocombine(images, output, ccdtype="none"):
	iraf.imred(_doprint=0)
	iraf.ccdred(_doprint=0)
	iraf.zerocombine(input=images, output=output, ccdtype=ccdtype, nhigh=0)

