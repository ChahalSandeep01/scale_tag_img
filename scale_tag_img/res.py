import cv2
import glob
import sys


class ResizingImagesDetails:
    def __init__(self, resizing_scale):
        self.valid_images = [".png", ".jpg", ".jpeg", ".tga"]
        self.default_image = "image.png"
        self.write_image = "new_image.png"
        self.res_scale = resizing_scale
        self.count = 0

    def writing_image(self, path_to_destination, name_of_image, new_image):
        """

        :param path_to_destination: String/None
         folder to write new_image, in case of not specified writes to current folder
        :param name_of_image: String/None
        name of image while storing.
        writes new_ + old image name in case of pictures are loaded from same folder which they are writen to.
        :param new_image: numpy array
        the image to be stored.
        :return: None
        """

        if path_to_destination is None and name_of_image is None:
            cv2.imwrite(self.write_image, new_image)

        elif path_to_destination is not None and name_of_image is None:
            cv2.imwrite(path_to_destination + "/" + self.write_image, new_image)

        elif path_to_destination is None and name_of_image is not None:
            cv2.imwrite("new_" + name_of_image, new_image)

        elif path_to_destination is not None and name_of_image is not None:
            cv2.imwrite(path_to_destination + "/" + name_of_image, new_image)

    def rescaling_image(self, my_image):
        """

        :param my_image: numpy array
        any image
        :return: re-scaled image
        numpy array
        """
        width = int(my_image.shape[1] * self.res_scale / 100)
        height = int(my_image.shape[0] * self.res_scale / 100)
        dim = (width, height)
        return cv2.resize(my_image, dim, interpolation=cv2.INTER_AREA)

    def loading_image(self, my_path, name_of_image):
        """

        :param my_path: String/None
         path to image, in case considers current folder
        :param name_of_image: String/None
        name of image, in case of none considers self.default_name
        :return: loaded image
        """
        print "loading_image.........."

        if my_path is None and name_of_image is None:
            my_image = cv2.imread(self.default_image)
        elif my_path is not None and name_of_image is None:
            my_image = cv2.imread(my_path + self.default_image)
        elif my_path is not None and name_of_image is not None:
            my_image = cv2.imread(my_path + name_of_image)
        else:  # none , not none
            my_image = cv2.imread(name_of_image)

        if my_image is None:
            print "ImagenotFoundError: image.png not found.Likely issue with either of these\n" \
                  "[11 if running with default/" \
                  "image option you don't have image.png in current directory.\n " \
                  "[2] if -f option is provided the path is not correct"

            sys.exit()

        else:
            return my_image

    def from_file(self, path_to_image, path_to_destination):
        """

        :param path_to_image:String/None
         path to image
        :param path_to_destination: String/None
        path to directory you want to store new images
        :return: 
        """
        for my_image_full_path in glob.glob(path_to_image + "/*.*"):
            # to check for .png .jpg .tga and jpeg
            if my_image_full_path[my_image_full_path.rfind("."):] in self.valid_images:
                name_of_image = my_image_full_path[my_image_full_path.rfind("/") + 1:]
                path_to_this_image = my_image_full_path[:my_image_full_path.rfind("/") + 1]
                # loading image
                print "loading image no ", self.count
                my_image = self.loading_image(path_to_this_image, name_of_image)
                print "Image loaded.... \n Rescaling image"
                # rescaling_image
                rescaled_image = self.rescaling_image(my_image)
                # writing image
                print "Image rescaled...."
                self.writing_image(path_to_destination, name_of_image, rescaled_image)
                print "Writing image to file"
                print "..............success..............."
                self.count = self.count + 1
        print "Number of images resized are : ", self.count

    def image_func(self, fi_or_ig, path_to_image, path_to_destination):
        """

        :param fi_or_ig: single image or all images in file
        :param path_to_image: path to directory where image/images are present
        :param path_to_destination: path to directory you want to store new images
        :return: 
        """

        if fi_or_ig == "default" or fi_or_ig == "image":  # by default re-sizes the image.png in the folder
            print "...................executing default............................"
            #  loading image
            name_of_image = None
            my_image = self.loading_image(path_to_image, name_of_image)
            print "Image loaded.... \n Rescaling image"
            # rescaling_image
            rescaled_image = self.rescaling_image(my_image)
            print "Image rescaled...."
            # writing image
            print "Writing image to file"
            self.writing_image(path_to_destination, name_of_image, rescaled_image)
            print "Success with an image"

        elif fi_or_ig == "file":
            if path_to_image is None:  # by default looks for tag36h11
                try:
                    self.from_file("tag36h11", path_to_destination)
                except Exception as e:
                    print e
                    print "this file does not contain tag36h11 directory"
            else:
                self.from_file(path_to_image, path_to_destination)