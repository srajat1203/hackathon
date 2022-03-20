{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Creating the model
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 model = Sequential()\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Conv2D(32,(3,3),input_shape = x.shape))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Activation("relu"))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(MaxPooling2D())\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Conv2D(32,(3,3)))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Activation("relu"))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(MaxPooling2D())\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Conv2D(64,(3,3)))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Activation("relu"))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(MaxPooling2D())\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Flatten())\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Dense(1024))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Activation("relu"))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Dropout(0.5))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Dense(number_of_class)) \cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 model.add(Activation("softmax"))\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \strokec2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Compiling the model
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 model.compile(loss = "categorical_crossentropy",\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 optimizer = "rmsprop",\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 metrics = ["accuracy"])\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \strokec2 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Getting model's summary
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 model.summary()\cf2 \cb1 \strokec2 \
}