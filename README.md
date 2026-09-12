# Learning Python: Automation Scripts

A collection of Python scripts I built to automate everyday tasks while learning Python.

## The Projects

<details>
<summary><b>🛡️ 1. Password Breach Checker</b></summary>

Checks how many times a password has been leaked in data breaches using the Have I Been Pwned API. To protect user privacy, it implements K-Anonymity so it only sends the first 5 characters of the hashed password to the API, performing the final match securely on your local machine.

**Terminal Preview:**
```bash
$ python checkmypass.py
Loaded 2 passwords to check safely.

Checking: ***********
*********** was found 35,412 times... you should probably change your password.
------------------------------
Checking: ******
****** was NOT leaked, you are safe.
------------------------------
```

**How to run it safely:**
To keep your real passwords off GitHub and out of your terminal command history, this script reads from a localized `.env` file.
1. Copy the template file: `cp .env.example .env`
2. Open `.env` and add your passwords separated by commas: `secret_pw=examplepassword1,examplepassword2`
3. Run the script: `python checkmypass.py`
</details>

<details>
<summary><b>📨 2. Email Sender</b></summary>

Logs into an SMTP server with Python's built in `smtplib` and sends an HTML email using a template file so the message body isn't a plain string in the code.
</details>

<details>
<summary><b>📄 3. PDF Toolset (Merger & Watermarker)</b></summary>

A file utility script that uses the `pypdf` library to manipulate PDF files. It can cleanly merge a list of individual PDFs into a single file or apply a transparent security watermark overlay across multiple documents.
</details>

<details>
<summary><b>📸 4. Batch Image Processor</b></summary>

An automation script that scans a folder for `.jpg` images, converts them all into `.png` files saving the results in an output folder using the `Pillow` library.
</details>

---
*Note: The repository's `.gitignore` file is configured to prevent personal files (like .env) from being tracked or pushed to GitHub.*
