import SimpleITK as sitk

scan_path = "demo/scan.nii.gz"
label_path = "labelsTr/ToothFairy2F_014.mha"
output_path = "demo/mask.nii.gz"

# load label
mask = sitk.ReadImage(label_path)

# save as nifti mask
sitk.WriteImage(mask, output_path)

print("Mask saved to:", output_path)