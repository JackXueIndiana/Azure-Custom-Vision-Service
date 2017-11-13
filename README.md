# Azure-Custom-Vision-Service
Azure Custom Vision Service is a tool for building custom image classifiers. It makes it easy and fast to build, deploy, and improve an image classifier. A REST API and a web interface have been provided to upload your images and train. As long as the interested object is sustain in the images, you only need less than 50 images to initially try a classifier. 

In our example we use the web interface and upload 20 images (10 labled as positive aka the object present and the other 10 negative, aka the object is absent) to train the classifier. We then use REST call to upload unseen images to the classifier that can pretty accurately classify the unseen images. Moreover, for the positive images we use CV2 to further identify the location of the object in the image.

