# JOJO-Style-Transform

## Author
Team leader: Wei Hsiang Liao
Team members: 陳榮漢，Shao-Chi Li
<!--  &nbsp;  -->
## Abstract
We propose a Cycle Gan-based method that transform a general cartoon style to JOJO style.
We obersve that the charastic of JOJO style is more edge in image, so we comine a edge loss between fake image and real image to promote there are more edge in fake image.   


 
<div style="text-align: center">
<img src="https://i.imgur.com/KAqh53N.png"/{:height="20%" width="20%"}>　&emsp;
&rArr;　&emsp;
<img src="https://i.imgur.com/UxNas1T.png"/{:height="20%" width="20%"}>
</div>

## Installation
```
git clone 
cd 
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
## traing
* Training
```
python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan  --display_freq 1
```
## Results
<div style="text-align: center">
<img src="https://i.imgur.com/KAqh53N.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/UxNas1T.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://i.imgur.com/sq9UA5J.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/QyXv2fA.png"/{:height="15%" width="15%"}>
</div>

&nbsp;
<div style="text-align: center">
<img src="https://i.imgur.com/BIoVFjG.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/mo3Tc87.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://i.imgur.com/27kXLMh.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/N4AMi4R.png"/{:height="15%" width="15%"}>
</div>

&nbsp;
<div style="text-align: center">
<img src="https://i.imgur.com/sK4CFwp.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/F5VtUm7.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://i.imgur.com/S27BFCr.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/JQCH1hg.png"/{:height="15%" width="15%"}>

</div>

&nbsp;
<div style="text-align: center">
<img src="https://i.imgur.com/Wg3Q7jN.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/zkMiQKs.png"/{:height="15%" width="15%"}>
&emsp;&emsp;
<img src="https://i.imgur.com/IzUoRh5.png"/{:height="15%" width="15%"}>&nbsp; &rArr;
<img src="https://i.imgur.com/Aoyq2NN.png"/{:height="15%" width="15%"}>
</div>


