# YoloV4_python_custom-data  
1.1 Make photo from the video for labeling    
Next step By tools "YOLO-Annotation-Tool-master" make label  
1.2 Conver label from   "YOLO-Annotation-Tool-master" type to yolo type  
example     
C:/Users/image/101.jpg 24,16,52,31,0     





Problems  
1. For google colab change tf version
%tensorflow_version 1.x
2. K.control_flow_ops.while_loop to
tf.while_loop.
