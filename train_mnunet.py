import os

def train_model():

    """
    Train nnU-Net model on ToothFairy dataset
    """

    os.system(
        "nnUNetv2_train Dataset001_ToothFairy "
        "3d_fullres nnUNetTrainerV2 nnUNetPlansv2.1 "
        "-tr nnUNetTrainerV2 -device cuda"
    )


if __name__ == "__main__":
    train_model()
