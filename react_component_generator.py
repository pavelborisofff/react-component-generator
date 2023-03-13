#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HOW TO USE
1. Copy this file to your any folder
2. Make it executable (you may need to use sudo)
   > chmod +x react_component_generator.py
3. Create symlink to /usr/local/bin (you may need to use sudo):
   > ln -s /...current_path.../react_component_generator.py /usr/local/bin/rcg
4. Now you can use it from any folder:
   > rcg PascalCase
   > rcg kebab-case
   > rcg onelowerword
   > rcg Titleword

HOW NOT TO USE
1. > rcg camelCase
   result will be just "case" folder with files
2. > rcg snake_case
   result will be Unknown arguments. Because it's not a Python!
"""

import argparse
import os
import re
import sys


def create_parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-n', '--name', default='MyComponent', type=str,
                         help='React component name like "MyComponent" (default). '
                              'Will be created folder "my-component" with files: '
                              '"index.ts", "my-component.module.scss", "my-component.tsx"\n')
    return _parser


def main(name: str):
    if re.findall(r'[^a-zA-Z0-9-]', name):
        sys.stderr.write('Component name must contain only letters, numbers and dashes')
        sys.exit(1)

    if name.lower() == name and '-' not in name:
        split_name = name.title()
        folder_name = name
    elif name.lower() == name and '-' in name:
        split_name = [group.title() for group in name.lower().split('-')]
        folder_name = '-'.join(split_name).lower()
    else:
        split_name = re.findall(r'[A-Z][^A-Z]*', name)
        folder_name = '-'.join(split_name).lower()

    component_name = ''.join(split_name)

    os.mkdir(folder_name)
    os.chdir(folder_name)

    with open('index.ts', 'w', encoding='utf-8') as f:
        f.write(f'import {component_name} from \'./{folder_name}\';\n\n'
                f'export default {component_name};')

    with open(f'{folder_name}.module.scss', 'w', encoding='utf-8') as f:
        f.write(f'.{component_name} {{\n'
                f'    \n'
                f'}}\n')

    with open(f'{folder_name}.tsx', 'w', encoding='utf-8') as f:
        f.write(f'import React from \'react\';\n'
                f'import cn from \'classnames\';\n'
                f'import styles from \'./{folder_name}.module.scss\';\n\n\n'
                f'interface I{component_name}Props {{\n'
                f'    props?: string;\n'
                f'}}\n\n'
                f'export const {component_name}: React.FC<I{component_name}Props> = ({{ props }}) => {{\n'
                f'    return (\n'
                f'        <div className={{cn(styles.{component_name})}}>\n'
                f'            {component_name}\n'
                f'        </div>\n'
                f'    );\n'
                f'}};\n\n'
                f'export default {component_name};')

    os.chdir('..')


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        parser.print_help()
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] in ['-n', '--name']:
        sys.stderr.write('Component name is required')
        sys.exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] not in ['-n', '--name']:
        main(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[1] in ['-n', '--name']:
        namespace = parser.parse_args(sys.argv[1:])
        main(namespace.name)
    else:
        sys.stderr.write('Unknown arguments')
        sys.exit(1)
