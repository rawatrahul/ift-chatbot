ift-chatbot
===================

Table of Contents
-------------
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Dataset preparations](#dataset-preparations)
4. [Screenshots](#screenshots)

Introduction
-------------

ift-chatbot is the implementation of chatbot using NMT - Neural Machine Translation (seq2seq). Includes BPE/WPM-like tokenizator. Main purpose of this project is to make a chatbot to help students get information from the depratment in a conversational manner.

The code is built on top of NMT but because of lack of available interfaces, some things are "hacked", and parts of the code had to be copied into that project (and will have to be maintained to follow changes in NMT).

This project forks NMT. We had to make a change in our code allowing the use of a stable TensorFlow (1.4) version. Doing so allowed us also to fix some bug before official patch as well as do couple of necessary changes.


Setup
-------------

Steps to setup project for your needs:
It is *highly* recommended that you use Python 3.6+.

 1. ```$ git clone https://github.com/rawatrahul/ift-chatbot.git```  
    
 2. ```$ cd ift-chatbot```
 3. ```$ pip install -r requirements.txt``` TensorFlow-GPU is one of the requirements. You also need CUDA Toolkit 8.0 and cuDNN 6.1.
 4. ```$ cd nmt_chatbot```
 5.  ```$ pip install -r requirements.txt``` 
 
 Dataset preparations
-------------
Datasets can be downloaded from https://files.pushshift.io/reddit/comments/

We used comments for month 0f 2018-08 if you have more powerful computeryou can use multiple months comments to make chatbot more intelligent.
 Download dataset and extract.
 ####Steps 
 (This may take time depending on your computer for i7/16GB RAM/ 6GB VRAM it took around 4 hours)
 1. From project root run `$ python chatbot_database.py`
 2. Now run `$ python create_datasets.py` this will give you test.to, test.from, train.to and train.from files.

 Train chatbot
-------------
1. Place training data inside "new_data" folder under nmt_chatbot
2. `$ python prepare_data.py` ...Run setup/prepare_data.py - a new folder called "data" will be created with prepared training data
3. `$ cd ../`
4. `$ python train.py` Begin training



Screenshots 
----------------------------------
![Minimized](/extras/1.PNG?raw=true "Minimized")
![Maximized](/extras/2.PNG?raw=true "Maximized")

