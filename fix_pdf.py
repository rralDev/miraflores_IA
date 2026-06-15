import re

with open('/Users/rral/Working/Hackaton/pp_miraflores/script.js', 'r') as f:
    lines = f.readlines()

new_lines = []
in_draw_agente = False

for line in lines:
    if "const drawAgenteBox = (startY, title, isAlterno) => {" in line:
        in_draw_agente = True

    if in_draw_agente and "doc.text(datos[" in line and "setTextColor" not in line:
        # It's an input value in drawAgenteBox
        leading_space = line[:len(line) - len(line.lstrip())]
        new_lines.append(f"{leading_space}doc.setTextColor(0, 86, 179);\n")
        new_lines.append(line)
        new_lines.append(f"{leading_space}doc.setTextColor(0, 0, 0);\n")
        continue

    # Increase font size slightly in drawAgenteBox
    if in_draw_agente and "doc.setFontSize(8);" in line:
        new_lines.append(line.replace("doc.setFontSize(8);", "doc.setFontSize(9);"))
        continue
    if in_draw_agente and "doc.setFontSize(7);" in line:
        new_lines.append(line.replace("doc.setFontSize(7);", "doc.setFontSize(8);"))
        continue

    if "};" in line and in_draw_agente:
        in_draw_agente = False

    new_lines.append(line)

with open('/Users/rral/Working/Hackaton/pp_miraflores/script.js', 'w') as f:
    f.writelines(new_lines)

print("Done")
