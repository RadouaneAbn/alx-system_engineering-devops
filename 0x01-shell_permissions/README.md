**0x01. Shell, permissions**

0-iam_betty: (su)  
this script will switch current user to user betty.

1-who_am_i: (whoami)  
this script will print the username of the current user.

2-groups: (groups)  
this script will print all groups that the current user is part of.

3-new_owner: (chown)  
this script will change the owner of a file named hello to a user named betty.

4-empty: (touch)  
this script will create a new file named hello.

5-execute: (chmod)  
this script will add execute permission to the owner of the file hello.

6-multiple_permissions: (chmod)  
this script will add execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody: (chmod)
this script will add execute permission to the owner, the group owner and the other users.

8-James_Bond: (chmod)  
this script will set the permission 007  to the file hello.

9-John_Doe: (chmod)  
this script will set the mode of the file hello to 753.

10-mirror_permissions: (chmod)  
this script will set the mode of file hello the same as olleh.

11-directories_permissions: (chmod)  
this script adds execute permission to all subdirectories of the current directory.

12-directory_permissions: (chmod)  
this script will create a directory named my_dir with permissions 751 in the working directory.

13-change_group: (chmod)  
this script will change the group owner to school for the file hello.

