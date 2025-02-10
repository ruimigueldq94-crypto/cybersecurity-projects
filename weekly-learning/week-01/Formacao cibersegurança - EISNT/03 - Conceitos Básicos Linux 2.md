# 🐧 Course - Linux Basics (Part 2)  

📅 **Date:** 05/02/2025  
🔗 **Platform:** EISNT  
🏆 **Goal:** Learn additional Linux fundamentals  

---  

## Linux – Keyboard Configuration  
```bash
sudo dpkg-reconfigure keyboard-configuration
sudo nano /etc/default/keyboard  # Manually edit the keyboard configuration
```
Save changes with `CTRL+X`, followed by `Y`. Then, apply the new configuration:
```bash
sudo systemctl restart keyboard-setup
```

## Linux – Time Zone Configuration  
```bash
sudo dpkg-reconfigure tzdata
cat /etc/timezone  # Check current time zone
```

## Linux – Date and Time  
Check system date and time:
```bash
date
```
Change system date and time:
```bash
sudo date MMDDhhmmYYYY  # Example: sudo date 120220302024
```

## Linux – Sync Date/Time with NTP  
Edit NTP server settings:
```bash
sudo nano /etc/systemd/timesyncd.conf
```
Restart the service:
```bash
sudo systemctl restart systemd-timesyncd
```
Verify the synchronization status:
```bash
timedatectl
journalctl -u systemd-timesyncd  # View last sync logs
```

## Linux – Creating Aliases  
Edit the `.bashrc` file:
```bash
nano .bashrc
```
Add:
```bash
alias cls='clear'
alias ls='ls -la'
alias re='sudo reboot'
alias out='sudo shutdown -P now'
```
Apply changes:
```bash
source .bashrc
```
Check defined aliases:
```bash
alias
```

## Linux – Hostname Configuration  
Check current hostname:
```bash
hostname
```
Change hostname to `kali`:
```bash
sudo hostnamectl set-hostname kali
```
Ensure `/etc/hosts` is updated accordingly.

## Linux – Routing Configuration  
View routing table:
```bash
route -n  # Does not support IPv6
ip route show  # Supports IPv6
```
Add a default route:
```bash
sudo route add default gw 10.0.2.254 eth1
```
To remove a route:
```bash
sudo route del default gw 10.0.2.254 eth1
```

## Linux – Scripting  
Create a simple script:
```bash
nano ola.sh
```
Add:
```bash
#!/bin/bash
echo ola $USER
pwd
date
```
Make the script executable:
```bash
chmod 700 ola.sh
```

## Linux – PATH Variable  
Display the current PATH:
```bash
echo $PATH
```
Add the current directory to PATH:
```bash
export PATH=$PATH:.
```

## Linux – Managing Services  
List active services:
```bash
systemctl list-units --type=service --state=active
```
Check the status of `ssh` service:
```bash
sudo systemctl status ssh
```
Start/Stop `ssh` service:
```bash
sudo systemctl start ssh
sudo systemctl stop ssh
```
Enable/Disable service at startup:
```bash
sudo systemctl enable ssh
sudo systemctl disable ssh
```

## Linux – Users and Groups  
Add a user:
```bash
sudo adduser antonio
```
Change user password:
```bash
sudo passwd antonio
```
Create a new group:
```bash
sudo addgroup comercial
```
Add a user to multiple groups:
```bash
sudo usermod -G financeiro,comercial antonio
```

## Linux – User Locking/Unlocking  
Lock user login:
```bash
sudo usermod -L antonio
```
Unlock user:
```bash
sudo usermod -U antonio
```

## Linux – Sudoers Configuration  
Check sudoers file:
```bash
sudo cat /etc/sudoers
```
Add a new user to sudo:
```bash
sudo adduser novouser
sudo usermod -G sudo novouser
```

## Linux – Installing Packages  
Update package list:
```bash
sudo apt-get update
```
Install a package (e.g., `htop`):
```bash
sudo apt-get install htop
```
Remove a package:
```bash
sudo apt-get remove htop
```

---  

This guide provides essential Linux commands for system administration and configuration. 🚀