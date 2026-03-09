import SimpleITK as sitk
import pyvista as pv

scan_path = "imagesTr/ToothFairy2P_548_0000.mha"
mask_path = "labelsTr/ToothFairy2P_548.mha"

scan = sitk.ReadImage(scan_path)
mask = sitk.ReadImage(mask_path)

scan_array = sitk.GetArrayFromImage(scan)
mask_array = sitk.GetArrayFromImage(mask)

grid = pv.ImageData()
grid.dimensions = scan_array.shape

grid["scan"] = scan_array.flatten(order="F")
grid["mask"] = (mask_array > 10).astype(int).flatten(order="F")

p = pv.Plotter()
p.add_volume(grid, scalars="scan", opacity="sigmoid")
p.add_mesh(grid.contour([1], scalars="mask"), color="red")

p.show()