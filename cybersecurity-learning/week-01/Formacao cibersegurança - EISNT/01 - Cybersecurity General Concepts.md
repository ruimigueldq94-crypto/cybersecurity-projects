# 🐧 Course - Cibersecurity  

📅 **Date:** 03/02/2025  
🔗 **Platform:** EISNT  
🏆 **Goal:** Learn the fundamentals of Cibersecurity  

---  

## Cibersecurity Overview  
Cibersecurity refers to the set of technologies, processes, and practices aimed at protecting networks, devices, programs, and data from attacks, damage, or unauthorized access.  

### Core Principles  
- **Confidentiality**  
- **Integrity**  
- **Availability**  

### Concerns in Cibersecurity  
- **Vulnerability**  
- **Threat**  
- **Risk**  

## Types of Threats  
### Malware  
Any type of unwanted software installed without consent. Subcategories include:  
- **Viruses**  
- **Worms**  
- **Trojans**  
- **Logic Bombs**  
- **Spyware**  
- **Adware**  
- **Ransomware**  

### Phishing  
Sending fraudulent messages that appear to come from a trusted source (e.g., bank, utility company, employer).  
- **Email Phishing**: An email impersonating a bank asking to verify a transaction by providing login credentials.  
- **Smishing** (Phishing via SMS/MMS): A message appearing to come from a bank, alerting suspicious activity and requesting confirmation through a link.  
- **Spear Phishing**: A targeted attack, e.g., an email directed at a financial manager, tricking them into making a transfer.  

### Social Engineering  
All deceptive techniques that manipulate someone into performing actions they wouldn’t normally do, often creating a sense of urgency to limit time for reflection.  

For this example, let’s refer to the attacker as the **malicious agent** and assume they are targeting us.  
- [https://thispersondoesnotexist.com/](https://thispersondoesnotexist.com/)  
- [https://www.fakenamegenerator.com](https://www.fakenamegenerator.com)  

### Social Engineering Indicators  
How to detect a fake account (never accept friendship requests from such accounts!):  
- Few friends (initially had only 12 friends).  
- Unusual name (e.g., foreign).  
- Few posts.  
- Persuasive or attractive texts.  
- Unusual location for the user.  
- Other suspicious signs.  

### Skimming & Carding  
- **Skimming**: Physically copying card data without the owner’s knowledge.  
- **Carding**: Fraudulent use of stolen credit/debit card information for online purchases.  

## Hackers & Ethical Hackers  
### Hacker  
- Gains unauthorized access to systems or networks.  
- Actions may constitute a crime.  

### Ethical Hacker  
- Performs similar activities but with **explicit authorization**.  
- The main goal is to identify vulnerabilities.  

## Kali Linux  
- Originally **BackTrack Linux** (2006), a Debian-based Linux distribution.  
- Rebranded as **Kali Linux** in 2013.  
- One of the most advanced open-source platforms for **security testing and penetration testing**.  

### Installing VirtualBox & Kali Linux Setup  
1. Install VirtualBox (choose the appropriate version for your OS).  
2. Install VirtualBox Extension Pack (enhances hardware and network compatibility, e.g., graphics, USB, etc.).  
3. In VirtualBox, shut down Kali Linux:  
   ```bash
   shutdown -P now
   ```  
4. In Kali Linux machine settings, **add a new network adapter**.  
5. Forward **port 22**.  

### Configuring SSH in Kali Linux  
1. Edit the SSH configuration file:  
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```  
   - To save and exit, press `CTRL + X`, then `Y` (yes).  
2. Restart and enable SSH on boot:  
   ```bash
   sudo systemctl restart ssh
   sudo systemctl enable ssh
   ```  
3. In Kali, create the `.ssh` folder to store the public key:  
   ```bash
   mkdir /home/kali/.ssh
   ```