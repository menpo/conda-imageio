"%PYTHON%" setup.py install --single-version-externally-managed --record=%TEMP%record.txt

rem Cross platform copying logic
rem Copy freeimage and ffmpeg into resources folder
"%PYTHON%" %RECIPE_DIR%\copy_requirements_shim.py

if errorlevel 1 exit 1
