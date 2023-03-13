# React Component Generator

### Description
This script generate React component with all necessary (for my opinion) files and folders.

Default structure:
```
+ my-component
  |_ index.ts
  |_ my-component.module.scss
  |_ my-component.tsx
```
You can also change script for your needs. Add folder with test for example).

### Requirements
- Linux/MacOS
- Python 3.6+ (you need not install any additional Python packages)

### How to use
1. Copy this file to your any folder
2. Make it executable:

    ```chmod +x react_component_generator.py``` (you may need to use sudo)
3. Create symlink to /usr/local/bin: 
 
    ```ln -s /...current_path.../react_component_generator.py /usr/local/bin/rcg``` (you may need to use sudo)
4. Now you can use it from any folder: 

   ```rcg PascalCase``` 

   ```rcg kebab-case```

   ```rcg onelowerword```

   ```rcg Titleword```

### How not to use

1.   ```rcg camelCase``` result will be ```case```
2.   ```rcg snake_case``` result will be ```Unknown arguments```. Because it's not a Python!