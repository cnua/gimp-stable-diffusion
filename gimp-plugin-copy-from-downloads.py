import os
import shutil

# Define the paths
download_folder = os.path.expanduser('C:/Downloads/gimp-stable-diffusion-main/stablehorde')
gimp_plugin_folder = os.path.expanduser('C:/Users/{you-username}/AppData/Roaming/GIMP/2.10/plug-ins')  # Update the path as necessary

# Name of the plugin file you downloaded
plugin_file_name = 'gimp-stable-diffusion-horde.py'  # Replace with the actual plugin file name

# Full paths
source_file = os.path.join(download_folder, plugin_file_name)
destination_file = os.path.join(gimp_plugin_folder, plugin_file_name)

# Copy the plugin file
if os.path.exists(source_file):
    shutil.copy(source_file, destination_file)
    print(f"Copied {plugin_file_name} to GIMP plugin folder.")
else:
    print(f"{plugin_file_name} not found in {download_folder}.")
