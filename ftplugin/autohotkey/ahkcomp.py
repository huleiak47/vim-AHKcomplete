#!/usr/bin/env python
# -*- coding:utf-8 -*-


AHK_DICT = {
    """AutoTrim""":
    """AutoTrim, On|Off

Determines whether <a href="SetEnv.htm">Var1 = %Var2%</a> statements omit spaces and tabs from the beginning and end of Var2.""",

    """Blocks""":
    """
{
zero or more commands
}

A pair of braces denotes a block. Blocks are typically used with functions, Else, Loop, While-loop, and IF-commands.""",

    """BlockInput""":
    """BlockInput, Mode

Disables or enables the user's ability to interact with the computer via keyboard and mouse. """,

    """Break""":
    """Break [, LoopLabel]

Exits (terminates) a loop. Valid inside any kind of loop.""",

    """Catch""":
    """""",

    """Click""":
    """""",

    """ClipWait""":
    """ClipWait [, SecondsToWait, 1]

Waits until the clipboard contains data.""",

    """ComObjActive()""":
    """ComObject := ComObjActive(CLSID)

Retrieves a running object that has been registered with OLE.""",

    """ComObjArray()""":
    """ArrayObj := ComObjArray(VarType, Count1 [, Count2, ... Count8])

Creates a SafeArray for use with COM.""",

    """ComObjConnect()""":
    """ComObjConnect(ComObject [, Prefix])

Connects the object's event sources to functions with a given prefix.""",

    """ComObjCreate()""":
    """ComObject := ComObjCreate(CLSID [, IID])

Creates a COM object.""",

    """ComObjError()""":
    """Enabled := ComObjError([Enable])

Enables or disables notification of COM errors.""",

    """ComObjFlags()""":
    """Flags := ComObjFlags(ComObject [, NewFlags, Mask])

Retrieves or changes flags which control a COM wrapper object's behaviour.""",

    """ComObjGet()""":
    """ComObject := ComObjGet(Name)

Returns a reference to an object provided by a COM component.""",

    """ComObjQuery()""":
    """InterfacePointer := ComObjQuery(ComObject, [SID,] IID)

Queries a COM object for an interface or service.""",

    """ComObjType()""":
    """VarType := ComObjType(ComObject)
Name    := ComObjType(ComObject, "Name")
IID     := ComObjType(ComObject, "IID")

Retrieves type information from a COM object.""",

    """ComObjValue()""":
    """Value := ComObjValue(ComObject)

Retrieves the value or pointer stored in a COM wrapper object.""",

    """Continue""":
    """Continue [, LoopLabel]

Skips the rest of the current loop iteration and begins a new one. Valid inside any kind of loop.""",

    """Control""":
    """Control, Cmd [, Value, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]

Makes a variety of changes to a control.""",

    """ControlClick""":
    """ControlClick [, Control-or-Pos, WinTitle, WinText, WhichButton, ClickCount, Options, ExcludeTitle, ExcludeText]

Sends a mouse  button or mouse wheel event to a  control. """,

    """ControlFocus""":
    """ControlFocus [, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]

Sets input focus to a given control on a window. """,

    """ControlGet""":
    """ControlGet, OutputVar, Cmd [, Value, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves various types of information about a control. """,

    """ControlGetFocus""":
    """ControlGetFocus, OutputVar [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves which control of the target window has input focus, if any.""",

    """ControlGetPos""":
    """ControlGetPos [, X, Y, Width, Height, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the position and size of a control.""",

    """ControlGetText""":
    """ControlGetText, OutputVar [, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves text from a control. """,

    """ControlMove""":
    """ControlMove, Control, X, Y, Width, Height [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Moves or resizes a control. """,

    """ControlSend""":
    """ControlSend [, Control, Keys, WinTitle, WinText, ExcludeTitle, ExcludeText]
ControlSendRaw: Same parameters as above.

Sends simulated keystrokes to a window or control.""",

    """ControlSendRaw""":
    """ControlSend [, Control, Keys, WinTitle, WinText, ExcludeTitle, ExcludeText]
ControlSendRaw: Same parameters as above.

Sends simulated keystrokes to a window or control.""",

    """ControlSetText""":
    """ControlSetText [, Control, NewText, WinTitle, WinText, ExcludeTitle, ExcludeText]

Changes the text of a control. """,

    """CoordMode""":
    """CoordMode, ToolTip|Pixel|Mouse|Caret|Menu [, Screen|Window|Client]

Sets coordinate mode for various commands to be relative to either the active window or the screen.""",

    """Critical""":
    """Critical [, Off]
Critical 50 ; See <a href="#Interval">bottom of remarks</a>.

Prevents the current thread from being interrupted by other threads.""",

    """DetectHiddenText""":
    """DetectHiddenText, On|Off

Determines whether invisible text in a window is "seen" for the purpose of finding the window. This affects commands such as IfWinExist and WinActivate.""",

    """DetectHiddenWindows""":
    """DetectHiddenWindows, On|Off

Determines whether invisible windows are "seen" by the script.""",

    """DllCall""":
    """Result := DllCall("[DllFile\]Function" [, Type1, Arg1, Type2, Arg2, "Cdecl ReturnType"])

Calls a function inside a DLL, such as a standard Windows API function.""",

    """Drive""":
    """Drive, Sub-command [, Drive , Value]

Ejects/retracts the tray in a CD or DVD drive, or sets a drive's volume label. """,

    """DriveGet""":
    """DriveGet, OutputVar, Cmd [, Value]

Retrieves various types of information about the computer's drive(s). """,

    """DriveSpaceFree""":
    """DriveSpaceFree, OutputVar, Path

Retrieves the free disk space of a drive, in Megabytes.""",

    """Edit""":
    """Edit

Opens the current script for editing in the associated editor.""",

    """Else""":
    """Else

Specifies the command(s) to perform if an IF-statement evaluates to FALSE. When more than one command is present, enclose them in a block (braces). """,

    """EnvAdd""":
    """EnvAdd, Var, Value [, TimeUnits]
Var += Value [, TimeUnits]
Var++

Sets a variable to the sum of itself plus the given value (can also add or subtract time from a date-time value). Synonymous with: var += value.""",

    """EnvDiv""":
    """EnvDiv, Var, Value

Sets a variable to itself divided by the given value. Synonymous with: Var /= Value.""",

    """EnvGet""":
    """EnvGet, OutputVar, EnvVarName

Retrieves an environment variable.""",

    """EnvMult""":
    """EnvMult, Var, Value

Sets a variable to itself times the given value. Synonymous with: Var *= Value.""",

    """EnvSet""":
    """EnvSet, EnvVar, Value

Writes a value to a variable contained in the  environment.""",

    """EnvSub""":
    """EnvSub, Var, Value [, TimeUnits]
Var -= Value [, TimeUnits]
Var--

Sets a variable to itself minus the given value (can also compare date-time values). Synonymous with: Var -= Value.""",

    """EnvUpdate""":
    """EnvUpdate

Notifies the OS and all running applications that environment variable(s) have changed.""",

    """Exit""":
    """Exit [, ExitCode]

Exits the current thread or (if the script is not persistent and contains no hotkeys) the entire script.""",

    """ExitApp""":
    """ExitApp [, ExitCode]

Terminates the script unconditionally.""",

    """FileAppend""":
    """FileAppend [, Text, Filename, Encoding]

Writes text to the end of a file (first creating the file, if necessary).""",

    """FileCopy""":
    """FileCopy, SourcePattern, DestPattern [, Flag]

Copies one or more files.""",

    """FileCopyDir""":
    """FileCopyDir, Source, Dest [, Flag]

Copies a folder along with all its sub-folders and files (similar to xcopy).""",

    """FileCreateDir""":
    """FileCreateDir, DirName

Creates a directory/folder. """,

    """FileCreateShortcut""":
    """FileCreateShortcut, Target, LinkFile [, WorkingDir, Args, Description, IconFile, ShortcutKey, IconNumber, RunState]

Creates a shortcut (.lnk) file.""",

    """FileDelete""":
    """FileDelete, FilePattern

Deletes one or more files. """,

    """FileEncoding""":
    """FileEncoding [, Encoding]

Sets the default encoding for FileRead, FileReadLine, Loop Read, FileAppend, and FileOpen.""",

    """FileGetAttrib""":
    """FileGetAttrib, OutputVar [, Filename]
AttributeString := FileExist(FilePattern)

Reports whether a file or folder is read-only, hidden, etc. """,

    """FileGetShortcut""":
    """FileGetShortcut, LinkFile [, OutTarget, OutDir, OutArgs, OutDescription, OutIcon, OutIconNum, OutRunState]

Retrieves information about a shortcut (.lnk) file, such as its target file. """,

    """FileGetSize""":
    """FileGetSize, OutputVar [, Filename, Units]

Retrieves the size of a file.""",

    """FileGetTime""":
    """FileGetTime, OutputVar [, Filename, WhichTime]

Retrieves the datetime stamp of a file or folder.""",

    """FileGetVersion""":
    """FileGetVersion, OutputVar [, Filename]

Retrieves the version of a file.""",

    """FileInstall""":
    """FileInstall, Source, Dest [, Flag]

Includes the specified file inside the compiled version of the script.""",

    """FileMove""":
    """FileMove, SourcePattern, DestPattern [, Flag]

Moves or renames one or more files.""",

    """FileMoveDir""":
    """FileMoveDir, Source, Dest [, Flag]

Moves a folder along with all its sub-folders and files. It can also rename a folder.""",

    """FileOpen""":
    """file := FileOpen(Filename, Flags [, Encoding])

Opens a file.""",

    """FileRead""":
    """FileRead, OutputVar, Filename

Reads a file's contents into a variable.""",

    """FileReadLine""":
    """FileReadLine, OutputVar, Filename, LineNum

Reads the specified line  from a file and stores the text in a variable.""",

    """FileRecycle""":
    """FileRecycle, FilePattern

Sends a file or directory to the recycle bin, if possible.""",

    """FileRecycleEmpty""":
    """FileRecycleEmpty [, DriveLetter]

Empties the recycle bin. """,

    """FileRemoveDir""":
    """FileRemoveDir, DirName [, Recurse?]

Deletes a folder.""",

    """FileSelectFile""":
    """FileSelectFile, OutputVar [, Options, RootDir\Filename, Prompt, Filter]

Displays a standard dialog  that allows the user to open or save file(s).""",

    """FileSelectFolder""":
    """FileSelectFolder, OutputVar [, StartingFolder, Options, Prompt]

Displays a standard dialog  that allows the user to select a folder.""",

    """FileSetAttrib""":
    """FileSetAttrib, Attributes [, FilePattern, OperateOnFolders?, Recurse?]

Changes the attributes of one or more files or folders. Wildcards are supported.""",

    """FileSetTime""":
    """FileSetTime [, YYYYMMDDHH24MISS, FilePattern, WhichTime, OperateOnFolders?, Recurse?]

Changes the  datetime stamp of one or more files or folders. Wildcards are supported.""",

    """For-loop""":
    """For Key [, Value] in Expression

Repeats a series of commands once for each key-value pair in an object.""",

    """FormatTime""":
    """FormatTime, OutputVar [, YYYYMMDDHH24MISS, Format]

Transforms a YYYYMMDDHH24MISS timestamp into the specified date/time format.""",

    """GetKeyState""":
    """GetKeyState, OutputVar, KeyName [, Mode]
      KeyIsDown := GetKeyState("KeyName" [, "Mode"])

Checks if a keyboard key or mouse/joystick button is down or up. Also retrieves joystick status.""",

    """Gosub""":
    """Gosub, Label

Jumps to the specified label and continues execution until Return is encountered.""",

    """Goto""":
    """Goto, Label

Jumps to the specified label and continues execution.""",

    """GroupActivate""":
    """GroupActivate, GroupName [, R]

Activates the next window in a window group that was defined with GroupAdd.  """,

    """GroupAdd""":
    """GroupAdd, GroupName [, WinTitle, WinText, Label, ExcludeTitle, ExcludeText]

Adds a window specification to a window group, creating the group if necessary.""",

    """GroupClose""":
    """GroupClose, GroupName [, A|R]

Closes the active window if it was just activated by GroupActivate or GroupDeactivate. It then activates the next window in the series. It can also close all windows in a group. """,

    """GroupDeactivate""":
    """GroupDeactivate, GroupName [, R]

Similar to GroupActivate except activates the next window not in the group.""",

    """GUI""":
    """Gui, sub-command [, Param2, Param3, Param4]

Creates and manages windows and controls. Such windows can be used as data entry forms or custom user interfaces.""",

    """GuiControl""":
    """GuiControl, Sub-command, ControlID [, Param3]

Makes a variety of changes to a control in a GUI window.""",

    """GuiControlGet""":
    """GuiControlGet, OutputVar [, Sub-command, ControlID, Param4]

Retrieves various types of information about a control in a GUI window. """,

    """Hotkey""":
    """Hotkey, KeyName [, Label, Options]
Hotkey, IfWinActive/Exist [, WinTitle, WinText]
Hotkey, If, Expression

Creates, modifies, enables, or disables a hotkey while the script is running.""",


    """If""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.
if Var between LowerBound and UpperBound
if Var not between LowerBound and UpperBound
See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).

if Var in MatchList
if Var not in <i>MatchList<br>
</i>if Var contains MatchList
if Var not contains MatchList

Checks whether a variable's contents match one of the items in a list.
""",

    """IfEqual""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfNotEqual""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfLess""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfLessOrEqual""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfGreater""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfGreaterOrEqual""":
    """IfEqual, var, value (same: if var = value)
IfNotEqual, var, value (same: if var <> value) (!= can be used in place of <>)
IfGreater, var, value (same: if var > value)
IfGreaterOrEqual, var, value (same: if var >= value)
IfLess, var, value (same: if var < value)
IfLessOrEqual, var, value (same: if var <= value)
If var ; If var's contents are blank or 0, it is considered false. Otherwise, it is true.

See also: IfInString

Specifies the command(s) to perform if the comparison of a variable to a value evalutes to TRUE. When more than one command is present, enclose them in a block (braces).""",

    """IfExist""":
    """IfExist, FilePattern
IfNotExist, FilePattern
AttributeString := FileExist(FilePattern)

Checks for the existence of a file or folder.""",

    """IfNotExist""":
    """IfExist, FilePattern
IfNotExist, FilePattern
AttributeString := FileExist(FilePattern)

Checks for the existence of a file or folder.""",

    """if""":
    """if (expression)

Specifies the command(s) to perform if an expression evaluates to TRUE. """,

    """contains""":
    """if Var in MatchList
if Var not in <i>MatchList<br>
</i>if Var contains MatchList
if Var not contains MatchList

Checks whether a variable's contents match one of the items in a list.""",

    """IfInString""":
    """IfInString, var, SearchString
IfNotInString, var, SearchString
Position := InStr(Haystack, Needle [, CaseSensitive?, StartingPos]]) ; See the <a href="../Functions.htm#InStr">InStr() function</a> for details.

Checks if a variable contains the specified string.""",

    """IfNotInString""":
    """IfInString, var, SearchString
IfNotInString, var, SearchString
Position := InStr(Haystack, Needle [, CaseSensitive?, StartingPos]]) ; See the <a href="../Functions.htm#InStr">InStr() function</a> for details.

Checks if a variable contains the specified string.""",

    """IfMsgBox""":
    """IfMsgBox, ButtonName

Checks which button was pushed by the user during the most recent MsgBox command.""",

    """IfWinActive""":
    """IfWinActive [, WinTitle, WinText,  ExcludeTitle, ExcludeText]
IfWinNotActive [, WinTitle, WinText, ExcludeTitle, ExcludeText]
UniqueID := WinActive("WinTitle", "WinText", "ExcludeTitle", "ExcludeText")

Checks if the specified window exists and is currently active (foremost).""",

    """IfWinNotActive""":
    """IfWinActive [, WinTitle, WinText,  ExcludeTitle, ExcludeText]
IfWinNotActive [, WinTitle, WinText, ExcludeTitle, ExcludeText]
UniqueID := WinActive("WinTitle", "WinText", "ExcludeTitle", "ExcludeText")

Checks if the specified window exists and is currently active (foremost).""",

    """IfWinExist""":
    """IfWinExist [, WinTitle, WinText,  ExcludeTitle, ExcludeText]
IfWinNotExist [, WinTitle, WinText, ExcludeTitle, ExcludeText]
UniqueID := WinExist("WinTitle", "WinText", "ExcludeTitle", "ExcludeText")

Checks if a matching window exists. WinExist() returns the Unique ID (HWND) of the first matching window.""",

    """IfWinNotExist""":
    """IfWinExist [, WinTitle, WinText,  ExcludeTitle, ExcludeText]
IfWinNotExist [, WinTitle, WinText, ExcludeTitle, ExcludeText]
UniqueID := WinExist("WinTitle", "WinText", "ExcludeTitle", "ExcludeText")

Checks if a matching window exists. WinExist() returns the Unique ID (HWND) of the first matching window.""",

    """WinExist""":
    """IfWinExist [, WinTitle, WinText,  ExcludeTitle, ExcludeText]
IfWinNotExist [, WinTitle, WinText, ExcludeTitle, ExcludeText]
UniqueID := WinExist("WinTitle", "WinText", "ExcludeTitle", "ExcludeText")

Checks if a matching window exists. WinExist() returns the Unique ID (HWND) of the first matching window.""",

    """ImageSearch""":
    """ImageSearch, OutputVarX, OutputVarY, X1, Y1, X2, Y2, ImageFile

Searches a region of the screen for an image.""",

    """IniDelete""":
    """IniDelete, Filename, Section [, Key]

Deletes a value from a standard format .ini file. """,

    """IniRead""":
    """IniRead, OutputVar, Filename [, Section, Key, Default]

Reads a value from a standard format .ini file.""",

    """IniWrite""":
    """IniWrite, Value, Filename, Section [, Key]

Writes a value to a standard format .ini file.""",

    """Input""":
    """Input [, OutputVar, Options, EndKeys, MatchList]

Waits for the user to type a string (not supported on Windows 9x: it does nothing).""",

    """InputBox""":
    """InputBox, OutputVar [, Title, Prompt, HIDE, Width, Height, X, Y, Font, Timeout, Default]

Displays an input box to ask the user to enter a string.""",

    """KeyHistory""":
    """KeyHistory

Displays script info and a history of the most recent keystrokes and mouse clicks.""",

    """KeyWait""":
    """KeyWait, KeyName [, Options]

Waits for a key or mouse/joystick button to be released or pressed down. """,

    """ListHotkeys""":
    """ListHotkeys

Displays the hotkeys in use by the current script, whether their subroutines are currently running, and whether or not they use the keyboard or mouse hook.""",

    """ListLines""":
    """ListLines [, On|Off]

Displays the script lines most recently executed.""",

    """ListVars""":
    """ListVars

Displays the script's variables: their names and current contents.""",

    """ListView""":
    """Gui, Add, ListView, Options, ColumnTitle1|ColumnTitle2|...

A List-View is one of the most elaborate controls provided by the operating system. In its most recognizable form, it displays a tabular view of rows and columns, the most common example of which is Explorer's list of files and folders (detail view).</p>
<p>Though it may be elaborate, a ListView's basic features are easy to use. The syntax for creating a ListView is:""",

    """Loop""":
    """Loop [, Count]

Perform a series of commands repeatedly: either the specified number of times or until break is encountered.""",

    """Loop""":
    """Loop, FilePattern [, IncludeFolders?, Recurse?]
Loop (parse a string)
Loop, Read, InputFile [, OutputFile]
Loop, RootKey [, Key, IncludeSubkeys?, Recurse?]

Retrieves the specified files or folders, one at a time.
Retrieves substrings (fields) from a string, one at a time.
Retrieves the lines in a text file, one at a time (performs better than FileReadLine).
Retrieves the contents of the specified registry subkey, one item at a time.""",


    """Menu""":
    """Menu, MenuName, Cmd [, P3, P4, P5]

Creates, deletes, modifies and displays menus and menu items. Changes the tray icon and its tooltip. Controls whether the main window of a compiled script can be opened.""",

    """MouseClick""":
    """MouseClick [, WhichButton , X, Y, ClickCount, Speed, D|U, R]

Clicks or holds down a mouse button, or turns the mouse wheel. NOTE: The Click command is generally more flexible and easier to use.""",

    """MouseClickDrag""":
    """MouseClickDrag, WhichButton, X1, Y1, X2, Y2 [, Speed, R]

Clicks and holds the specified mouse button, moves the mouse to the destination coordinates, then releases the button.""",

    """MouseGetPos""":
    """MouseGetPos, [OutputVarX, OutputVarY, OutputVarWin, OutputVarControl, 1|2|3]

Retrieves the current position of the mouse cursor, and optionally which window and control it is hovering over. """,

    """MouseMove""":
    """MouseMove, X, Y [, Speed, R]

Moves the mouse cursor.""",

    """MsgBox""":
    """MsgBox, Text
MsgBox [, Options, Title, Text, Timeout]

Displays the specified text in a small window containing one or more buttons (such as Yes and No).""",

    """ObjAddRef()""":
    """ObjAddRef(Ptr)<br>ObjRelease(Ptr)

Increments or decrements an object's reference count.""",

    """ObjRelease()""":
    """ObjAddRef(Ptr)<br>ObjRelease(Ptr)

Increments or decrements an object's reference count.""",

    """OnExit""":
    """OnExit [, Label]

Specifies a subroutine to run  automatically when the script exits.""",

    """OnMessage""":
    """OnMessage(MsgNumber [, "FunctionName", MaxThreads])

Specifies a function to call automatically when the script receives the specified message.""",

    """OutputDebug""":
    """OutputDebug, Text

Sends a string to the debugger (if any) for display.""",

    """Pause""":
    """#p::Pause ; Pressing Win+P once will pause the script. Pressing it again will unpause.
Pause [, On|Off|Toggle, OperateOnUnderlyingThread?]

Pauses the script's current thread.""",

    """PixelGetColor""":
    """PixelGetColor, OutputVar, X, Y [, Alt|Slow|RGB]

Retrieves  the color of the pixel at the specified x,y coordinates.""",

    """PixelSearch""":
    """PixelSearch, OutputVarX, OutputVarY, X1, Y1, X2, Y2, ColorID [, Variation, Fast|RGB]

Searches a region of the screen for a pixel of the specified color.""",

    """PostMessage""":
    """PostMessage, Msg [, wParam, lParam, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]
SendMessage, Msg [, wParam, lParam, Control, WinTitle, WinText, ExcludeTitle, ExcludeText, Timeout]

Sends a message to a window or control (SendMessage additionally waits for acknowledgement).""",

    """SendMessage""":
    """PostMessage, Msg [, wParam, lParam, Control, WinTitle, WinText, ExcludeTitle, ExcludeText]
SendMessage, Msg [, wParam, lParam, Control, WinTitle, WinText, ExcludeTitle, ExcludeText, Timeout]

Sends a message to a window or control (SendMessage additionally waits for acknowledgement).""",

    """Process""":
    """Process, Cmd, PID-or-Name [, Param3]

Performs one of the following operations on a process: checks if it exists; changes its priority; closes it; waits for it to close.""",

    """Progress""":
    """SplashImage, Off
SplashImage [, ImageFile, Options, SubText, MainText, WinTitle, FontName]

Progress, Off
Progress, ProgressParam1 [, SubText, MainText, WinTitle, FontName]

Creates or updates a window containing a progress bar or an image.""",

    """SplashImage""":
    """SplashImage, Off
SplashImage [, ImageFile, Options, SubText, MainText, WinTitle, FontName]

Progress, Off
Progress, ProgressParam1 [, SubText, MainText, WinTitle, FontName]

Creates or updates a window containing a progress bar or an image.""",

    """Random""":
    """Random, OutputVar [, Min, Max]
Random, , NewSeed

Generates a pseudo-random number.""",

    """RegDelete""":
    """RegDelete, RootKey, SubKey [, ValueName]

Deletes a subkey or value from the registry. """,

    """RegExMatch""":
    """FoundPos := RegExMatch(Haystack, NeedleRegEx [, UnquotedOutputVar = "", StartingPosition = 1])

Determines whether a string contains a pattern (regular expression).""",

    """RegExReplace""":
    """NewStr := RegExReplace(Haystack, NeedleRegEx [, Replacement = "", OutputVarCount = "", Limit = -1, StartingPosition = 1])

Replaces occurrences of a pattern (regular expression) inside a string.""",

    """RegisterCallback""":
    """Address := RegisterCallback("FunctionName" [, Options = "", ParamCount = FormalCount, EventInfo = Address])

Creates a machine-code address that when called, redirects the call to a function in the script.""",

    """RegRead""":
    """RegRead, OutputVar, RootKey, SubKey [, ValueName]

Reads a value from the registry.""",

    """RegWrite""":
    """RegWrite, ValueType, RootKey, SubKey [, ValueName, Value]

Writes a value to the registry.""",

    """Reload""":
    """Reload

Replaces the currently running instance of the script with a new one. """,

    """Return""":
    """Return [, Expression]

Returns from a subroutine to which execution had previously jumped via function-call, Gosub, Hotkey activation, GroupActivate, or other means. """,

    """Run""":
    """Run, Target [, WorkingDir, Max|Min|Hide|UseErrorLevel, OutputVarPID]

Runs an external program. Unlike Run, RunWait will wait until
the program finishes before continuing.""",

    """RunWait""":
    """Run, Target [, WorkingDir, Max|Min|Hide|UseErrorLevel, OutputVarPID]

Runs an external program. Unlike Run, RunWait will wait until
the program finishes before continuing.""",

    """RunAs""":
    """RunAs [, User, Password, Domain]

Specifies a set of user credentials to use for all subsequent uses of Run and RunWait. Requires Windows 2000/XP or later.""",

    """Send""":
    """Send Keys
SendRaw Keys
SendInput Keys
SendPlay Keys
SendEvent Keys

Sends simulated keystrokes and mouse clicks to the active window.""",

    """SendRaw""":
    """Send Keys
SendRaw Keys
SendInput Keys
SendPlay Keys
SendEvent Keys

Sends simulated keystrokes and mouse clicks to the active window.""",

    """SendInput""":
    """Send Keys
SendRaw Keys
SendInput Keys
SendPlay Keys
SendEvent Keys

Sends simulated keystrokes and mouse clicks to the active window.""",

    """SendPlay""":
    """Send Keys
SendRaw Keys
SendInput Keys
SendPlay Keys
SendEvent Keys

Sends simulated keystrokes and mouse clicks to the active window.""",

    """SendEvent""":
    """Send Keys
SendRaw Keys
SendInput Keys
SendPlay Keys
SendEvent Keys

Sends simulated keystrokes and mouse clicks to the active window.""",

    """SendLevel""":
    """SendLevel, Level

Controls which artificial keyboard and mouse events are ignored by hotkeys and hotstrings.""",

    """SendMode""":
    """SendMode Input|Play|Event|InputThenPlay

Makes Send synonymous with SendInput or SendPlay rather than the default (SendEvent). Also makes Click and MouseMove/Click/Drag use the specified method.""",

    """SetBatchLines""":
    """SetBatchLines, 20ms
SetBatchLines, LineCount

Determines how fast a script will run (affects CPU utilization).""",

    """SetControlDelay""":
    """SetControlDelay, Delay

Sets the delay that will occur after each control-modifying command.""",

    """SetDefaultMouseSpeed""":
    """SetDefaultMouseSpeed, Speed

Sets the mouse speed that will be used if unspecified in Click and MouseMove/Click/Drag.""",

    """SetEnv""":
    """SetEnv, Var, Value
Var = Value

Assigns the specified value to a variable.""",

    """SetFormat""":
    """SetFormat, NumberType, Format

Sets the format of integers and floating point numbers generated by math operations.""",

    """SetKeyDelay""":
    """SetKeyDelay [, Delay, PressDuration, Play]

Sets the delay that will occur after each keystroke sent by Send and ControlSend.""",

    """SetMouseDelay""":
    """SetMouseDelay, Delay [, Play]

Sets the delay that will occur after each mouse movement or click.""",

    """SetCapsLockState""":
    """SetCapsLockState [, State]
SetNumLockState [, State]
SetScrollLockState [, State]

Sets the state of the Capslock/NumLock/ScrollLock key. Can also force the key to stay on or off.""",

    """SetNumLockState""":
    """SetCapsLockState [, State]
SetNumLockState [, State]
SetScrollLockState [, State]

Sets the state of the Capslock/NumLock/ScrollLock key. Can also force the key to stay on or off.""",

    """SetScrollLockState""":
    """SetCapsLockState [, State]
SetNumLockState [, State]
SetScrollLockState [, State]

Sets the state of the Capslock/NumLock/ScrollLock key. Can also force the key to stay on or off.""",

    """SetRegView""":
    """SetRegView, RegView

Sets the registry view used by RegRead, RegWrite, RegDelete and registry loops.""",

    """SetStoreCapslockMode""":
    """SetStoreCapslockMode, On|Off

Whether to restore the state of CapsLock after a Send.""",

    """SetTimer""":
    """SetTimer [, Label, Period|On|Off, Priority]

Causes a subroutine to be launched automatically  and repeatedly at a specified time interval.""",

    """SetTitleMatchMode""":
    """SetTitleMatchMode, MatchMode
SetTitleMatchMode, Fast|Slow

Sets the matching behavior of the WinTitle parameter in commands such as WinWait.""",

    """SetWinDelay""":
    """SetWinDelay, Delay

Sets the delay that will occur after each windowing command, such as WinActivate.""",

    """SetWorkingDir""":
    """SetWorkingDir, DirName

Changes the script's current working directory. """,

    """Shutdown""":
    """Shutdown, Code

Shuts down, restarts, or logs off the system.""",

    """Sleep""":
    """Sleep, DelayInMilliseconds

Waits the specified amount of time before continuing.""",

    """Sort""":
    """Sort, VarName [, Options]

Arranges a variable's contents in alphabetical, numerical, or random order (optionally removing duplicates).""",

    """SoundBeep""":
    """SoundBeep [, Frequency, Duration]

Emits a tone from the PC speaker.""",

    """SoundGet""":
    """SoundGet, OutputVar [, ComponentType, ControlType, DeviceNumber]

Retrieves various settings from a sound device (master mute, master volume, etc.)""",

    """SoundGetWaveVolume""":
    """SoundGetWaveVolume, OutputVar [, DeviceNumber]

Retrieves the wave output volume for a sound device.""",

    """SoundPlay""":
    """SoundPlay, Filename [, wait]

Plays a sound, video, or other supported file type. """,

    """SoundSet""":
    """SoundSet, NewSetting [, ComponentType, ControlType, DeviceNumber]

Changes various settings of a sound device (master mute, master volume, etc.)""",

    """SoundSetWaveVolume""":
    """SoundSetWaveVolume, Percent [, DeviceNumber]

Changes the wave output volume for a sound device.""",

    """SplashTextOn""":
    """SplashTextOff
SplashTextOn [, Width, Height, Title, Text]

Creates a customizable text popup window.""",

    """SplashTextOff""":
    """SplashTextOff
SplashTextOn [, Width, Height, Title, Text]

Creates a customizable text popup window.""",

    """SplitPath""":
    """SplitPath, InputVar [, OutFileName, OutDir, OutExtension, OutNameNoExt, OutDrive]

Separates a file name or URL into its name, directory, extension, and drive.""",

    """StatusbarGetText""":
    """StatusBarGetText, OutputVar [, Part#, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the text from a standard status bar control. """,

    """StatusBarWait""":
    """StatusBarWait [, BarText, Seconds, Part#, WinTitle, WinText, Interval, ExcludeTitle, ExcludeText]

Waits until a window's status bar contains the specified string.""",

    """StringCaseSense""":
    """StringCaseSense, On|Off|Locale

Determines whether string comparisons are case sensitive (default is "not case sensitive"). """,

    """StringGetPos""":
    """StringGetPos, OutputVar, InputVar, SearchText [, L#|R#, Offset]
Position := InStr(Haystack, Needle [, CaseSensitive?, StartingPos]) ; See the <a href="../Functions.htm#InStr">InStr() function</a> for details.

Retrieves the position of the specified substring within a string.""",

    """StringLeft""":
    """StringLeft, OutputVar, InputVar, Count
StringRight, OutputVar, InputVar, Count
NewStr := SubStr(String, StartPos [, Length]) ; See the <a href="../Functions.htm#SubStr">SubStr() function</a> for details.

Retrieves a number of characters from the left or right-hand side of
a string.""",

    """StringRight""":
    """StringLeft, OutputVar, InputVar, Count
StringRight, OutputVar, InputVar, Count
NewStr := SubStr(String, StartPos [, Length]) ; See the <a href="../Functions.htm#SubStr">SubStr() function</a> for details.

Retrieves a number of characters from the left or right-hand side of
a string.""",

    """StrLen""":
    """OutputVar := StrLen(InputVar)
StringLen, OutputVar, InputVar


Retrieves the count of how many characters are in a string.""",

    """StringLen""":
    """OutputVar := StrLen(InputVar)
StringLen, OutputVar, InputVar


Retrieves the count of how many characters are in a string.""",

    """StringLower""":
    """StringLower, OutputVar, InputVar [, T]
StringUpper, OutputVar, InputVar [, T]

Converts a string to lowercase or uppercase.""",

    """StringUpper""":
    """StringLower, OutputVar, InputVar [, T]
StringUpper, OutputVar, InputVar [, T]

Converts a string to lowercase or uppercase.""",

    """StringMid""":
    """StringMid, OutputVar, InputVar, StartChar [, Count , L]
NewStr := SubStr(String, StartPos [, Length]) ; See the <a href="../Functions.htm#SubStr">SubStr() function</a> for details.

Retrieves one or more characters from the specified position in a string.""",

    """StringReplace""":
    """StringReplace, OutputVar, InputVar, SearchText [, ReplaceText, ReplaceAll?]

Replaces the specified substring with a new string.""",

    """StringSplit""":
    """StringSplit, OutputArray, InputVar [, Delimiters, OmitChars]
Array := StrSplit(String [, Delimiters, OmitChars])  ; [v1.1.13+]

Separates a string into an array of substrings using the specified delimiters.""",

    """StrSplit()""":
    """StringSplit, OutputArray, InputVar [, Delimiters, OmitChars]
Array := StrSplit(String [, Delimiters, OmitChars])  ; [v1.1.13+]

Separates a string into an array of substrings using the specified delimiters.""",

    """StringTrimLeft""":
    """StringTrimLeft, OutputVar, InputVar, Count
StringTrimRight, OutputVar, InputVar, Count
NewStr := SubStr(String, StartPos [, Length]) ; See the <a href="../Functions.htm#SubStr">SubStr() function</a> for details.

Removes a number of characters from the left or right-hand side of a
string.""",

    """StringTrimRight""":
    """StringTrimLeft, OutputVar, InputVar, Count
StringTrimRight, OutputVar, InputVar, Count
NewStr := SubStr(String, StartPos [, Length]) ; See the <a href="../Functions.htm#SubStr">SubStr() function</a> for details.

Removes a number of characters from the left or right-hand side of a
string.""",

    """StrPut""":
    """StrPut(String [, Encoding = None ] )
StrPut(String, Address [, Length] [, Encoding = None ] )
StrGet(Address [, Length] [, Encoding = None ] )

Copies a string to or from a memory address, optionally converting to or from a given code page.""",

    """StrGet""":
    """StrPut(String [, Encoding = None ] )
StrPut(String, Address [, Length] [, Encoding = None ] )
StrGet(Address [, Length] [, Encoding = None ] )

Copies a string to or from a memory address, optionally converting to or from a given code page.""",

    """Suspend""":
    """Suspend [, Mode]

Disables or enables all or selected hotkeys and hotstrings.""",

    """SysGet""":
    """SysGet, OutputVar, Sub-command [, Param3]

Retrieves screen resolution, multi-monitor info, dimensions of system objects, and other system properties.""",

    """Thread""":
    """Thread, NoTimers [, false]
Thread, Priority, n
Thread, Interrupt [, Duration, LineCount]

Sets the priority or interruptibility of threads. It can also temporarily disable all timers.""",

    """Throw""":
    """Throw [, Expression]

Signals the occurrence of an error. This signal can be caught by a try-catch statement.""",

    """ToolTip""":
    """ToolTip [, Text, X, Y, WhichToolTip]

Creates an always-on-top window anywhere on the screen.""",

    """Transform""":
    """Transform, OutputVar, Cmd, Value1 [, Value2]

Performs miscellaneous math functions, bitwise operations, and tasks such as ASCII/Unicode conversion.""",

    """TrayTip""":
    """TrayTip [, Title, Text, Seconds, Options]

Creates a balloon message window near the tray icon. Requires Windows 2000/XP or later.""",

    """TreeView""":
    """Gui, Add, TreeView, Options

A Tree-View displays a hierarchy of items by indenting child items beneath their parents. The most common example is Explorer's tree of drives and folders.""",

    """Trim""":
    """Result :=  Trim(String, OmitChars = " `t")
Result := LTrim(String, OmitChars = " `t")
Result := RTrim(String, OmitChars = " `t")

Trims characters from the beginning and/or end of a string.""",

    """Try""":
    """Try Statement

Guards one or more statements (commands or expressions) against runtime errors and exceptions thrown by the throw command.""",

    """Until""":
    """Loop {
    ...
} Until Expression

Applies a condition to the continuation of a Loop or For-loop.""",

    """UrlDownloadToFile""":
    """UrlDownloadToFile, URL, Filename

Downloads a file from the Internet.""",

    """VarSetCapacity()""":
    """GrantedCapacity := VarSetCapacity(UnquotedVarName [, RequestedCapacity, FillByte])

Enlarges a variable's holding capacity or frees its memory. Normally, this is necessary only for unusual circumstances such as DllCall.""",

    """While-loop""":
    """While Expression

Performs a series of commands repeatedly until the specified expression evaluates to false.""",

    """WinActivate""":
    """WinActivate [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Activates the specified window (makes it foremost).""",

    """WinActivateBottom""":
    """WinActivateBottom [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Same as WinActivate except that it activates the bottommost (least recently active) matching window rather than the topmost.""",

    """WinClose""":
    """WinClose [, WinTitle, WinText, SecondsToWait, ExcludeTitle, ExcludeText]

Closes the specified  window.""",

    """WinGet""":
    """WinGet, OutputVar [, Cmd, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the specified window's unique ID, process ID, process name, or a list of its controls. It can also retrieve a list of all windows matching the specified criteria.""",

    """WinGetActiveStats""":
    """WinGetActiveStats, Title, Width, Height, X, Y

Combines the functions of WinGetActiveTitle and WinGetPos into one command.""",

    """WinGetActiveTitle""":
    """WinGetActiveTitle, OutputVar

Retrieves the title of the active window.""",

    """WinGetClass""":
    """WinGetClass, OutputVar [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the specified window's class name.""",

    """WinGetPos""":
    """WinGetPos [, X, Y, Width, Height, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the position and size of the specified window.""",

    """WinGetText""":
    """WinGetText, OutputVar [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the text from the specified window.""",

    """WinGetTitle""":
    """WinGetTitle, OutputVar [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Retrieves the title of the specified window.""",

    """WinHide""":
    """WinHide [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Hides the specified window.""",

    """WinKill""":
    """WinKill [, WinTitle, WinText, SecondsToWait, ExcludeTitle, ExcludeText]

Forces the specified window to close.""",

    """WinMaximize""":
    """WinMaximize [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Enlarges the specified window to its maximum size. """,

    """WinMenuSelectItem""":
    """WinMenuSelectItem, WinTitle, WinText, Menu [, SubMenu1, SubMenu2, SubMenu3, SubMenu4, SubMenu5, SubMenu6, ExcludeTitle, ExcludeText]

Invokes a menu item from the menu bar of the specified window.""",

    """WinMinimize""":
    """WinMinimize [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Collapses the specified window into a button on the task bar.""",

    """WinMinimizeAll""":
    """WinMinimizeAll
WinMinimizeAllUndo

Minimizes or unminimizes all windows.""",

    """WinMinimizeAllUndo""":
    """WinMinimizeAll
WinMinimizeAllUndo

Minimizes or unminimizes all windows.""",

    """WinMove""":
    """WinMove, X, Y
WinMove, WinTitle, WinText, X, Y [, Width, Height, ExcludeTitle, ExcludeText]

Changes the position and/or size of the specified window.""",

    """WinRestore""":
    """WinRestore [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Unminimizes or unmaximizes the specified window if it is minimized or maximized.""",

    """WinSet""":
    """WinSet, Attribute, Value [, WinTitle, WinText,  ExcludeTitle, ExcludeText]

Makes a variety of changes to the specified window, such as "always on top" and transparency.""",

    """WinSetTitle""":
    """WinSetTitle, NewTitle
WinSetTitle, WinTitle, WinText, NewTitle [, ExcludeTitle, ExcludeText]

Changes the title of the specified window.""",

    """WinShow""":
    """WinShow [, WinTitle, WinText, ExcludeTitle, ExcludeText]

Unhides the specified window.""",

    """WinWait""":
    """WinWait [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]

Waits until the specified window
exists.""",

    """WinWaitActive""":
    """WinWaitActive [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]
WinWaitNotActive [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]

Waits until the specified window
is active or not active. """,

    """WinWaitNotActive""":
    """WinWaitActive [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]
WinWaitNotActive [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]

Waits until the specified window
is active or not active. """,

    """WinWaitClose""":
    """WinWaitClose [, WinTitle, WinText, Seconds, ExcludeTitle, ExcludeText]

Waits until the specified window
does not exist.""",

    """#AllowSameLineComments""":
    """#AllowSameLineComments

Removed in v1.1.09: AutoIt scripts are no longer supported.</p>

<p>Only for AutoIt v2 (.aut) scripts: Allows a comment to appear on the same line as a command.""",

    """#ClipboardTimeout""":
    """#ClipboardTimeout Milliseconds

Changes how long the script keeps trying to access the clipboard when the first attempt fails.""",

    """#CommentFlag""":
    """#CommentFlag NewString

Changes the script's comment symbol from semicolon to some other string.""",

    """#ErrorStdOut""":
    """#ErrorStdOut

Sends any syntax error that prevents a script from launching to stdout rather than displaying a dialog.""",

    """#EscapeChar""":
    """#EscapeChar NewChar

Changes the script's escape character (e.g. accent vs. backslash).""",

    """#HotkeyInterval""":
    """#HotkeyInterval Milliseconds

Along with #MaxHotkeysPerInterval, specifies the rate of hotkey activations beyond which a warning dialog will be displayed.""",

    """#HotkeyModifierTimeout""":
    """#HotkeyModifierTimeout Milliseconds

Affects the behavior of hotkey modifiers: CTRL, ALT, WIN, and SHIFT.""",

    """#Hotstring""":
    """#Hotstring NoMouse
#Hotstring EndChars NewChars
#Hotstring NewOptions

Changes hotstring options or ending characters.""",

    """#If""":
    """#If [, Expression ]

Creates context-sensitive hotkeys and hotstrings. Such hotkeys perform a different action (or none at all) depending on the result of an expression.""",

    """#IfTimeout""":
    """#IfTimeout Timeout

Sets the maximum time that may be spent evaluating a single #If expression.""",

    """#IfWinActive""":
    """#IfWinActive [, WinTitle, WinText]
#IfWinExist [, WinTitle, WinText]
#IfWinNotActive [, WinTitle, WinText]
#IfWinNotExist [, WinTitle, WinText]
#If [, Expression]

Creates context-sensitive hotkeys and hotstrings. Such hotkeys perform a different action (or none at all) depending on the type of window that is active or exists.""",

    """#IfWinNotActive""":
    """#IfWinActive [, WinTitle, WinText]
#IfWinExist [, WinTitle, WinText]
#IfWinNotActive [, WinTitle, WinText]
#IfWinNotExist [, WinTitle, WinText]
#If [, Expression]

Creates context-sensitive hotkeys and hotstrings. Such hotkeys perform a different action (or none at all) depending on the type of window that is active or exists.""",

    """#IfWinExist""":
    """#IfWinActive [, WinTitle, WinText]
#IfWinExist [, WinTitle, WinText]
#IfWinNotActive [, WinTitle, WinText]
#IfWinNotExist [, WinTitle, WinText]
#If [, Expression]

Creates context-sensitive hotkeys and hotstrings. Such hotkeys perform a different action (or none at all) depending on the type of window that is active or exists.""",

    """#IfWinNotExist""":
    """#IfWinActive [, WinTitle, WinText]
#IfWinExist [, WinTitle, WinText]
#IfWinNotActive [, WinTitle, WinText]
#IfWinNotExist [, WinTitle, WinText]
#If [, Expression]

Creates context-sensitive hotkeys and hotstrings. Such hotkeys perform a different action (or none at all) depending on the type of window that is active or exists.""",

    """#Include""":
    """#Include FileOrDirName
#Include <LibName>
#IncludeAgain FileOrDirName

Causes the script to behave as though the specified file's contents are present at this exact position.""",

    """#InputLevel""":
    """#InputLevel [, Level]

Controls which artificial keyboard and mouse events are ignored by hotkeys and hotstrings.""",

    """#InstallKeybdHook""":
    """#InstallKeybdHook

Forces the unconditional installation of the keyboard hook.""",

    """#InstallMouseHook""":
    """#InstallMouseHook

Forces the unconditional installation of the mouse hook.""",

    """#KeyHistory""":
    """#KeyHistory MaxEvents

Sets the maximum number of keyboard and mouse events displayed by the KeyHistory window. You can set it to 0 to disable key history.""",

    """#MaxHotkeysPerInterval""":
    """#MaxHotkeysPerInterval Value

Along with #HotkeyInterval, specifies the rate of hotkey activations beyond which a warning dialog will be displayed.""",

    """#MaxMem""":
    """#MaxMem Megabytes

Sets the maximum capacity of each variable to the specified number of megabytes.""",

    """#MaxThreads""":
    """#MaxThreads Value

Sets the maximum number of simultaneous threads.""",

    """#MaxThreadsBuffer""":
    """#MaxThreadsBuffer On|Off

Causes some or all hotkeys to buffer rather than ignore keypresses when their #MaxThreadsPerHotkey limit has been reached. """,

    """#MaxThreadsPerHotkey""":
    """#MaxThreadsPerHotkey Value

Sets the maximum number of simultaneous threads per hotkey or hotstring.""",

    """#MenuMaskKey""":
    """#MenuMaskKey KeyName

Changes which key is used to mask Win or Alt keyup events.""",

    """#NoEnv""":
    """#NoEnv

Avoids checking empty variables to see if they are environment variables (recommended for all new scripts).""",

    """#NoTrayIcon""":
    """#NoTrayIcon

Disables the showing of a tray icon.""",

    """#Persistent""":
    """#Persistent

Keeps a script permanently running (that is, until the user closes it or ExitApp is encountered).""",

    """#SingleInstance""":
    """#SingleInstance [force|ignore|off]

Determines whether a script is allowed to run again when it is already running.""",

    """#UseHook""":
    """#UseHook [On|Off]

Forces the use of the  hook to implement all or some keyboard hotkeys.""",

    """#Warn""":
    """#Warn [, WarningType, WarningMode]

Enables or disables warnings for specific conditions which may indicate an error, such as a typo or missing "global" declaration.""",

    """#WinActivateForce""":
    """#WinActivateForce

Skips the gentle method of activating a window and goes straight to the forceful method. """,

    "ACos": "",
    "ASin": "",
    "ATan": "",
    "A_AhkPAth": "",
    "A_AhkVersion": "",
    "A_AppData": "",
    "A_AppDataCommon": "",
    "A_AutoTrim": "",
    "A_BatchLines": "",
    "A_CaretX": "",
    "A_CaretY": "",
    "A_ComputerName": "",
    "A_ControlDelay": "",
    "A_Cursor": "",
    "A_DD": "",
    "A_DDD": "",
    "A_DDDD": "",
    "A_DefaultMouseSpeed": "",
    "A_Desktop": "",
    "A_DesktopCommon": "",
    "A_DetectHiddenText": "",
    "A_DetectHiddenWindows": "",
    "A_EndChar": "",
    "A_EventInfo": "",
    "A_ExitReason": "",
    "A_FormatFloat": "",
    "A_FormatInteger": "",
    "A_Gui": "",
    "A_GuiControl": "",
    "A_GuiControlEvent": "",
    "A_GuiEvent": "",
    "A_GuiHeight": "",
    "A_GuiWidth": "",
    "A_GuiX": "",
    "A_GuiY": "",
    "A_Hour": "",
    "A_IPAddress1": "",
    "A_IPAddress2": "",
    "A_IPAddress3": "",
    "A_IPAddress4": "",
    "A_IconFile": "",
    "A_IconHidden": "",
    "A_IconNumber": "",
    "A_IconTip": "",
    "A_Index": "",
    "A_IsAdmin": "",
    "A_IsCompiled": "",
    "A_IsSuspended": "",
    "A_KeyDelay": "",
    "A_Language": "",
    "A_LastError": "",
    "A_LineFile": "",
    "A_LineNumber": "",
    "A_LoopField": "",
    "A_LoopFileName": "",
    "A_LoopReadLine": "",
    "A_LoopRegName": "",
    "A_MM": "",
    "A_MMM": "",
    "A_MMMM": "",
    "A_MSec": "",
    "A_Min": "",
    "A_MouseDelay": "",
    "A_MyDocuments": "",
    "A_Now": "",
    "A_NowUTC": "",
    "A_OSType": "",
    "A_OSVersion": "",
    "A_PriorHotkey": "",
    "A_ProgramFiles": "",
    "A_Programs": "",
    "A_ProgramsCommon": "",
    "A_STringCaseSense": "",
    "A_ScreenHeight": "",
    "A_ScreenWidth": "",
    "A_ScriptDir": "",
    "A_ScriptFullPath": "",
    "A_ScriptName": "",
    "A_Sec": "",
    "A_Space": "",
    "A_StartMenu": "",
    "A_StartMenuCommon": "",
    "A_Startup": "",
    "A_StartupCommon": "",
    "A_Tab": "",
    "A_Temp": "",
    "A_ThisHotkey": "",
    "A_ThisMenu": "",
    "A_ThisMenuItem": "",
    "A_ThisMenuItemPos": "",
    "A_TickCount": "",
    "A_TimeIdle": "",
    "A_TimeIdlePhysical": "",
    "A_TimeSincePriorHotkey": "",
    "A_TimeSinceThisHotkey": "",
    "A_TitleMatchMode": "",
    "A_TitleMatchModeSpeed": "",
    "A_UserName": "",
    "A_WDay": "",
    "A_WinDelay": "",
    "A_WinDir": "",
    "A_WorkingDir": "",
    "A_YWeek": "",
    "A_YYYY": "",
    "Abs": "",
    "AllowSameLineComments": "",
    "Asc": "",
    "Ceil": "",
    "Chr": "",
    "Clipboard": "",
    "ClipboardAll": "",
    "ClipboardTimeout": "",
    "ComSpec": "",
    "CommentFlag": "",
    "Cos": "",
    "ErrorLevel": "",
    "ErrorStdOut": "",
    "EscapeChar": "",
    "Exp": "",
    "FileExist": "",
    "Floor": "",
    "Gui": "",
    "HotKeyModifierTimeout": "",
    "HotkeyInterval": "",
    "Hotstring": "",
    "InStr": "",
    "Include": "",
    "IncludeAgain": "",
    "InstallKeybdHook": "",
    "InstallMouseHook": "",
    "IsLabel": "",
    "Ln": "",
    "Log": "",
    "MaxHotkeysPerInterval": "",
    "MaxMem": "",
    "MaxThreads": "",
    "MaxThreadsBuffer": "",
    "MaxThreadsPerHotkey": "",
    "Mod": "",
    "NoEnv": "",
    "NoTrayIcon": "",
    "Persistent": "",
    "ProgramFiles": "",
    "Round": "",
    "SetNumScrollCapsLockState": "",
    "Sin": "",
    "SingleInstance": "",
    "Sqrt": "",
    "StatusBarGetText": "",
    "SubStr": "",
    "Tan": "",
    "URLDownloadToFile": "",
    "UseHook": "",
    "VarSetCapacity": "",
    "WinActivateForce": "",
    "WinActive": "",
    "ahk_class": "",
    "ahk_group": "",
    "ahk_id": "",
    "ahk_pid": "",
    "contained": "",
    "contained": "",
    "false": "",
    "global": "",
    "local": "",
    "true": "",
}

def ahk_complete(base):
    import vim
    lbase = base.lower()
    vim.command("let g:ahk_complete_dict = []")
    for k, v in AHK_DICT.iteritems():
        if k.lower().startswith(lbase):
            try:
                vim.command(r"""call add(g:ahk_complete_dict, {'word':'%s', 'info':'%s', 'icase':1})""" % (k, v))
            except vim.error as e:
                import sys
                print >> sys.stderr, str(e)
