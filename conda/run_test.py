import imageio
from os.path import join as path_join
from nose.tools import assert_equal


# Paths
resource_path = imageio.core.util.resource_dirs()[0]
images_path = path_join(resource_path, 'images')
astronaut_path = path_join(images_path, 'astronaut.png')
vid_path = path_join(images_path, 'realshort.mp4')

# Freeimage Test

# This comes back lower case! So we have to do .lower() on the outputs
actual_freeimage_lib_path = imageio.plugins._freeimage.get_freeimage_lib()
freeimage_lib_fname = imageio.plugins._freeimage.FNAME_PER_PLATFORM[imageio.core.get_platform()]
expected_freeimage_path = path_join(resource_path, 'freeimage', freeimage_lib_fname)
assert_equal(actual_freeimage_lib_path.lower(), expected_freeimage_path.lower())

astronaut_im = imageio.imread(astronaut_path)
assert_equal(astronaut_im.shape, (512, 512, 3))

# FFMPEG Test
# This comes back lower case! So we have to do .lower() on the outputs
actual_ffmpeg_exe_path = imageio.plugins.ffmpeg.get_exe()
ffmpeg_exe_fname = imageio.plugins.ffmpeg.FNAME_PER_PLATFORM[imageio.core.get_platform()]
expected_ffmpeg_exe_path = path_join(resource_path, 'ffmpeg', ffmpeg_exe_fname)
assert_equal(actual_ffmpeg_exe_path.lower(), expected_ffmpeg_exe_path.lower())

vid = imageio.mimread(vid_path)
assert_equal(len(vid), 36)

