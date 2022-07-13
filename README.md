# cert-ifier
### Quick script to verify site certificate status (Verification: OK vs Self-signed)

Designed to perform an **openssl s_client -connect** from a list of domains and then print it to the console so it can be easily copy/imported into excel for further analysis/sharing/presentation.

### Directions  
Create a file called domain_input.txt.  
Paste a single domain address on each line.  
Run cert-ifier.py in the same directory as domain_input.txt  

### Be sure to edit the code to change the domain_input.txt directory path to reprsent the location on your system.

### Inputs:

pypi.org  
grafana.com  
raw.githubusercontent.com  
motd.ubuntu.com  

### Outputs:

pypi.org PASS  
grafana.com FAIL  
raw.githubusercontent.com FAIL  
motd.ubuntu.com PASS  
