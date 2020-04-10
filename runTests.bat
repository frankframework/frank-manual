@echo off
SETLOCAL EnableDelayedExpansion
echo Running unit tests of TutorialSteps
echo -----------------------------------
echo.
FOR /R TutorialSteps %%F IN (test*.py) DO (
    SET name=%%~nF
    echo Running !name!
    python -m TutorialSteps.!name!
)