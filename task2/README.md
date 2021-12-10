# Identify  if a person is wearing a face mask and a safety helmet
Acording to the annotation file, we have only one object localization is HEAD, and there are 2 attributes in this object is HELMET and MASK
The test says that I need to identify if a person wearing Helmet and Mark or not. So I set the wearing status is 0 and 1 ("wear" and "not_wear")
  - "wear" state include "wear right" and "wear wrong"
  - "not_wear" state include  "not wear" and "invisible" (invisible mean that if image is capture a person from behind, so cannot check that the person is wearing face mask or not)
 
 I seperate this problem by seperate the process into 2 steps:
  - Head Detection (Object Detection)
  - Identify Helmet and Mask (MultilClass Image Classification)
  
  The running flow is:
  - First, I build an object detection model to localize the region of HEAD
  - Then, Crop the HEAD region detected
  - Then, Build an image classification model to identify Helmet and Mask is exist inside the before Croped HEAD image
  - Finally, putting all together

# Head Detection
because the time to do the test is limited, So I choose an fastest way to build an object detection model is FasterRCNN. <br />
[SPECS]<br />
 - Backbone: Resnet50 (fine tune 3 last layers)
 - RPN
 - FPN: Because we need to detect both small and big object so FPN is make sense
 [Evaluation Metrics]
  - Precision/Recall of each small/medium/big object
  
