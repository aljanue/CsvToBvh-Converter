# CSV to BVH Converter Addon for Blender

This Blender addon allows you to convert CSV files to BVH and import the resulting animation. BVH (Biovision Hierarchy) is a file format used for importing 3D motion data.

## Installation

1. Click on `<> Code` and Download the folder as `.zip`.
2. Compress the `converter_blender` folder into a `.zip` file.
3. Open Blender and go to `Edit > Preferences`.
4. In the preferences window, select the `Add-ons` tab.
5. Click on `Install...` and locate the `.zip` file you compressed.
6. Once installed, make sure the addon is enabled by checking the box next to its name.

## Usage

This addon adds a panel in the 3D viewport. To use it, follow these steps:

1. Once the addon is installed, you can find it in the 3D view in the "CSV to BVH" category.
2. In the "CSV to BVH" panel, click on the "Load and convert!" button.
A dialog box will open allowing you to select the CSV file you want to convert.
3. Select your CSV file and click on Accept. The addon will convert the CSV file to BVH and import the resulting animation.

## How it works

The `convert_csv_to_bvh` function in the `addon.py` script is the core of this addon. It takes a CSV file containing motion capture data and converts it into a BVH (BioVision Hierarchy) file, which can be used to import the motion data into Blender.

Here's a step-by-step breakdown of what the function does:

1. CSV Data Reading: The function opens the CSV file and reads its content. It looks for the 'Rotation Type' in the first few rows of the CSV file. The rotation type is used later to correctly interpret the rotation data in the CSV file. The function then reads the rest of the CSV file starting from the 9th row, which is assumed to contain the actual motion capture data.

2. BVH Data Writing: The function then opens the BVH file for writing. It starts by writing the BVH file header, which includes the hierarchy definition and the root joint ("Hips"). The root joint is assumed to have 6 channels: 3 for position (X, Y, Z) and 3 for rotation (X, Y, Z). The function then writes the 'MOTION' section of the BVH file, which includes the number of frames and the frame time. The number of frames is determined from the last row of the CSV data.

3. Motion Data Conversion: For each row in the CSV data, the function writes the position and rotation data to the BVH file. The position data is taken directly from the CSV file (columns 6, 7, 8). The rotation data is also taken from the CSV file (columns 2, 3, 4), but the order in which it is written to the BVH file depends on the rotation type. If the rotation type is 'ZXY', the rotation data is written in the order Z, X, Y. If the rotation type is 'Quaternion', the rotation data is converted from quaternion to Euler angles before being written to the BVH file.

The `open_bvh` function in the `addon.py` script is used to import a BVH file into the current Blender scene. It uses the `bpy.ops.import_anim.bvh` operator provided by Blender to import the BVH file.

These functions effectively transform motion capture data from a CSV format to a BVH format that can be used to animate 3D models in Blender, and provide a way to import the resulting BVH file into Blender.

