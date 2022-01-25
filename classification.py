'''
binary classification with skewed dataset : AUC would be the metrics and Stratified k-fold Cross Validation
resizing to 256*256
converting to grayscale 
'''
import os

import numpy as np
import pandas as pd

from PIL import Image
from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection

from tqdm import tqdm

def create_dataset(training_df, image_dir):
    images = []
    targets =[]

    