# Brain Tumor Detection using CNN

This repository contains code and resources for training and using a Convolutional Neural Network (CNN) model to detect brain tumors. The model is implemented using Python and TensorFlow, and it can be executed in Google Colab.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Instructions](#instructions)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Model Prediction](#model-prediction)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Brain Tumor Detection using CNN is a project aimed at automating the process of detecting brain tumors in medical images. The implemented CNN model can analyze brain MRI scans and predict whether an image contains a brain tumor or not. The model achieves accurate results and can be a valuable tool in assisting medical professionals.

## Usage
To use this project, follow the instructions below to implement the model in Google Colab:

## Instructions
1. Open the [Google Colab](https://colab.research.google.com/) website.

2. If you are using the same dataset as me then download this dataset from kaggle https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection?resource=download then open the zipped file. There will be a file named "brain_tumor_dataset", copy and save it in a downloads or any other folder separately. Now make a folder named "dataset"  in colab and make two sub folders namely "yes" and "no". Now upload all the "yes" and "no" folder images by selectiong all, to their respective folders in colab from the folder "brain_tumor_dataset". Now run the code of "SplitCode.py" of this repository in colab. Make necessary folders in colab namely "train", "test", "validation" if required.

3. If you want to use your own dataset then, upload the dataset to Colab and divide the dataset into 'train','test' and 'validation' set by executing the code provided in the notebook's first section(code file name- "SplitCode.py". Ensure that your dataset is properly organized with "yes" and "no" folders containing brain tumor and non-brain tumor images, respectively.

4. Proceed to the second section of the notebook and run the code(file name- "BuildModel.py") to build, train, and save the CNN model. Modify the model architecture and hyperparameters according to your requirements.

6. Finally, execute the code in the last section (file_name- "Prediction.py") to predict whether an input image contains a brain tumor or not. Replace the path to the image file with your own test image file.

## Dataset
The dataset used for this project consists of brain MRI scans in two categories: images containing brain tumors (positive class) and images without brain tumors (negative class). You can create your own dataset or use publicly available brain tumor datasets.

Please ensure that the dataset is properly organized with separate folders for positive and negative images.

## Model Training
The CNN model architecture used for this project is provided in the notebook. It includes convolutional layers, pooling layers, and fully connected layers. The model is trained on the provided dataset using the Adam optimizer and categorical cross-entropy loss.

You can modify the architecture, hyperparameters, and training configuration to experiment and achieve better results for your specific use case.

## Model Prediction
After training the model, you can utilize it to make predictions on new brain MRI images. The notebook includes code to load the trained model and predict whether an input image indicates the presence of a brain tumor or no brain tumor.

Replace the path to the image file in the provided code with the path to your own test image, and the model will output the corresponding prediction.

## Contributing
Contributions to this project are welcome. Feel free to open issues for any questions or problems you encounter. If you have any suggestions for improvements or new features, you can also submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).

---


