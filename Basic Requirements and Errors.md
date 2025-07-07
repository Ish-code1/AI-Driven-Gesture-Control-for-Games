# Basic Requirements

-	__Install python 3.8__ –  python 3.10 and up do not support mediapipe.\
You can get error like : ImportError: DLL load failed while importing _framework_bindings: A dynamic link library (DLL) initialization routine failed.

Now, in cmd of vscode(preferably) type the following after the name of folder:
-	To create virtual environment named hand-gesture-env in 3.8:
   **py -3.8 -m venv hand-gesture-env**  
-	Activate venv : **hand-gesture-env\Scripts\activate**

### Libraries: 
-	pip install opencv
-	pip install mediapipe
-	pip install autopy
-	pip install numpy
-	pip install PyDirectInput
-	pip install protobuf\
**these are to be installed inside the virtual environment**

# Common Errors And Solutions

-	Type : **pip list** to   see list of installed libraries
-	**_If error arises:_** reportMissingImports\
   **Ctrl + Shift + P   →  Python: Select Interpreter    →  .\hand-gesture-env\Scripts\python.exe**\
 - **_AttributeError_**: partially initialized module ...\
**Move the Code Out of the venv Folder**
-	**_Other Errors_**: cv2.gapi_wip_gst_GStreamerPipeline\
	[ OpenCV is trying to access an internal GStreamer component (cv2.gapi_wip_gst_GStreamerPipeline) that isn’t properly available,
 possibly due to a corrupted or incompatible installation.] \
**Downgrade OpenCV : opencv-python==4.9.0** 
- TO CHECK , type  : import cv2\
print(cv2.__version__)

Your terminal should look like this:   
(hand-gesture-env) PS C:\Users\DELL\Desktop\folder name>
