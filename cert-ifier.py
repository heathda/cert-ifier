import subprocess

#Open file with domain addresses.  Each domain on its own line.
search_domain_txt_file = open("/home/user/ssl-cert-verify/domain_input.txt", "r")
#Read the file
domain_array_from_file = search_domain_txt_file.read()
#Create an array consisting of each domain
domain_array = domain_array_from_file.split("\n")
#Close file
search_domain_txt_file.close()
#Define variable(s)
substring = "Verification: OK"

#loop through the domains..
for i in domain_array:
    #Perform openssl query to check the certificate status
    openssl_raw = subprocess.getoutput("echo -n | openssl s_client -connect " + i + ":443")
    if substring in openssl_raw:
        print (i + " PASS")
    else:
        print (i + " FAIL")
