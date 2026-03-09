import SimpleITK as sitk
import sys
import os

def convert_to_nifti(input_path, output_path):
    """
    Converts CBCT input formats (.mha, DICOM, etc.) to .nii.gz
    """

    if os.path.isdir(input_path):
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(input_path)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
    else:
        image = sitk.ReadImage(input_path)

    sitk.WriteImage(image, output_path)
    print("Saved NIfTI:", output_path)


if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    convert_to_nifti(input_path, output_path)