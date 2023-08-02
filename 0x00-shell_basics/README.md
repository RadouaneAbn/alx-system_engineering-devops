**0x00. Shell, basics**:

0-current_working_director: (pwd)  
this script prints the path name of the current working directory.

1-listit: (ls)  
this script displays the contents list of the current directory.

2-bring_me_home: (cd)  
this script changes the working directory to the user's home directory (/root).

3-listfiles: (ls -l)  
this script displays the contents list of the current directory in a long format.

4-listmorefiles: (ls -la)  
this script displays the contents list of the current directory including hidden files in a long format.

5-listfilesdigitonly: (ls -lan)  
this script displays the contents list of the current directory with user and group IDs  including hidden files in long format.

6-firstdirectory: (mkdir)  
this script creates a directory named my_first_directory int /tmp/ directory.

7-movethatfile: (mv)  
this script will move a file named betty from /tmp/ to /tmp/my_first_directory.

8-firstdelete: (rm)  
this script will remove a file named betty from /tmp/my_first_directory.

9-firstdirdeletion: (rm -r)  
this script will remove a directory named my_first_directory.

10-back: (cd --)  
this script will change the working directory to previous one.

11-lists: (ls -la . .. /boot)  
this script lists the files including hidden ones in the working directory '.', parent of the working directory '..' and the /boot directory in long format.

12-file_type: (file)  
this script will print the type of the file named iamafile in the /tmp directory.

13-symbolic_link: (ls -s)  
this script will create a symbolic link to /bin/ls, named __ls__ in the working directory.

14-copy_html: (cp -u)  
this script will copy all HTML files from working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

100-lets_move: (mv)  
this script will move all files beginning with an uppercase letter to the directory /tmp/u/.

101-clean_emacs: (rm)  
this script will delete all files in the current working directory the end with character ~(emacs backup files).

102-tree: (mkdir -p)  
this script will create a directory named welcome and inside of welcome/ will create another directory named /to and inside of welcome/to/ will create a directory named school.

