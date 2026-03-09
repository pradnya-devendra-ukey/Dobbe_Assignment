# 3D CBCT Tooth Segmentation & Visualization Pipeline

## 1. Problem Understanding

Cone Beam Computed Tomography (CBCT) scans provide high-resolution 3D volumetric images of dental structures.
The objective of this assignment is to build a pipeline that can process CBCT volumes and generate clinically meaningful segmentation outputs such as:

* FDI tooth identifiers
* jawbone separation
* dental restorations and implants
* anatomical structures such as maxillary sinus and inferior alveolar canal

The pipeline should also support visualization of the segmented structures in both slice-based and 3D rendering formats.

The dataset used for this task is **ToothFairy2**, a public CBCT segmentation dataset containing annotated volumetric scans.


## 2. Dataset

Dataset: **ToothFairy2 – Segmentation of Maxillofacial CBCT Volumes**
Reference: https://ditto.ing.unimore.it/toothfairy2/

Dataset structure:

imagesTr/   → CBCT scans (input volumes)
labelsTr/   → voxel-wise segmentation masks

Example pair:

imagesTr/ToothFairy2F_014_0000.mha
labelsTr/ToothFairy2F_014.mha

The labels correspond to anatomical structures and teeth using the **FDI numbering system**.


## 3. Pipeline Architecture

The overall system follows the pipeline below:

```
CBCT Volume (.mha / .nii / DICOM)
          ↓
Preprocessing (SimpleITK)
          ↓
Segmentation Model (3D CNN)
          ↓
Segmentation Mask Generation
          ↓
3D Visualization
```

### Components

1. **Input Handling**

   * Supports CBCT formats such as `.mha`, `.nii`, `.nii.gz`, and DICOM.

2. **Preprocessing**

   * Convert scans into NIfTI format when needed.
   * Load volumetric data using SimpleITK.
   * Prepare 3D tensor input for inference.

3. **Segmentation Model**

   * A lightweight 3D convolutional neural network is used for demonstration.
   * Model weights are stored in `models/model_weights.pth`.

4. **Inference**

   * The model processes the CBCT volume and generates a voxel-wise segmentation mask.
   * Output mask is exported as `mask.nii.gz`.

5. **Visualization**

   * PyVista is used for volumetric rendering.
   * Supports 3D surface extraction of segmented structures.

---

## 4. Project Structure

```
cbct-segmentation
│
├── models
│     model_weights.pth
│
├── demo
│     scan.nii.gz
│     mask.nii.gz
│
├── sample_data
│     ToothFairy2F_014_0000.mha
│
├── convert_to_nifti.py
├── predict.py
├── viewer.py
├── save_model.py
│
├── requirements.txt
└── README.md
```

---

## 5. Installation

Create a Python environment and install dependencies:

pip install -r requirements.txt

Main dependencies:

* SimpleITK
* PyVista
* VTK
* NumPy
* PyTorch

---

## 6. Running the Pipeline

### Step 1 – Convert CBCT scan to NIfTI

python convert_to_nifti.py imagesTr/ToothFairy2F_014_0000.mha demo/scan.nii.gz

---

### Step 2 – Run Model Inference

python predict.py

This generates the segmentation mask:

demo/mask.nii.gz

---

### Step 3 – Visualize Segmentation

python viewer.py

This launches an interactive 3D visualization showing:

* CBCT volume rendering
* segmented structures overlay

---

## 7. Demo Output

Example output folder:
demo/
   scan.nii.gz
   mask.nii.gz

These files demonstrate the inference pipeline on a sample CBCT volume.


