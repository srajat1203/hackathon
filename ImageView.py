{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Setting Training & Test dir paths
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 train_path = './fruits-360/Training/'\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 test_path = './fruits-360/Test/'\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \cb3 #Displaying the image
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 img = load_img(train_path + "Apple Braeburn/0_100.jpg", target_size=(100,100))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 plt.imshow(img)\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 plt.axis("off")\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 plt.show()\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \cb3 #Printing the shape of the image array 
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 x = img_to_array(img)\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 print(x.shape)\cf2 \cb1 \strokec2 \
}