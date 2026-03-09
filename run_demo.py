import os

print("Running segmentation pipeline")

os.system("python inference/predict.py")

print("Opening visualization")

os.system("python visualization/viewer.py")
