import re

def filter_microsoft_emails(input_file, output_file):
    microsoft_domains = [
        "@hotmail.com", "@live.com", "@outlook.com", "@hotmail.co.uk", "@hotmail.de",
        "@hotmail.fr", "@hotmail.it", "@hotmail.ca", "@live.co.uk", "@live.de",
        "@live.fr", "@live.com.au", "@live.jp", "@outlook.co.uk", "@outlook.de",
        "@outlook.fr", "@outlook.jp", "@outlook.in", "@outlook.com.br", "@msn.com",
        "@passport.com", "@windowslive.com", "@office365.com", "@email.com",
        "@live.com.ph", "@outlook.com.ph", "@outlook.office365.com", "@microsoft.com"
    ]
    
    microsoft_pattern = re.compile(
        rf"\b[\w.%+-]+({'|'.join(map(re.escape, microsoft_domains))})\b"
    )
    
    seen_emails = set()
    
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
            
            filtered_line = " ".join(filtered_parts)
            
            if filtered_line and filtered_line not in seen_emails:
                seen_emails.add(filtered_line)
                outfile.write(filtered_line + "\n")

input_file_path = "input_emails.txt"
output_file_path = "filtered_emails.txt"
filter_microsoft_emails(input_file_path, output_file_path)

print(f"Filtered emails saved to {output_file_path}")
