@echo off
REM Set up the Visual Studio environment using vcvars64.bat
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

REM Check if a filename was provided
if "%~1"=="" (
    echo Usage: buildcpp filename.cpp
    exit /b 1
)

REM Extract the base name without extension
set "filename=%~n1"

REM Compile the C++ file and output an executable with the same base name
cl "%~1" /Fe"%filename%.exe"
