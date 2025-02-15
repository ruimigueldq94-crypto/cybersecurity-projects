# 🐧 Course - Linux Security Best Practices  

📅 **Date:** 05/02/2025 
🔗 **Platform:** EISNT  
🏆 **Goal:** Learn essential Linux security practices  

---  

## Updating System Packages
Updating the list of available applications and their respective versions:
```bash
sudo apt-get update
```
Upgrade installed applications/packages to the latest version:
```bash
sudo apt-get upgrade
```

## Avoiding Unnecessary Applications
A vulnerable application can be exploited to compromise other applications or even the system itself. To list active services:
```bash
sudo systemctl list-units -t service --state=active
```
To remove an unnecessary service (e.g., Apache2):
```bash
sudo systemctl stop apache2
sudo systemctl disable apache2
sudo apt remove apache2 --purge
```
(`--purge` ensures removal of configuration files as well.)

## Identifying Running Services and Open Ports
To check active services and the ports they are listening on:
```bash
sudo ss -tulpn
```
Alternatively, using netstat:
```bash
sudo netstat -tulpn
```

## Secure Password Management
- Use strong passwords with at least 10 characters, including special characters, numbers, and uppercase/lowercase letters.
- Generate a secure password:
```bash
pwmake 64
```
- Follow NIST best practices.
- Use a password manager to avoid reusing passwords across different systems.

### Installing a Local Password Manager (Keepass)
A good practice is to sync the password database (Database.kdbx) to Google Drive while keeping the key file (Database.keyx) stored separately (e.g., on a USB drive).

## Encrypting Sensitive Data
Download VeraCrypt:  
🔗 [VeraCrypt Official Download](https://www.veracrypt.fr/en/Downloads.html)

For Windows users: Install the VeraCrypt version for Windows.

## Locking the System
To install and use `vlock` for terminal security:
```bash
sudo apt-get install vlock
vlock
```

## Disabling IPv6
Even if not actively used, IPv6 can introduce security risks. To disable it:
```bash
sudo nano /etc/sysctl.conf
```
Add these lines at the end of the file:
```bash
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv6.conf.eth0.disable_ipv6 = 1
```
Save and exit (CTRL+X in nano). Apply changes:
```bash
sudo sysctl -p
```

## Secure DNS Configuration
To configure a secure DNS server:
```bash
sudo nano /etc/resolv.conf
```
Add the following:
```bash
nameserver 9.9.9.9
nameserver 1.1.1.1
nameserver 8.8.8.8
```
Save and exit (CTRL+X in nano).

### Preventing Unwanted Changes to DNS Configuration
Make the file immutable to prevent unauthorized modifications:
```bash
sudo chattr +i /etc/resolv.conf
```
To remove the immutable attribute if needed:
```bash
sudo chattr -i /etc/resolv.conf
```
Check file attributes:
```bash
sudo lsattr /etc/resolv.conf
```
Allow only append operations (useful for log files):
```bash
sudo chattr +a logfile.log
```

## Practical Exercise
- Create an encrypted volume using VeraCrypt (e.g., 500MB in size).
- Store the encrypted volume securely (e.g., Google Drive).
- Use a misleading filename for added security, such as:
  - `BatizadoDoLuis.avi`
  - `FeriasFamilia2023.mp4`
  - `Aniversario_Pedro_10anos.mov`