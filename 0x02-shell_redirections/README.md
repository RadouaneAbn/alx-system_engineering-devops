Shell, I/O Redirections and filters:  

0-hello_world:  (echo)  
	this script will print "Hello, World".

1-confused_smiley:  (echo)  
	this script will print "(Ôo)'.

2-hellofile:  (cat)  
	this script will display the content of the **/etc/passwd** file.

3-twofiles:  (cat)  
	this script will display the content of two files, **/etc/passwd** and **/etc/hosts**.

4-lastlines: (tail)  
	this script will display the last 10 lines of the file **/etc/passwd**.

5-firstlines: (head)  
	this script will display the first 10 lines of the file **/etc/passwd**.

6-third_line: (head|tail)  
	this script will display the third line of the file iacta.

7-file: (echo)  
	this script will create a file named '\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)' and will contain "Best School"

8-cwd_state: (ls>)  
	this script will write the result of the command 'ls -la' into the file "ls_cwd_content" if it exist, if doesn't it will create it and then write the result in it.

9-duplicate_last_line: (tail)  
	this script will duplicate the last line of the file iacta.

10-no_more_js: (find)  
	this script delete all regular files with .js extension from the curent directory and all its subdirectories.

11-directories: (find)  
	this script will counts the number of directories and sub-directories in the current directory.

12-newest_files: (ls)  
	this script will displays the 10 newest files in the current directory.

13-unique: (sort)  
	this script will take a list of words as input and prints only words that appear exactly once.

14-findthatword: (cat|grep)  
	this script will display lines containing the pattern “root” from the file /etc/passwd.

15-countthatword: (cat|grep)
	this script will display the number of lines that contain the pattern “bin” in the file /etc/passwd.

16-whatsnext: (cat|grep)  
	this script display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

17-hidethisword: (cat|grep)  
	this script display lines in the file /etc/passwd that do not contain the pattern “bin”.

18-letteronly: (cat|grep)  
	this script display all lines of the file /etc/ssh/sshd_config starting with a letter.

19-AZ: (cat|tr)  
	this script will replace all characters A and c from input to Z and e respectively.

20-hiago: (cat|tr)  
	this script will removes all letters c and C from input.

21-reverse: (cat|rev)  
	this script will reverse its input.

22-users_and_homes: (cut)  
	this script will display all users and their home directories sorted by users.

100-empty_casks: (find)  
	this script will find all empty files and directories in the current directory and all subdirectories.

101-gifs: (find)  
	this script will list all the **.git** files in the current directory and all its subdirectories, including hidden files and files should be sorted by byte value, but case insensitive.

102-acrostic: (cut)  
	this script will decode acrostics that use the first letter of each line.
