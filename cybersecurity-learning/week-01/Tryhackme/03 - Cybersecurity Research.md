# 🛡️ Cybersecurity Research & Methodology

📅 **Date:** 05/02/2025  
🔗 **Platform:** TryHackMe, ExploitDB, Linux man pages  
🏆 **Goal:** Develop strong research skills for cybersecurity and ethical hacking.  

---

## 📌 Introduction
Effective research is the most important skill a hacker can have. Since hacking requires deep technical knowledge, understanding how to find information quickly is crucial. This documentation summarizes key research methodologies and tools used in cybersecurity.

Topics covered:
- 🔍 **Research Question Example**
- 🛠 **Vulnerability Searching Tools**
- 🐧 **Linux Manual Pages**

---

## 🎯 Example Research Question

### **Scenario**:
You download a JPEG image from a remote server and suspect hidden data inside. How do you extract it?

### **Research Steps:**
1️⃣ Search Google for **“hiding things inside images”** → Learn about **Steganography**.  
2️⃣ Search **“extract files using steganography”** → Find relevant tools like `steghide`.  
3️⃣ Search **“install steghide Linux”** → Learn to install it using `apt install steghide`.  
4️⃣ Search **“how to use steghide”** → Learn to extract hidden data using `steghide extract -sf image.jpg`.  

### **Key Takeaway:**
By iterating through search queries, we build knowledge step by step. Start broad, refine queries, and explore deeper aspects as needed.

---

## 🔎 Vulnerability Searching
When testing security, you need to identify vulnerabilities in software. Useful resources include:

🔹 [ExploitDB](https://www.exploit-db.com/) - Database of public exploits.  
🔹 [CVE Mitre](https://cve.mitre.org/) - Official registry of vulnerabilities.  
🔹 [NVD](https://nvd.nist.gov/) - National Vulnerability Database.

### **Example: Finding an Exploit for FuelCMS**
- **Search ExploitDB manually** or use `searchsploit fuel cms` in Kali Linux.
- Identify CVEs (e.g., `CVE-2020-17462`) to find more details.
- Use available exploits to test vulnerabilities (within ethical/legal boundaries).

---

## 🐧 Linux Manual Pages (man)
Linux tools come with built-in documentation via the `man` command. This is useful for understanding command syntax and options.

### **Example Commands:**
📌 **Find SSH usage:** `man ssh`  
📌 **List partitions:** `fdisk -l`  
📌 **Copy directories with SCP:** `scp -r source/ user@remote:/destination/`  
📌 **Start netcat in listen mode:** `nc -l -p 12345`  

---

## ✅ **Final Thoughts**
- **Any source** can be valuable, including blogs, forums, and Wikipedia.
- **Refining search queries** is a key skill for penetration testing.
- **Practice using CLI tools** like `searchsploit`, `man`, and `apt` to speed up workflow.

🚀 *Next steps: Continue learning by exploring advanced Google Dorking techniques!*