[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

# YOLOv3 !
everything files stored in the root directory are components of yolov3.

The darknet weightset is required and available below :
  - https://pjreddie.com/media/files/yolov3.weights

 yolo_object_detection.py is the main file to run the algorithm.
the folder get_images will be used later and is not mandatory to run the yolov3 classic algorithm

# Custom objects section (needs improvements) !

  - get_images folder contains :
    * get_images.py : features to download (in bad quality) pictures based on google images 
    * draw_box.py : design interactive box to annotate pictures downloaded with get_images.py
    * generate_xml.py : create xml files specifying locations of the box in each picture
 