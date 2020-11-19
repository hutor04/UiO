1. Install the package blurring3110
Navigate to blurring3110 package directory
run "pip install ."
NOTE: Package must be installed so that all imports are properly resolved.

2. Tests are implemented using pytest package.
To run the test run command "py.test", alternatively navigate to /test directory and run test_blur.py

3. Make sure that the package is installed before trying to use blur.py

4. blur_image method is in module blur_image.py

5. blur_faces.py module contains a method main() that finds and blurs faces on a given image. Run the module
with ./blur_faces.py, test inputs are already provided.

5. /data folder contains test images and xml file for face recognition. Output images are stored in this folder.

(Note: blur_1.py, blur_2.py, blur_2.py could be written in less verbose form, but I chose this implementations,
since each of the files is a part of the task set and I presupposed that each module should be able to function
standalone.)