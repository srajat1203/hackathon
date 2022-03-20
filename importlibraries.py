{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0   
\f1\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import os\
\pard\pardeftab720\partightenfactor0
\cf2 from collections import Counter\
import numpy as np\
import pandas as pd\
import matplotlib.pyplot as plt\
from keras.models import Sequential\
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense\
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img\
from PIL import Image\
from glob import glob\
from google.colab import drive}