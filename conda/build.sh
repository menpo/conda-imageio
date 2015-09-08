# Install using the setup.py
"$PYTHON" setup.py install --single-version-externally-managed --record=/tmp/record.txt

# Manually link freeimage ourselves (soft link)
IMAGEIO_RESOURCE_DIR="${SP_DIR}/imageio/resources"
IMAGEIO_FREEIMAGE_DIR="${IMAGEIO_RESOURCE_DIR}/freeimage"

mkdir -p ${IMAGEIO_FREEIMAGE_DIR}
# Remove shipped freeimage
rm ${IMAGEIO_FREEIMAGE_DIR}/*.so
# Softlink conda freeimage
ln -s "${PREFIX}/lib/libfreeimage.so" ${IMAGEIO_FREEIMAGE_DIR}

