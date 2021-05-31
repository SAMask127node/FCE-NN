# [FCE-NN](https://ayaanzhaque.github.io/FCE-NN/)

This repository contains the implementation of the paper ["Simulated Data Generation Through Algorithmic Force Coefficient Estimation for AI-Based Robotic Projectile Launch Modeling"](https://arxiv.org/abs/2105.12833) by Sajiv Shah*, Ayaan Haque*, and Fei Liu.

We present FCE-NN, a novel method of modeling robotic launching of non-rigid objects using neural networks which are trained with supplemental simulated data, generated from algorithmic force coefficient estimation.

## Abstract

Modeling of non-rigid object launching and manipulation is complex considering the wide range of dynamics affecting trajectory, many of which may be unknown. Using physics models can be inaccurate because they cannot account for unknown factors and the effects of the deformation of the object as it is launched; moreover, deriving force coefficients for these models is not possible without extensive experimental testing. Recently, advancements in data-powered artificial intelligence methods have allowed learnable models and systems to emerge. It is desirable to train a model for launch prediction on a robot, as deep neural networks can account for immeasurable dynamics. However, the inability to collect large amounts of experimental data decreases performance of deep neural networks. Through estimating force coefficients, the accepted physics models can be leveraged to produce adequate supplemental data to artificially increase the size of the training set, yielding improved neural networks. In this paper, we introduce a new framework for algorithmic estimation of force coefficients for non-rigid object launching, which can be generalized to other domains, in order to generate large datasets. We implement a novel training algorithm and objective for our deep neural network to accurately model launch trajectory of non-rigid objects and predict whether they will hit a series of targets. Our experimental results demonstrate the effectiveness of using simulated data from force coefficient estimation and shows the importance of simulated data for training an effective neural network.

## Methods

![](https://github.com/ayaanzhaque/FCE-NN/blob/main/images/model_fig.png?raw=true)

## Results

## Code

Our scripts and code are provided in the repo. We provide the loop to perform force coefficient estimation as well as a barebones neural network with correct node configurations. However, we recommend this network is substituted with a deeper and more effective network. The force coefficient estimator code is in [```fce.py```](https://github.com/ayaanzhaque/FCE-NN/blob/main/fce.py).

## Citation

If you found our code or paper useful, please consider citing.

```
@misc{shah2021simulated,
      title={Simulated Data Generation Through Algorithmic Force Coefficient Estimation for AI-Based Robotic Projectile Launch Modeling}, 
      author={Sajiv Shah and Ayaan Haque and Fei Liu},
      year={2021},
      eprint={2105.12833},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```
