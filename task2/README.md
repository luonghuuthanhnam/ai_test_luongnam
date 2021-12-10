# Identify  if a person is wearing a face mask and a safety helmet
Acording to the annotation file, we have only one object localization is HEAD. and there are 2 attributes in this object is HELMET and MASK
The test says that I need to identify if a person wearing Helmet and Mark or not. So I set the wearing status is 0 and 1 ("wear" and "not_wear")
  - "wear" state include "wear right" and "wear wrong"
  - "not_wear" state include  "not wear" and "invisible" (invisible mean that if image is capture a person from behind, so cannot check that the person is wearing face mask or not)
 
 I solve this problem by seperate the process into 2 steps:
  - Head Detection (Object Detection)
  - Identify Helmet and Mask (MultilClass Image Classification)
  
 First, I build an object detection model to localize the region of HEAD
 Then, Crop the HEAD region\n
 Then, Build an image classification model to identify Helmet and Mask in the before Croped HEAD image\n
 Finally, putting all together\n
