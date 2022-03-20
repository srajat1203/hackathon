{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red31\green31\blue31;\red239\green239\blue239;}
{\*\expandedcolortbl;;\cssrgb\c16078\c16078\c16078;\cssrgb\c94902\c94902\c94902;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Mounting the drive
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 drive.mount('/content/gdrive')\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \cb3 #Setting kaggle configuration directory
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 os.environ['KAGGLE_CONFIG_DIR'] = "/content/gdrive/My Drive/Kaggle"\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 %cd /content/gdrive/My Drive/Kaggle\cf2 \cb1 \strokec2 \
\pard\pardeftab720\partightenfactor0

\f0\b \cf2 \cb3 #Downloading and unzip dataset
\f1\b0 \cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 !kaggle datasets download -d moltean/fruits\cf2 \cb1 \strokec2 \
\cf2 \cb3 \strokec2 !unzip \\*.zip && rm *.zip\cf2 \cb1 \strokec2 \
}