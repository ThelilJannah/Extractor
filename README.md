## **README – Email and IP Extractor**

This Python tool scans text files or raw input and extracts **IPv4 addresses** and **email addresses** while automatically removing duplicates.
It’s handy for log analysis, forensics or data cleaning tasks.

---

### **Features**

* Extracts IPv4 addresses (e.g., `192.168.1.10`)
* Extracts valid email addresses (e.g., `no-reply@domain.com`)
* Filters out duplicates automatically
* Handles noisy/unstructured text
* Lightweight — no external dependencies

---

### **Usage**

1. **Install Python 3**
   Make sure Python 3 is installed:

   ```bash
   python3 --version
   ```

2. **Place your target file**
   Put the text file (e.g., `noisy_data.txt`) in the same directory as `extractor.py`.

3. **Run the extractor**

   ```bash
   python3 extractor.py
   ```

4. **Follow prompts (if any)**
   The script will process the file and print the results.

---

### **Example Input**

(noisy_data.txt)

```
User connected from 192.168.1.10 at 12:03PM
Contact: support@company.com
Retrying connection to 10.0.0.45 failed.
Email: no-reply@domain.org
```

---

### **Example Output**

```
Number of non dup IPs found: 2
192.168.1.10
10.0.0.45

Number of non dup emails found: 2
support@company.com
no-reply@domain.org
```

---

### **Misc**

* You can modify the filename or input path directly in `extractor.py` if needed.
* To redirect output to a file:

  ```bash
  python3 extractor.py > results.txt
  ```

