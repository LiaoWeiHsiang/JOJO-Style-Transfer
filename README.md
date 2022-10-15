# JOJO-Style-Transfer

<!--  &nbsp;  -->
## Abstract
We propose a Cycle Gan-based method that transform a general cartoon style to JOJO style.
<!--- 
We obersve that the charastic of JOJO style is more edge in image, so we comine a edge loss between fake image and real image to promote there are more edge in fake image.
-->


 
<div style="text-align: center">
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/1-1.png"/{:height="20%" width="20%"}>　&emsp;  
&rArr;　&emsp;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/1-2.png"/{:height="20%" width="20%"}>  
</div>

## Installation
```
git clone https://github.com/zxc741852741/JOJO-Style-Transfer.git
cd JOJO-Style-Transfer
conda env create -f environment.yml
pip install -r requirements.txt
```
## Dataset 
All data are collected on internet by ourselves
Download link: https://drive.google.com/file/d/1CJ6GzOgrQr16W9MNRzCsdDSsmfOet2cN/view?usp=sharing
```
JOJO
├── datasets
│   ├── maps
│   │   │── trainA
│   │   │   ├──0.png
│   │   │   ├──1.png
│   │   │   ├──...
│   │   │── train2
│   │   │   ├──0.png
│   │   │   ├──1.png
│   │   │   ├──...
├── models
├── data
```
## Training
* Training
```
python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan  --display_freq 1
```
* Resume training
```
python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan --continue_train --display_freq 1
```

## Results
<div style="text-align: center">
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/1-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/1-2.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/2-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/2-2.png"/{:height="15%" width="15%"}>
</div>

&nbsp;
<div style="text-align: center">
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/3-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/3-2.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/4-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/4-2.png"/{:height="15%" width="15%"}>
</div>

&nbsp;
<div style="text-align: center">
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/5-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/5-2.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/6-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/6-2.png"/{:height="15%" width="15%"}>

</div>

&nbsp;
<div style="text-align: center">
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/7-1.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/7-2.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/8-2.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://github.com/zxc741852741/JOJO-Style-Transfer/blob/main/document/8-1.png"/{:height="15%" width="15%"}>
</div>

## Author
Wei-Hsiang Liao, Jung-Han Chen, Shao-Chi Li
