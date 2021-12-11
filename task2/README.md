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
  - Average Precision/Recall of each small/medium/big object<br />
  <img src="/task2/images/training_log.png" height = 1000> <br />
 <br />
  # Image Clasification:<br />
  Helmet and Mask is 2 attribute maybe inside the HeadObject. So this is a multi-label classification.<br />
  Build a model take the image input, feed to a CNN backbone to get the feature output.<br />
  At the last layer, instead of using Softmax solve nomal classification probject, we have to choose something like One-vs-rest approach to class multiple classes.<br />
  [SPECS]<br />
  - CNN BackBone: Resnet18<br />
  - Loss function: BCE + One-vs-rest<br />
 [Evaluation Metrics]:<br />
  - Micro Precision/Recall/F1_Score<br />
  - Macro Precision/Recall/F1_Score<br />
  <br /><br /><br />
  I spent alot of time to checking the data and recognize that the attribute inside data is very bad. A lot of data is mislabel, wrong label, Becase I only have 2 days so I just relabel half of them, and here is the comparetion between them .<br />
  [Training with raw datatset]<br />
  <img src="/task2/images/tensor_board.png" width = 1300> <br /> <br />
  [Training with relabel dataset]<br />
  <img src="/task2/images/tensor_board_relabel.png" width = 1300> <br />
  # Each Metrics increase 5%->8% accuracy. <br />
  I only relabel half of miss/wrong attributes and get a huge positive impart. So, data is realy importance in Computer Vison or AI field<br />
  <br />
  # Inference
  Checkout the `helmet_mask_end2end.ipynb` file for Inference with trained weight. But please don't expect to much, because I don't have enough time for find the best hyper parameters.
