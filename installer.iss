; Inno Setup Script for Argus Overview Windows
; Build with: iscc installer.iss

#define MyAppName "Argus Overview"
#define MyAppVersion "2.4.2"
#define MyAppPublisher "AreteDriver"
#define MyAppURL "https://github.com/AreteDriver/Argus_Overview_Windows"
#define MyAppExeName "Argus_Overview.exe"

[Setup]
; Application info
AppId={{A8F3E2D1-B5C4-4E6F-9A8B-1C2D3E4F5A6B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
AppUpdatesURL={#MyAppURL}/releases

; Install location
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes

; Output settings
OutputDir=dist
OutputBaseFilename=Argus_Overview_Setup_{#MyAppVersion}
SetupIconFile=assets\icon.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

; Compression
Compression=lzma2/ultra64
SolidCompression=yes

; Privileges - don't require admin if installing to user folder
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

; Modern installer look
WizardStyle=modern
WizardSizePercent=100

; License and info
LicenseFile=LICENSE
InfoBeforeFile=README.md

; Misc
AllowNoIcons=yes
CloseApplications=yes
RestartApplications=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "startupicon"; Description: "Start with Windows"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Main executable
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

; Assets (if needed at runtime)
Source: "assets\icon.ico"; DestDir: "{app}\assets"; Flags: ignoreversion
Source: "assets\icon_256.png"; DestDir: "{app}\assets"; Flags: ignoreversion

[Icons]
; Start Menu
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

; Desktop (optional)
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

; Startup (optional)
Name: "{userstartup}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startupicon

[Run]
; Option to run after install
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Clean up config on uninstall (optional - commented out to preserve settings)
; Type: filesandordirs; Name: "{localappdata}\Argus-Overview"

[Code]
// Check if app is running before install/uninstall
function InitializeSetup(): Boolean;
begin
  Result := True;
end;

function InitializeUninstall(): Boolean;
begin
  Result := True;
end;
