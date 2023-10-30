EDA:
run notebook EDA.ipynb

10% of train data moved to validation

Key findings:
1) classes frequencies in train and test are different
2) some symbols are unlabelled: check pictures with less than 7 objects
3) Objects are usually have similar size - easier to learn anchors.
4) Most pictures are aligned (sides are parallel to screen sides). But some are not
5) 90% of photos has resolution less than 630 x 324. Preprocessing with resize to 640 looks optimal 
6) objects are distributed on 

Training: 


Evaluation:
{'metrics/precision(B)': 0.9208474724456436,
 'metrics/recall(B)': 0.9656120747252827,
 'metrics/mAP50(B)': 0.9925618014464169,
 'metrics/mAP50-95(B)': 0.7770107902541031,
 'fitness': 0.7985658913733344}
Detection works good: MAP50 for each class is higher than 99 %.
Classification not perfect: some labels (Ground True) are missed. 


Next steps:
1) Data:
check and correct data. Some mislabelled cases found.
It lead to FalsePositive results and affects classification Precision.
Generate synthetic data
Get rid of low res photos


2) Models:
Try other nets: FasterRCNN, DETR, 
Try detectors pretrained on OCR. For example from PaddleOCR. 
