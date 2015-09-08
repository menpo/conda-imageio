# Install using the setup.py
"$PYTHON" setup.py install --single-version-externally-managed --record=/tmp/record.txt

# Replace logic with cross-platform python script
# Copies the freeimage and ffmpeg to the resources folder
"$PYTHON" $RECIPE_DIR/copy_requirements_shim.py
 
