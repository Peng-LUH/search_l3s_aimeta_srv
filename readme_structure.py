import os

def generate_structure(root_dir):
    structure = []

    for root, dirs, files in os.walk(root_dir):
        if not os.path.basename(root)=="__pycache__":
            level = root.replace(root_dir, '').count(os.sep)
            indent = '|'+ ' ' * 4 * level
            structure.append(f"{indent}├── {os.path.basename(root)}/")

        # sub_indent = ' ' * 2 * (level + 1)
        # for f in files:
        #     structure.append(f"{sub_indent}├── {f}")

    return "\n".join(structure)

def main():
    project_root = '/home/rathee/search/aims/search_l3s_aimeta_srv/src'  # Change this if your script is not in the root of the project
    structure = generate_structure(project_root)

    print(structure)

main()    