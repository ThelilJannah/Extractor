import re
# noinspection PyBroadException

try:
    file_path = input("Enter a path to txt/log file: ").lower()
    print()
    with open(file_path, "r") as f:
        pass
except:
    print("Please enter a valid path.")
    quit()

def extract_emails(file):
    emails = []
    with open(file, "r") as f:
        pattern = re.compile(r"\w+@.+\.*\w+$")
        for line in f:
            found = pattern.findall(line)
            if found:
                emails.extend(found)
                
    emails = set(emails)
    print(f"Number of non-duplicates IPs found: {len(emails)}")
    print()
    for email in emails:
        print(email)
    print()
    
def extract_ips(file):
    list_of_ips = []

    with open(file, 'r') as file:
        lines = file.readlines()
        pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        for i in lines:
            j = re.findall(pattern, i)
            if j and j not in list_of_ips:
                list_of_ips.extend(j)
    ips = set(list_of_ips)
    print(f"Number of non-duplicates IPs found: {len(ips)}")
    print()
    for ip in ips:
        print(ip)
    print()

while True:
    mode = input("Choose an option for extractor type (ip/email) or q to quit: ").lower()
    print()
    if mode == "ip":
        extract_ips(file_path)
    elif mode == "email":
        extract_emails(file_path)
    elif mode == "q":
        quit()
    else:
        print("Please enter a valid option.")
        continue