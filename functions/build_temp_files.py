import os


def build_temp_files( element , ndir ):

    root_path = os.getcwd()
    md_path = os.path.join(root_path, 'structure.md')
    layout_path = os.path.join(root_path, 'temp_layout_fs.tsx')
    imports_path = os.path.join(root_path, 'temp_imports_fs.tsx')

    with open(md_path, "r") as file:

        organismos = []

        for line in file:
            if line.strip().startswith('# **'+element+'**'):
                for line in file:
                    if line.startswith('## '):
                        organismos.append(line[2:].strip())
                    elif line.strip() == "":
                        break
    

    with open(layout_path, 'w') as f:
        for organismo in organismos:
            f.write('      <'+organismo+' />\n')

    organismos.sort()

    path_fix = ""
    ndir = int(ndir)

    for i in range(ndir):
        path_fix = path_fix + "../"

    with open(imports_path, 'w') as f:
        f.write('import Layout from "'+path_fix+'../modules/Layout/Layout";\nimport { SEO } from "'+path_fix+'../modules/SEO/SEO";\n')
        for organismo in organismos:
            f.write('import { '+organismo+' } from "'+path_fix+'../sections/'+organismo+'/'+organismo+';"\n')