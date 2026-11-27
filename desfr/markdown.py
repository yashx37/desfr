import re

def extract_headings(content):
    headings = []
    document_title_found = False
    code_fence = None

    for line_number, line in enumerate(content.splitlines(), start=1):

        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)

        if fence_match:
            marker = fence_match.group(1)

            if code_fence is None:
                code_fence = marker
            elif marker[0] == code_fence[0] and len(marker) >= len(code_fence):
                if re.match(r"^\s*(`{3,}|~{3,})\s*$", line):
                    code_fence = None
            continue

        if code_fence is not None:
            continue


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

def extract_section(content, headings, section_number):
    target = next( 
        (h for h in headings if h["number"] == section_number), None
        )

    if target is None:
        return None

    lines = content.splitlines()

    start = target["line"]-1
    end = len(lines)

    for heading in headings:
        if heading["line"] <= target["line"]:
            continue

        if heading["level"] <= target["level"]:
            end = heading["line"]-1
            break

    return "\n".join(lines[start:end])