import imageio
from os.path import join as path_join


resource_path = imageio.core.util.resource_dirs()[0]
images_path = path_join(resource_path, 'images', 'astronaut.png')

astronaut_im = imageio.imread(images_path)
assert astronaut_im.shape == (512, 512, 3)

