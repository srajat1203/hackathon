{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Creating an object of ImageDataGenerator.
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 train_datagen = ImageDataGenerator(rescale= 1./255,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 shear_range = 0.3,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 horizontal_flip=True,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 zoom_range = 0.3)\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 test_datagen = ImageDataGenerator(rescale= 1./255)\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \cb3 #Generating batches of Augmented data.
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 train_generator = train_datagen.flow_from_directory(\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 directory = train_path,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 target_size= x.shape[:2],\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 batch_size = batch_size,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 color_mode= "rgb",\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 class_mode= "categorical")\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 test_generator = test_datagen.flow_from_directory(\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 directory = test_path,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 target_size= x.shape[:2],\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 batch_size = batch_size,\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 color_mode= "rgb",\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 class_mode= "categorical")\cf2 \cb1 \strokec2 \
}