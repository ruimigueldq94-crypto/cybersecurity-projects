# 🤛 Course - Linux Basics  

📅 **Date:**  05/02/2025
🔗 **Platform:** EISNT  
🏆 **Goal:** Learn the fundamentals of Linux  

---  

## Linux - Basic Concepts  

### Key Terms  
- **Source Code**  
- **Open Source Code**  
- **Kernel**  
- **GNU**  

### Source Code  
Most software we acquire comes precompiled for an operating system, meaning the original source code is not available. Open-source code is the opposite—it allows users to view, modify, and distribute the code. Many Linux distributions are open source. However, some Linux-based systems do not disclose their source code (e.g., routers and smartphones).

### Kernel  
The kernel is the software layer that interacts directly with the hardware (e.g., disk, RAM). It communicates with device drivers, which define how hardware should be used.

### GNU  
GNU ("GNU's Not Unix") is a free software project started in 1983 by Richard Stallman. GNU lacked a kernel until 1991, when Linus Torvalds developed the Linux kernel. The combination resulted in the first Linux-based operating system.

### Features of Linux  
- **Multitasking**  
- **Multi-user support**  
- **Compatible with multiple architectures**:  
  - x86 and x86-64 (Intel & AMD processors)  
  - ARM (smartphones, IoT, embedded systems)  
  - PowerPC (servers, high-performance systems)  
  - MIPS (embedded systems, networking devices)  
  - SPARC (servers, high-performance systems)  
  - Home usage examples: PlayStation 3, Xbox 360  

## Basic Linux Commands  

### File and Directory Management  
- `ls` - List directories and files (similar to `dir` in MS-DOS)  
- `mkdir` - Create a directory  
- `tree` - Display a tree structure of directories  

### Navigating Directories  
- `cd` - Change directory  
- `pwd` - Print working directory (shows current path)  

### Understanding `ls` Output  
- `-` → Regular file  
- `d` → Directory  
- `l` → Symbolic link  
- `c` → Special character file (e.g., serial ports, disks)  
- `b` → Similar to `c`, but used for block devices  
- `s` → Sockets (communication between applications)  
- `p` → Pipes (linking processes)  

### File Operations  
- **Copy files**  
- **Move files**  
- **Delete files and directories**  

### Viewing File Contents  
- `cat` - Display the entire file  
- `less` - View a file page by page  
- `head` - Show the first 5 lines of a file  
- `tail` - Show the last 5 lines of a file  

### Searching Within Files  
- Search for words or patterns  
- Count lines, words, or characters  

### Finding Files and Directories  
- Locate files or folders  

## Stream Pointers in Linux  
Every process has three standard stream pointers:  
- `0 stdin` - Standard Input Stream (default: keyboard)  
- `1 stdout` - Standard Output Stream (default: screen)  
- `2 stderr` - Standard Error Stream (default: screen)  

## User and Host Information  
- `who` - List logged-in users  
- `whoami` - Display current user  
- `id` - Show user ID and group membership  
- `hostname` - Show machine name  

## Process Management  
- `ps -aux` - List running processes  
- `ps -aux | wc -l` - Count the number of running processes  
- `|` (pipe) - Redirects output of one command to another  

## Extracting Columns  
- `cut -d [delimiter] -f [column number] file` - Extract columns from a file  

## Linux Manuals and Command Lookup  
- `man [command]` - Open the manual for a command  
- `whatis [command]` - Briefly describe a command  
- `apropos [keyword]` - Search for commands related to a keyword  

## Hash Functions  
- `md5sum` - Compute MD5 hash of a file  
- `sha1sum` - Compute SHA-1 hash of a file  

### Example - Verifying File Integrity  
Download a file:  
```sh
wget https://releases.ubuntu.com/14.04.6/wubi.exe
```
Compute its hash:  
```sh
md5sum wubi.exe
sha1sum wubi.exe
```
Compare it with official hashes:  
- [MD5SUMS](https://releases.ubuntu.com/14.04.6/MD5SUMS)  
- [SHA1SUMS](https://releases.ubuntu.com/14.04.6/SHA1SUMS)  

## Backups and Compression  
### Creating Backups  
- `tar cvf archive.tar directory/` - Archive a directory  
- `tar xvf archive.tar` - Extract an archive  

### Compression with `tar`  
- `tar czfvP archive.tgz directory/` - Compress with gzip  
- `tar cjvf archive.tbz directory/` - Compress with bzip2  
- `tar -xzvf archive.tgz` - Extract gzip archive  
- `tar -xjvf archive.tbz` - Extract bzip2 archive  

### File Compression  
- `gzip -9 file.tar` - Compress using gzip  
- `gzip -d file.tar.gz` - Decompress gzip file  

## File Comparison  
- `diff file1.txt file2.txt` - Compare text files  
- `cmp file1.txt file2.txt` - Compare binary files  

## Text Editors  
### Using `nano`  
- `nano file.txt` - Open a file in Nano editor  
- Common shortcuts:  
  - `CTRL-X` - Exit  
  - `CTRL-R` - Read a file  
  - `CTRL-C` - Show cursor position  
  - `CTRL-K` - Cut text  
  - `CTRL-U` - Paste text  
  - `CTRL-O` - Save file  
  - `CTRL-W` - Search within the file  
  - `CTRL-A` - Move to the start of a line  
  - `CTRL-E` - Move to the end of a line  
  - `CTRL-G` - Show Nano manual  

---  

This document provides an overview of Linux fundamentals. Let me know if you need any additions or modifications! 🚀