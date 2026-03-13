# Linux Command Cheat Sheet

1. Command: echo
What it does: 
The  command prints text or variables to the terminal. It is used for displaying messages or writing text into files.

Syntax:
echo [text]

Example: 
echo "Hello Linux"

Useful flags: 
-n → prints text without a new line 
-e → allows special characters like \n for new line


2. Command: whoami
What it does: 
Shows the username of the currently logged-in user.

Syntax:
whoami

Example: 
whoami


3. Command: ls
What it does: 
Lists all files and directories in the current directory. 

Syntax: 
ls [options] [path]

Example: 
ls -la

Useful flags: 
-l → shows detailed file information 
-a → shows hidden files 
-h → shows file sizes in human readable format


4. Command: cd
What it does: 
Changes the current working directory.

Syntax: 
cd [directory]

Example: 
cd Documents

Useful flags: 
cd .. → go back one directory 
cd ~ → go to home directory


5. Command: mkdir
What it does: 
Creates a new directory (folder).

Syntax: 
mkdir [directory_name]

Example: 
mkdir projects

Useful flags: 
-p → creates parent directories if they don't exist


6. Command: cat
What it does: 
Displays the contents of a file.

Syntax: 
cat [file]

Example: 
cat notes.txt

Useful flags: 
-n → shows line numbers 
-b → shows line numbers for non-empty lines


7. Command: pwd
What it does: 
Displays/finds out the full path of the current directory you are working in.

Syntax: 
pwd

Example: 
pwd


7. Command: find
What it does: 
Searches for files and directories within a specific location in the system without exploring anything else.

Syntax: 
find [path] [condition]

Example: 
find /home -name file.txt

Useful flags: 
-name → search by file name 
-type f → search for files 
-type d → search for directories


8. Command: grep
What it does: 
Searches for specific text/contents inside files.

Syntax: 
grep [pattern] [file]

Example: 
grep "error" log.txt

Useful flags: 
-i → ignore case sensitivity 
-r → search recursively in directories 
-n → show line numbers

9.Command: touch

What it does:
Creates a new empty file or updates the timestamp of an existing file.

Syntax:
touch [file_name]

Example:
touch notes.txt


10.Command: cp

What it does:
Copies files or directories from one location to another.

Syntax:
cp [source] [destination]

Example:
cp file.txt backup.txt

Useful flags:
-r → copy directories recursively


11.Command: mv

What it does:
Moves files or directories and also rename files.

Syntax:
mv [source] [destination]

Example:
mv file.txt documents/


12.Command: nano

What it does:
Opens a file using the Nano text editor so it can be edited directly in the terminal.

Syntax:
nano [file]

Example:
nano notes.md


13.Command: ping

What it does:
Tests the connectivity between our computer and another host on the network.

Syntax:
ping [host]

Example:
ping google.com


14.Command: ssh

What it does:
Connects securely to another computer or server over the network.

Syntax:
ssh user@host

Example:
ssh bandit0@bandit.labs.overthewire.org
