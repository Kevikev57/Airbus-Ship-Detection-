# Airbus-Ship-Detection-
I attempted the Kaggle Airbus Ship Detection Challenge to show my level of compentancy with image segmantation
## Overview ##
The goal of this challenge is to build a machine learning model to anaylze satelite images of container ships, located the ships and put a bounded box segment around them. By evaluating the F2 score at different intersection over union (IoU) threshold. The algorithm will sweep through a range of IoU and calculate the F2 score at each point(pixel). Each score is deteremined by the number of true positives(TP),false positives(FP) and false negativee(FN). A TP indicates a single preedicted object matches a ground truth object, FP shows a predicted object has no associated ground truth object and FN sa a ground truth object has no associated predictions. With this the average F2 score is calcualted. 

## Solution ##
The solution was implemented by using the U-net architecture. Which is a convolutional neural network that operates by downsampling and encoding the information in the image and than later upsampling and decoding the collected information from the same image.

## Dependencies ##
* Python 3.8.16
* Tensorflow 2
* Jupyter Notebook


## Resources ## 
* [U-net Model](https://www.kaggle.com/code/hmendonca/u-net-model-with-submission)
* [Dmitry Larko,- Kaggle Airbus Ship Detection Challenge Slides](https://www.slideshare.net/0xdata/dmitry-larko-h2oai-kaggle-airbus-ship-detection-challenge-h2o-world-san-francisco)
* [Jeff Heaton Deep Learning](https://github.com/jeffheaton/t81_558_deep_learning)
* [Cynical Learning Rate](https://github.com/bckenstler/CLR)
* [Albumentationns](https://github.com/albumentations-team/albumentations/blob/master/README.md)
* [Kaggle Meetup Ship Detection Challenge](https://www.youtube.com/watch?v=QXEy4rdLsDw)  
* [Dmitry Larko, H2O.ai - Kaggle Airbus Ship Detection Challenge](https://www.youtube.com/watch?v=0Opb8gB1p4w)
*[2021, Installing TensorFlow 2.4, Keras, & Python 3.8 in Mac OSX Intel](https://www.youtube.com/watch?v=LnzgQr14p7s&list=PL0vtEDTTf8RBicJnmjeVgT7HBaRl0AyVP&index=3)
*[Github Readme Cheatsheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
