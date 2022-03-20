{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Visualizing more Images
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 images = ['Orange', 'Banana', 'Cauliflower', 'Cactus fruit', 'Eggplant', 'Avocado', 'Watermelon','Lychee', 'Walnut']\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 fig = plt.figure(figsize =(10,5))\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 for i in range(len(images)):\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2     ax = fig.add_subplot(3,3,i+1,xticks=[],yticks=[])\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2     plt.title(images[i])\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2     plt.axis("off")\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2     ax.imshow(load_img(train_path + images[i] +"/0_100.jpg", target_size=(100,100)))\cf2 \cb1 \strokec2 \
}