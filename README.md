# scale_tag_img

The main intention of this project was to create re-scaled AprilTags for experiment purpose.
However, it works on any image that you wan resize. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites and their Installation

* [OpenCV](https://opencv.org/)
* [python](https://www.python.org/download/releases/2.7/)
* optional (not required if you want to resize image other than Apriltag)
    >  [apriltag library](https://pypi.org/project/apriltag/)
    >
    >[apriltagpictures] (https://april.eecs.umich.edu/media/apriltag/tag36h11.tgz)
        
        **Note : above link provide link to 36h11 family.**


### Running the test


1. Download/Clone in any folder.
2. Go to the directory in your command terminal where you cloned/downloaded
3. type the following line:
        chmod +x scaling_tag_img_main.py scaling_tag_img_cmd_tr.py scaling_tag_img_res.py

   default(without any argument): rescales image.png by 200
        python scaling_tag_img_main.pym

##### Available argument: -i/-f/-d, --rs, --p, --ds
-i/--image : to rescale image  
-f/--file  : to rescale all images in file  
-d/--default : takes default if -i/-f is not specified
--rs : rescale size  
--p  : path to image/images (takes "image.png" by default)  
--ds : destination for re-sized image ( takes current folder by default)

### Examples :

 * To resize image.png in current folder.
 >
      python scaling_tag_img_main.py -i

 * To resize all images in directory tag36h11 which is located in the same directory as this file:
 >     
    python scaling_tag_img_main.py -f

 * To resize change resize scale: takes int at the place of scale size  
 python scaling_tag_img_main.py --rs scale_size  i.e
 >
     python  python scaling_tag_img_main.py --rs 500

Few more examples:   
from your_file
 >
     python  python scaling_tag_img_main.py -i --rs 1000 --p path_to_your_file

 to your_file_2
 >
    python  python scaling_tag_img_main.py --rs scale_size --p  path_to_your_file --ds path_to_your_file_2


**Note** : **By default it takes image.png in current directory or tag36h11 in current directory.** 

Author : Sandeep Chahal (schahal@fetchrobotics.com/sandeepchahal@mavs.uta.edu) for any question.

