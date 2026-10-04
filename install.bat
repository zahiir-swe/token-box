@echo off
echo --- DIAGNOSTIC INSTALLATION TOKENBOX ---
cd /d "%~dp0"

echo.
echo 1. Verification de Python...
python --version
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas reconnu. Assure-toi de l'avoir installe et d'avoir coche "Add Python to PATH".
    pause
    exit /b
)

echo.
echo 2. Installation des packages...
python -m pip install keyboard keyring pyperclip pyinstaller

echo.
echo 3. Compilation avec PyInstaller...
python -m PyInstaller --noconsole --onefile token_box.py

if not exist "dist\token_box.exe" (
    echo.
    echo [ERREUR] La compilation a echoue. Verifie les messages ci-dessus.
    pause
    exit /b
)

echo.
echo 4. Creation du raccourci au demarrage...
set SCRIPT="%TEMP%\CreateShortcut.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") > %SCRIPT%
echo sLinkFile = "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\TokenBox.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%cd%\dist\token_box.exe" >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\dist" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%

echo.
echo === SUCCES ! ===
echo Le dossier 'dist' a bien ete cree.
pause