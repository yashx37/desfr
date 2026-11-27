import re

def extract_headings(content):
    headings = []
    document_title_found = False

    for line_number, line in enumerate(content.splitlines(), start=1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)

        if match:
            level = len(match.group(1))
            title = match.group(2)

            if level == 1 and not document_title_found:
                document_title_found = True
                continue

            title = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", title)

            headings.append({
                "level": level-1,
                "title": title,
                "line": line_number
            })
    
    return headings

def number_headings(headings):
    counters = [0] * 6

    for heading in headings:
        level = heading["level"]
        counters[level-1] += 1

        for i in range(level, 6):
            counters[i] = 0

        heading["number"] = ".".join(str(counters[i]) for i in range(level))

    return headings