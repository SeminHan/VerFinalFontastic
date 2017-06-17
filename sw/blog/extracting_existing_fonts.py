from sklearn.feature_extraction.text import TfidfVectorizer
# This library is needed for converging pixel information formatted as txt file to vector
from scipy.sparse import csr_matrix
# This library is needed for normalize csr_matrix to general matrix
from math import *
# This library is needed for calculating intersection and union of two fonts' list
import numpy as np
from numpy import matrix
# These two libraries are needed for transforming vectored pixel to single-dimensional list






def estand(font):
	docu=open(font, 'r')
	tfidf=TfidfVectorizer().fit_transform(docu)

	return tfidf.todense()
# This function is 1. converging txt file to vector(csr_matrix format) 2. converging csr_matrix vector to general matrix

def eflatten(nlist):
	result=[val for sublist in nlist for val in sublist]
	# result=[]
	# for sublist in nlist:
		# for val in sublist:
			# result.append(val)

	return result
# This function is for flattening nested list(in exact, two-dimensional list) to single-dimensional list

def econversion(ffile):
	sfont=estand(ffile)
	cfont=np.squeeze(np.asarray(sfont))
	ffont=eflatten(cfont)

	return ffont
# This function is for executing conversion process that can make txt file transformed as single dimensional list
# And this function is a set of above functions	

# Developed by Semin Han