; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; Basic settings
AppId={{521a4e4b-f7b0-4416-b4f4-227b96e949ab}}
AppName=XPrimeEditor
AppVersion=1.0
AppPublisher=Xprimes.com
AppPublisherURL=https://www.xprimes.com
DefaultDirName={pf}\XPrimeEditor
DefaultGroupName=XPrimeEditor
OutputBaseFilename=XPrimeEditorInstaller
Compression=lzma
SolidCompression=yes
SetupIconFile=dist/XPrimeEditor/_internal/assets/xicon.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Source files
Source: "dist/XPrimeEditor/XPrimeEditor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist/XPrimeEditor/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\XPrimeEditor"; Filename: "{app}\XPrimeEditor.exe"

[Run]
; Run the application after installation
Filename: "{app}\XPrimeEditor.exe"; Description: "{cm:LaunchProgram,XPrimeEditor}"; Flags: nowait postinstall skipifsilent

[Registry]
Root: "HKCR"; Subkey: "."; ValueType: string; ValueName: ""; ValueData: "XPrimeEditorFile"; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".txt"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".py"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".cpp"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".java"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".cs"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: ".html"; ValueType: string; ValueData: ""; Flags: uninsdeletevalue
Root: "HKCR"; Subkey: "XPrimeEditorFile"; ValueType: string; ValueName: ""; ValueData: "XPrimeEditor Document"; Flags: uninsdeletekey
Root: "HKCR"; Subkey: "XPrimeEditorFile\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\XPrimeEditor.exe,0"; Flags: uninsdeletekey
Root: "HKCR"; Subkey: "XPrimeEditorFile\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\XPrimeEditor.exe"" ""%1"""; Flags: uninsdeletekey