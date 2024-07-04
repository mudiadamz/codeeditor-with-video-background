# XPrime Editor
An awesome code editor

### Install devs (first time):
`
pip -r requirements.txt
`

### Run/debugging the app:
`
python app.py
`

### To build executable:
`
pyinstaller XPrimeEditor.spec
`

### To create installer:
- Download Inno Setup, link  (https://jrsoftware.org/isdl.php#stable)
- Innosetup location 'C:\Program Files (x86)\Inno Setup 6'
- Add innosetup into environment
- run `build.bat`
- OR
- Open XPrimeEditorInstaller.iss using Inno Setup
- And then press the Build > Compile

Note: 
- the location of build is inside 'dist'
- the location of single file installer is 'Output'

