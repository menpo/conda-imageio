import imageio
import os
from os.path import join as path_join, exists as path_exists


def norm_path(filepath):
    return os.path.abspath(os.path.normpath(
        os.path.expandvars(os.path.expanduser(str(filepath)))))


def empty_dir(initial_root):
    for root, dirs, files in os.walk(initial_root, topdown=False):
        for name in files:
            os.remove(path_join(root, name))
        for name in dirs:
            os.rmdir(path_join(root, name))


def symlink(fpath, lpath, platform):
    if 'win' not in platform:
        os.symlink(norm_path(fpath), norm_path(lpath))
    else:  # win
        os.copy(norm_path(fpath), norm_path(lpath))


def get_conda_lib_path(platform):
    if 'win' in platform:
        return os.environ['LIBRARY_BIN']
    else:  # unix
        return path_join(os.environ['PREFIX'], 'lib')


def get_conda_bin_path(platform):
    if 'win' in platform:
        # Technically incorrect, but I put FFMPEG in Scripts
        return os.environ['SCRIPTS']
    else:  # unix
        return path_join(os.environ['PREFIX'], 'bin')


CONDA_FREEIMAGE_FNAME = {
    'osx32': 'libfreeimage.dylib',
    'osx64': 'libfreeimage.dylib',
    'win32': 'FreeImage.dll',
    'win64': 'FreeImage.dll',
    'linux32': 'libfreeimage.so',
    'linux64': 'libfreeimage.so',
}

CONDA_FFMPEG_FNAME = {
    'osx32': 'ffmpeg',
    'osx64': 'ffmpeg',
    'win32': 'ffmpeg.exe',
    'win64': 'ffmpeg.exe',
    'linux32': 'ffmpeg',
    'linux64': 'ffmpeg',
}
################################################################################
platform = imageio.core.get_platform()

SP_DIR = os.environ['SP_DIR']
PREFIX = os.environ['PREFIX']

# Manually link freeimage and ffmpeg ourselves (soft link)
IMAGEIO_RESOURCE_DIR = path_join(SP_DIR, 'imageio', 'resources')
IMAGEIO_FREEIMAGE_DIR = path_join(IMAGEIO_RESOURCE_DIR, 'freeimage')
IMAGEIO_FFMPEG_DIR = path_join(IMAGEIO_RESOURCE_DIR, 'ffmpeg')

# Freeimage
FREEIMAGE_FNAME = imageio.plugins._freeimage.FNAME_PER_PLATFORM[platform]
if not path_exists(IMAGEIO_FREEIMAGE_DIR):
    os.mkdir(IMAGEIO_FREEIMAGE_DIR)

# Remove shipped freeimage
empty_dir(IMAGEIO_FREEIMAGE_DIR)
# Softlink conda freeimage
symlink(path_join(get_conda_lib_path(platform), CONDA_FREEIMAGE_FNAME[platform]), 
        path_join(IMAGEIO_FREEIMAGE_DIR, FREEIMAGE_FNAME),
        platform)

# FFMPEG
FFMPEG_FNAME = imageio.plugins.ffmpeg.FNAME_PER_PLATFORM[platform]
if not path_exists(IMAGEIO_FFMPEG_DIR):
    os.mkdir(IMAGEIO_FFMPEG_DIR)

# Remove shipped ffmpeg
empty_dir(IMAGEIO_FFMPEG_DIR)
# Softlink conda ffmpeg
symlink(path_join(get_conda_bin_path(platform), CONDA_FFMPEG_FNAME[platform]),
        path_join(IMAGEIO_FFMPEG_DIR, FFMPEG_FNAME),
        platform)


