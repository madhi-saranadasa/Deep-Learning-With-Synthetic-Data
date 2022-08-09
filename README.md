# Deep-Learning-With-Synthetic-Data
 
# Motivation
Computer vision is an exciting application within the field of deep learning. One important application is the assessment of disease status based on medical images, such as histopathology sections, radiology images, and colonoscopy videos. This assessment is typically performed by a trained physican, but training a neural network to perform the assessment can streamline the patient experience and reduce burden on the healthcare system. 

Below is an example of frames from colonoscopy videos where different kinds of lesions were identified (Yamada et al 2019). In the bottom left right image is a sessile serrated lesion with a characteristic shape and color. With enough labelled training data, we could develop a model to identify these lesions in new colonoscopy footage. However, collecting and hand-labelled enough training data can be expensive and time-consuming. 

![alt text](https://github.com/madhi-saranadasa/Deep-Learning-With-Synthetic-Data/blob/main/images/image1.png "Logo Title Text 1")

In this project, I developed a novel pipeline to randomly generate synthetic colonoscopy video frames using procedural modeling and texturing techniques used in the computer graphics field. This pipeline is parameterized to generate images that contain random lesions of various shapes, sizes, and colors. The synthetic data was then used to train a neural network to recognize lesions. This is a proof-of-concept that can be further leveraged in real world applications. 

# Procedural Modeling
