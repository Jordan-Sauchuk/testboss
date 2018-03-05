# BossSensor
Hide your screen when your boss is approaching.

## Demo
The boss stands up. He is approaching.

![standup](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/standup.jpg)

When he is approaching, the program fetches face images and classifies the image.
 
![approaching](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/approach.jpg)

If the image is classified as the Boss, it will monitor changes.

![editor](https://github.com/Hironsan/BossSensor/blob/master/resource_for_readme/editor.jpg)

## Requirements

* WebCamera
* Python3.5
* OSX
* Anaconda
* Lots of images of your boss and other person image

Put images into [data/boss](https://github.com/Hironsan/BossSensor/tree/master/data/boss) and [data/other](https://github.com/Hironsan/BossSensor/tree/master/data/other).

## Usage
First, Train boss image.

```
$ python boss_train.py
```

Second, start BossSensor. 

```
$ python camera_reader.py
```

## Install
Install OpenCV, PyQt4, Anaconda.

```
# 1. Create virtual environment using conda
conda create -n venv python=3.5
source activate venv


# 2. Install PyQt4
# PyQt4 can not be installed using pip
# So install it using conda
conda install pyqt=4


# 3. Install packages in requirements.txt
# Packages which can not be installed using pip, install them through conda
conda install scipy==0.18.1
conda install h5py==2.6.0

# Install other packages using pip
# Make sure isntall pip-windows unsupported packages using conda first
pip install -r requirements.txt


4. Install OpenCV
conda install -c https://conda.anaconda.org/menpo opencv3

# Ignore this command. This cause the version conflict 
# and after this command, pip is broken.
# https://stackoverflow.com/q/46499808/7906358
# conda install -c conda-forge tensorflow
```


## Fix some known issues on Windows
### AttributeError: module 'tensorflow.python' has no attribute 'control_flow_ops'

As discuess on [StackOverflow](https://stackoverflow.com/questions/40046619/keras-tensorflow-gives-the-error-no-attribute-control-flow-ops)

Detail issue: https://github.com/fchollet/keras/issues/3857

To fix it, edit `tendorflow_backend.py` file at
`<path-to-venv-virtual-environment>\lib\site-packages\keras\backend\tensorflow_backend.py` by adding this line `tf.python.control_flow_ops = tf`

tendorflow_backend.py
```python
[...]

tf.python.control_flow_ops = tf
# INTERNAL UTILS

[...]
```

Change Keras backend from Theano to TensorFlow. 

## Demo dataset
Run `boss_test_photo_generator.py` to generate boss photos, it will capture your face and save as images in `./data/boss` folder
## Licence

[MIT](https://github.com/Hironsan/BossSensor/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)
