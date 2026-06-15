import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to add <span class="text-danger">*</span> to all labels that belong to required fields.
# We also need to remove 'required' from Tesorero fields.

# First, remove required from Tesorero fields
content = re.sub(r'(id="orgTesorero".*?) required', r'\1', content)
content = re.sub(r'(id="orgTesoreroDNI".*?) required', r'\1', content)
content = re.sub(r'(id="orgTesoreroNacimiento".*?) required', r'\1', content)

# Now, we find all blocks: label ... then input/select/textarea with 'required'
# It's better to just do string replacements for the specific labels since the structure varies slightly.

labels_to_star = [
    'Nombre de la Organización',
    'Zona Vecinal',
    'Domicilio Legal',
    'N° de Registro (RUOS)',
    'Fecha de Fundación',
    'N° de Miembros',
    'Tipo de Organización ',
    'Nivel ',
    'Fines y Objetivo Social ',
    'Nombre Completo', # Wait, Presidente has Nombre Completo, Tesorero has Nombre Completo.
    'DNI',
    'Fecha de Nacimiento',
    'Celular',
    'Correo Electrónico',
    'Profesión / Ocupación',
    'Cargo en la Organización',
    'Grado de Instrucción'
]

# Let's write a regex that matches: <label ...>TEXT</label> followed by whitespace and an input/select/textarea that contains 'required'
# Actually, since python regex is tricky with variable spacing, let's just do it line by line:

lines = content.split('\n')
for i, line in enumerate(lines):
    if '<label' in line and 'class="form-label fw-semibold"' in line or 'class="form-label small fw-semibold text-muted"' in line:
        # Check if the next line or the one after has 'required'
        is_required = False
        for j in range(1, 4):
            if i + j < len(lines) and 'required' in lines[i+j]:
                is_required = True
                break
        
        if is_required:
            # We add <span class="text-danger">*</span> before the closing </label>
            # OR before the <i class="fas fa-question-circle if it exists
            if '<i class="fas fa-question-circle' in line:
                lines[i] = line.replace('<i class="fas fa-question-circle', '<span class="text-danger">*</span> <i class="fas fa-question-circle')
            else:
                lines[i] = line.replace('</label>', ' <span class="text-danger">*</span></label>')

with open('index.html', 'w') as f:
    f.write('\n'.join(lines))

print("Done")
