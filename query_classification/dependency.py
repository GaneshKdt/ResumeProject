import json
import string
import emoji
import sys
sys.path.append(r"D:\Project\query_classification")
from helper import preprocessing
import pickle
import numpy as np
import warnings
from flask import Flask, request
import gensim
import sklearn
print("All dependency installed...")