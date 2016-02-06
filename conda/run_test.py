import imageio
from os.path import join as path_join
from nose.tools import assert_equal


# Paths
platform = imageio.core.get_platform()
resource_path = imageio.core.util.resource_dirs()[0]
images_path = path_join(resource_path, 'images')
astronaut_path = path_join(images_path, 'astronaut.png')
vid_path = path_join(images_path, 'realshort.mp4')

# Freeimage Test
astronaut_im = imageio.imread(astronaut_path)
assert_equal(astronaut_im.shape, (512, 512, 3))

# FFMPEG Test
# This comes back lower case! So we have to do .lower() on the outputs
vid = imageio.mimread(vid_path)
assert_equal(len(vid), 36)

