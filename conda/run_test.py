import imageio
from os.path import join as path_join

# Paths
resource_path = imageio.core.util.resource_dirs()[0]
images_path = path_join(resource_path, 'images')
astronaut_path = path_join(images_path, 'astronaut.png')
vid_path = path_join(images_path, 'realshort.mp4')

# Freeimage Test
astronaut_im = imageio.imread(astronaut_path)
freeimage_lib_path = imageio.plugins._freeimage.get_freeimage_lib()
freeimage_lib_fname = imageio.plugins._freeimage.FNAME_PER_PLATFORM[imageio.core.get_platform()]
assert freeimage_lib_path == path_join(resource_path, 'freeimage', freeimage_lib_fname)
assert astronaut_im.shape == (512, 512, 3)

# FFMPEG Test
vid = imageio.mimread(vid_path)
ffmpeg_exe_path = imageio.plugins.ffmpeg.get_exe()
ffmpeg_exe_fname = imageio.plugins.ffmpeg.FNAME_PER_PLATFORM[imageio.core.get_platform()]
assert ffmpeg_exe_path == path_join(resource_path, 'ffmpeg', ffmpeg_exe_fname)
assert len(vid) == 36
