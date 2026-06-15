import re

with open('/Users/rral/Working/Hackaton/pp_miraflores/script.js', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # 1. Fix chart labels
    if "const labels = Object.keys(conteoZonas).sort();" in line:
        new_lines.append("    const labelsOriginales = Object.keys(conteoZonas).sort();\n")
        new_lines.append("    const labels = labelsOriginales.map(l => l.replace('Zona ', 'Z'));\n")
        continue
    if "const data = labels.map(label => conteoZonas[label]);" in line:
        new_lines.append("    const data = labelsOriginales.map(label => conteoZonas[label]);\n")
        continue
    
    # 2. Color the input data blue
    if "doc.text(" in line and ("datos." in line or "finesLines" in line or "calcEdad" in line or "getVal(" in line or "getRepVal(" in line):
        leading_space = line[:len(line) - len(line.lstrip())]
        new_lines.append(f"{leading_space}doc.setTextColor(0, 86, 179);\n")
        new_lines.append(line)
        new_lines.append(f"{leading_space}doc.setTextColor(0, 0, 0);\n")
        continue

    new_lines.append(line)

with open('/Users/rral/Working/Hackaton/pp_miraflores/script.js', 'w') as f:
    f.writelines(new_lines)
print("Done")
