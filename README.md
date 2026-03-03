VISION SPEC QC
Deep Learning-Based Surface Defect Detection System

Internship Project Report
Submitted by: SK Salma
Under the Guidance of: Infotact Solutions

📌 Abstract

Industrial quality inspection plays a critical role in ensuring product reliability, safety, and performance. Traditional manual inspection systems are slow, inconsistent, and prone to human error.

This project presents Vision Spec QC, a deep learning-based surface defect detection system designed to classify industrial surface images into Pass and Defect categories.

Transfer learning using MobileNetV2 was implemented to enhance performance while reducing training time.

The system achieved a peak validation accuracy of 92.49%, demonstrating strong generalization capability and suitability for real-world industrial deployment.

🏭 Introduction

Automated quality control systems are essential in modern manufacturing industries. Surface defect detection ensures structural integrity and optimal product performance.

Convolutional Neural Networks (CNNs) have significantly improved image classification tasks. This project explores:

CNN model built from scratch

Transfer learning using MobileNetV2

Performance comparison and optimization

The objective is to develop a reliable AI-driven inspection system.

❗ Problem Statement

Manual inspection systems suffer from:

Human fatigue and inconsistency

Subjective judgment errors

Slow inspection speed

High operational cost

The goal is to design an automated deep learning system that:

Improves inspection accuracy

Reduces operational cost

Increases inspection speed

Provides scalable industrial deployment

🎯 Objectives

Design a CNN-based binary classification model

Implement transfer learning using MobileNetV2

Achieve high validation accuracy

Build a scalable and deployable inspection framework

📂 Dataset Description

Dataset Used: Magnetic Tile Surface Defect Dataset

Original Classes:

MT Blowhole

MT Break

MT Crack

MT Fray

MT Free (Normal)

For practical deployment, the dataset was converted into:

Defect (All defect classes merged)

Pass (MT Free)

Preprocessing Steps:

Image resizing: 128 × 128 pixels

80% Training / 20% Validation split

Data augmentation applied

🛠 Tools & Technologies

Python

TensorFlow

Keras

MobileNetV2

Google Colab

NumPy

Matplotlib

🏗 System Architecture

Image Acquisition

Image Preprocessing

Feature Extraction

Classification Layer

Output Prediction

🔬 Model Development & Experimental Results
1️⃣ CNN From Scratch
Architecture

Conv2D (32 filters, 3×3) + ReLU

MaxPooling (2×2)

Conv2D (64 filters, 3×3) + ReLU

MaxPooling (2×2)

Conv2D (128 filters, 3×3) + ReLU

MaxPooling (2×2)

Flatten

Dense (128, ReLU)

Dropout (0.5)

Sigmoid Output

Total Parameters: 3,304,769

Training Configuration

Optimizer: Adam

Loss Function: Binary Crossentropy

Batch Size: 16

Epochs: 5

Training Results
Epoch	Train Acc	Val Acc
1	0.6467	0.8728
2	0.7992	0.9017
3	0.8236	0.9249
4	0.8695	0.9191
5	0.8598	0.9075

✅ Peak Validation Accuracy: 92.49%

2️⃣ Transfer Learning Using MobileNetV2
Architecture

MobileNetV2 (ImageNet Pretrained Weights)

Global Average Pooling

Dense (128, ReLU)

Dropout (0.3)

Sigmoid Output

Total Parameters: 2,422,081

Training Results
Epoch	Train Acc	Val Acc
1	0.6994	0.9075
2	0.8538	0.8960
3	0.8509	0.9191
4	0.8779	0.9075
5	0.8867	0.9017

✅ Peak Validation Accuracy: 91.91%

📊 Comparative Analysis

Scratch CNN achieved slightly higher peak accuracy

MobileNetV2 showed more stable convergence

Transfer learning required fewer parameters

Faster training time

Better scalability for industrial deployment

📈 Additional Classification Metrics

From evaluation:

Overall Accuracy: 67% (Test Set)

Strong detection of Defect class

Lower recall for Normal class (due to class imbalance)

Future improvement:

Class balancing

Advanced augmentation

Threshold tuning

📊 Model Evaluation & Analysis
1️⃣ Confusion Matrix Analysis

The confusion matrix evaluates the classification performance of the defect detection model on unseen test data.
![Confusion Matrix](images/confusion_matrix.png)

Key Observations:

The model correctly identified 116 Defect samples

The model failed to classify Normal samples properly

Class imbalance affected prediction capability

High recall for Defect class

Low precision and recall for Normal class

This indicates the model is highly sensitive to defect detection but requires balancing techniques for improved generalization.

2️⃣ Transfer Learning Performance (MobileNetV2)

Transfer learning was implemented using pretrained ImageNet weights.

![Transfer Learning Graph](images/transfer_learning_graph.png)

Observations:

Faster convergence compared to scratch CNN

Stable validation accuracy across epochs

Reduced number of trainable parameters

Suitable for scalable industrial deployment

Computationally efficient

Peak Validation Accuracy: 91.91%

3️⃣ CNN Model Accuracy Trends

The CNN built from scratch demonstrated:

Gradual improvement in training accuracy

Strong validation performance

Slight overfitting at later epochs

High learning capability on binary defect classification

Peak Validation Accuracy: 92.49%

![Model Accuracy Graph](images/model_accuracy_graph.png)

4️⃣ Output Heatmap Interpretation

Model visualization techniques highlight activated regions in defective images.

Insights:

The model focuses on crack/fracture regions

Feature extraction layers detect texture irregularities

Heatmap visualization improves explainability

Useful for industrial validation and auditing

✅ Conclusion

The Vision Spec QC system demonstrates that both CNN from scratch and transfer learning approaches are effective for surface defect detection.

While the scratch CNN achieved the highest peak validation accuracy (92.49%), transfer learning using MobileNetV2 offers:

Computational efficiency

Faster convergence

Easier deployment

Better scalability

The system is suitable for real-time industrial quality control applications.

🚀 Future Scope

Grad-CAM for model explainability

TensorFlow Lite deployment

OpenCV integration for real-time inspection

Edge AI deployment on embedded systems

Multi-class defect detection

📚 References

Howard et al., MobileNets, 2017

Sandler et al., MobileNetV2, CVPR 2018

Goodfellow et al., Deep Learning, MIT Press

Krizhevsky et al., ImageNet Classification, NIPS 2012

TensorFlow Documentation
