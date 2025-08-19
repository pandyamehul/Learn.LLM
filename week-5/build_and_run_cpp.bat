@echo off
REM Batch file to compile and run a C++ file using MSVC and vcvars64.bat

REM Check if a filename was provided
IF "%~1"=="" (
    echo [ERROR] No C++ source file provided.
    echo Usage: build_and_run_cpp.bat filename.cpp
    exit /b 1
)

REM Set up the MSVC environment
CALL "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat"
IF ERRORLEVEL 1 (
    echo [ERROR] Failed to set up MSVC environment. Please check the path to vcvars64.bat.
    exit /b 1
)

REM Compile the C++ file
cl "%~1"
IF ERRORLEVEL 1 (
    echo [ERROR] Compilation failed.
    exit /b 1
)

REM Extract the filename without extension
FOR %%F IN ("%~1") DO SET exe_name=%%~nF.exe

REM Run the executable
IF EXIST "%exe_name%" (
    echo [INFO] Running %exe_name%...
    "%exe_name%"
) ELSE (
    echo [ERROR] Executable %exe_name% not found.
    exit /b 1
)
