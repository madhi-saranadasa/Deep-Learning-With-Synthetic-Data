# Deep-Learning-With-Synthetic-Data
 
# Motivation
Computer vision is an exciting application within the field of deep learning. One important application is the assessment of disease status based on medical images, such as histopathology sections, radiology images, and colonoscopy videos. This assessment is typically performed by a trained physican, but training a neural network to perform the assessment can streamline the patient experience and reduce burden on the healthcare system. 

Below is an example of frames from colonoscopy videos where different kinds of lesions were identified (Yamada et al 2019). In the bottom right image is a sessile serrated lesion with a characteristic shape and color. With enough labelled training data, we could develop a model to identify these lesions in new colonoscopy footage. However, collecting and hand-labelled enough training data can be expensive and time-consuming. 

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Picture0.png "Example colonoscopy images")

In this project, I developed a novel pipeline to randomly generate synthetic colonoscopy video frames using procedural modeling and texturing techniques used in the computer graphics field. This pipeline is parameterized to generate images that contain random lesions of various shapes, sizes, and colors. The synthetic data was then used to train a neural network to recognize lesions. This is a proof-of-concept that can be further leveraged in real world applications. 

# Procedural Modeling 
The Geometry Nodes system in Blender was used in conjunction with procedural materials developed in Substance Designer. The basic idea is shown below - first base geometry is constructed in Blender and procedural textures developed in Substance Designer are applied to the mesh to generate the inner lumen of the colon. 

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Picture1.png "Procedural modeling workflow")

# Parameterized Lumen
The appearance of the lumen is parameterized within the Substance Designer graph. The lesion status, size, color, and height can be randomized as well as the vascular density and color. By randomly generating images through procedural texturing, it is possible to create a diverse image set than can be used to train a robust and generalized neural network. In the example below, the same lumen is modified with increasing lesion height and increasing vascularity.

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Picture2.png "Parameterized Lumen")

# Training a neural network
For this project, I randomly generated roughly 8000 images of lumens with and without lesions. The lesions were further randomly assigned a size, color, and height. The benefit of this approach is that the pipeline knows a priori the label of the image and therefore the time-consuming process of hand-labeling is avoided!

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Picture2.png "Training a neural network 1")

Next, I developed a convolutional neural network using PyTorch to classify normal vs. lesion images. The architecture is a fairly simply implementation containing 3 convolutional layers with a 2x2 pixel kernel, followed by a dense layer with 512 nodes, and an output layer with 2 nodes (for each prediction class: normal vs. lesion). As shown below, after 3 epochs of training with a batch size of 100, the neural network was highly accurate in the hold-out validation set.

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Performance.png "Training a neural network 2")

# Future directions
In this project, I've developed a novel pipeline to generate synthetic data for medical computer vision tasks. Although the images are not true colonoscopy frames, this synthetic data can be used in transfer learning. In this application, the general concepts will be learned by the network using synthetic data, after which real data can be shown to the model for fine-tuning. This can be especially useful where real data is rare or expensive to collect. 

Finally, the pipeline can be further developed for more specific tasks. For example, the shaders I used in Blender can be manipulated to generated a automatic segmentation mask. This can be useful in object detection tasks where manual annotation of the segmentation mask or bounding box is very expensive and time consuming.

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/Picture4.png "Segmentation mask")

Thanks for reading!
