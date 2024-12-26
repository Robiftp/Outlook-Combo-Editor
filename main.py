import re

def filter_microsoft_emails(input_file, output_file):
    microsoft_domains = [
        "@hotmail.com", "@hotmail.es", "@hotmail.be", "@hotmail.ca", "@hotmail.ch",
        "@hotmail.cl", "@hotmail.co.jp", "@hotmail.co.th", "@hotmail.co.uk",
        "@hotmail.com.ar", "@hotmail.com.au", "@hotmail.com.br", "@hotmail.com.hk",
        "@hotmail.com.tr", "@hotmail.de", "@hotmail.dk", "@hotmail.fr", "@hotmail.gr",
        "@hotmail.hu", "@hotmail.it", "@hotmail.live", "@hotmail.my", "@hotmail.nl",
        "@hotmail.no", "@hotmail.se", "@hotmail.sg", "@live.com", "@live.be",
        "@live.ca", "@live.cl", "@live.cn", "@live.co.kr", "@live.co.uk", "@live.com.ar",
        "@live.com.au", "@live.com.mx", "@live.com.pt", "@live.com.sg", "@live.de",
        "@live.dk", "@live.fi", "@live.fr", "@live.it", "@live.jp", "@live.nl",
        "@live.no", "@live.ru", "@live.se", "@msn.com", "@msn.se", "@outlook.com",
        "@outlook.at", "@outlook.be", "@outlook.cl", "@outlook.co.id", "@outlook.co.th",
        "@outlook.com.ar", "@outlook.com.au", "@outlook.com.br", "@outlook.com.vn",
        "@outlook.cz", "@outlook.de", "@outlook.dk", "@outlook.es", "@outlook.fr",
        "@outlook.hu", "@outlook.it", "@outlook.jp", "@outlook.kr", "@outlook.my",
        "@outlook.pt", "@outlook.sa", "@windowslive.com"
    ]
    
    microsoft_pattern = re.compile(
        rf"\b[\w.%+-]+({'|'.join(map(re.escape, microsoft_domains))})\b",
        re.IGNORECASE
    )
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            filtered_parts = []
            for part in parts:
                match = microsoft_pattern.search(part)
                if match:
                    filtered_parts.append(part)
                elif not re.search(r"\b[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", part):
                    filtered_parts.append(part)
            if filtered_parts:
                outfile.write(" ".join(filtered_parts) + "\n")

input_file_path = "input_emails.txt"
output_file_path = "filtered_emails.txt"
filter_microsoft_emails(input_file_path, output_file_path)

print(f"Filtered emails saved to {output_file_path}")
