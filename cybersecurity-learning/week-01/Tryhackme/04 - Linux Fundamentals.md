# 🐧 TryHackMe - Linux Fundamentals  

📅 **Date:** 06/02/2025 
🔗 **Platform:** [TryHackMe](https://tryhackme.com/)  
🏆 **Goal:** Learn the fundamentals of Linux through interactive exercises.  

---  

## 📌 Introduction  
Welcome to the **Linux Fundamentals** room series! This room introduces the basics of Linux, including:

- 🖥️ **Interacting with a Linux machine** in-browser.  
- 📂 **Navigating the file system** using essential commands.  
- 🔍 **Searching for files** efficiently.  
- 🛠️ **Understanding shell operators** to enhance command-line efficiency.  

By completing this room, you'll gain hands-on experience and confidence using Linux! 🚀  

---  

## 🔎 A Bit of Background on Linux  
### Where is Linux Used?  
Linux is one of the most widely used operating systems, powering:

- 🌐 **Websites & servers**
- 🚗 **Smart cars & infotainment systems**
- 🏪 **Point of Sale (PoS) systems**
- 🏭 **Industrial & critical infrastructure**

### Flavours of Linux  
Linux comes in many distributions (distros), each suited for different use cases. Some common ones include:

- **Ubuntu & Debian**: Popular for desktops and servers.
- **CentOS & Red Hat**: Enterprise-grade Linux.
- **Kali Linux**: Cybersecurity and penetration testing.  

For this room, we will be using **Ubuntu** due to its simplicity and widespread use.  

💡 *Fact: The first Linux OS was released in* **1991**.

---  

## 🛠️ Interacting With Your First Linux Machine (In-Browser)  
To get started, press the **Start Machine** button below. This will launch an Ubuntu machine in your browser.  

### **Basic Commands**  
| Command  | Description  |
|----------|-------------|
| `echo`   | Output text to the terminal.  |
| `whoami` | Show the current user.  |

### **Example Commands**  
```bash
$ echo "TryHackMe"
TryHackMe

$ whoami
tryhackme
```

---  

## 📂 Interacting With the Filesystem  
### **Essential Navigation Commands**  
| Command  | Description  |
|----------|-------------|
| `ls`     | List files and directories.  |
| `cd`     | Change directories.  |
| `cat`    | View the contents of a file.  |
| `pwd`    | Show the current directory path.  |

#### **Example Usage**  
```bash
$ ls
Documents  Pictures  folder1  folder2  folder3  folder4

$ cd folder4
$ ls
file.txt

$ cat file.txt
Hello World

$ pwd
/home/tryhackme/folder4
```

---  

## 🔍 Searching for Files  
### **Using `find` to Locate Files**  
```bash
$ find -name passwords.txt
./folder1/passwords.txt
```

### **Using `grep` to Search Within Files**  
```bash
$ grep "THM" access.log
THM{ACCESS}
```

---  

## ⚡ Introduction to Shell Operators  
| Operator | Description  |
|----------|-------------|
| `&`      | Run commands in the background.  |
| `&&`     | Run multiple commands in sequence.  |
| `>`      | Redirect output (overwrite).  |
| `>>`     | Redirect output (append).  |

#### **Example Usage**  
```bash
$ echo password123 > passwords  # Overwrites contents
$ echo tryhackme >> passwords   # Appends to file
```

---  

## ✅ Conclusion  
Great job on completing this room! You've covered:

✔️ **Why Linux is so widely used**
✔️ **Basic Linux commands**
✔️ **Navigating the filesystem**
✔️ **Finding files efficiently**
✔️ **Using shell operators to enhance productivity**

💡 *Practice regularly, and soon these commands will become second nature!* 🚀