import sys
import jupyterlab
import pandas

import pandas_datareader
import numpy
import matplotlib
import sklearn
import django
import tensorflow
import scipy
import keras
import seaborn
import cv2 # opencv-python
import nltk
import statsmodels

# print default conda environment
# import os
# print(os.environ['CONDA_DEFAULT_ENV'] + "\n")

# adding newlines
print('Python version: \n{0}'.format(sys.version), "\n")

# jupyterlab
print('jupyterlab: {0}'.format(jupyterlab.__version__))

# pandas
print('pandas: {0}'.format(pandas.__version__))

# pandas_datareader
print('pandas_datareader: {0}'.format(pandas_datareader.__version__))

# numpy
print('numpy: {0}'.format(numpy.__version__))

# matplotlib
print('matplotlib: {0}'.format(matplotlib.__version__))

# scikit-learn
print('sklearn: {0}'.format(sklearn.__version__))

# django
print('django: {0}'.format(django.__version__))

# tensorflow
print('tensorflow: {0}'.format(tensorflow.__version__))

# scipy
print('scipy: {0}'.format(scipy.__version__))

# keras
print('keras: {0}'.format(keras.__version__))

# seaborn
print('seaborn: {0}'.format(seaborn.__version__))

# cv2 (opencv-python)
print('cv2 (opencv-python): {0}'.format(cv2.__version__))

# nltk
print('nltk: {0}'.format(nltk.__version__))

# statsmodels
print('statsmodels: {0}'.format(statsmodels.__version__))