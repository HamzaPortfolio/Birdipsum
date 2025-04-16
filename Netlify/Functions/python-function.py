from zipfile import ZipFile
from pathlib import Path

# Creating the project structure for Netlify with Python function
project_root = Path("/mnt/data/hcss-netlify-python")
netlify_dir = project_root / "netlify"
functions_dir = netlify_dir / "functions"
functions_dir.mkdir(parents=True, exist_ok=True)

# 1. generate-css.js (Node.js function)
generate_css_js = """
exports.handler = async () => {
  const classes = {
    df: "display: flex;",
    db: "display: block;",
    dib: "display: inline-block;",
    jc-ctr: "justify-content: center;",
    ai-ctr: "align-items: center;",
    clr-black: "color: black;",
    clr-white: "color: white;",
    bg-red: "background-color: red;",
    bg-blue: "background-color: blue;"
  };

  let cssOutput = "";

  for (const className in classes) {
    cssOutput += `.${className} { ${classes[className]} }\n`;
  }

  return {
    statusCode: 200,
    headers: { "Content-Type": "text/css" },
    body: cssOutput
  };
};
"""
(functions_dir / "generate-css.js").write_text(generate_css_js.strip())

# 2. python-function.py (Optional Python function)
python_function = """
# Example Python function that could be used in Netlify (if Python support is enabled)
import json

def lambda_handler(event, context):
    classes = {
        "df": "display: flex;",
        "db": "display: block;",
        "dib": "display: inline-block;",
        "jc-ctr": "justify-content: center;",
        "ai-ctr": "align-items: center;",
        "clr-black": "color: black;",
        "clr-white": "color: white;",
        "bg-red": "background-color: red;",
        "bg-blue": "background-color: blue;"
    }
    
    cssOutput = ""
    for className, css in classes.items():
        cssOutput += f".{className} {{ {css} }}\n"
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/css'},
        'body': cssOutput
    }
"""
(functions_dir / "python-function.py").write_text(python_function.strip())

# 3. netlify.toml
netlify_toml = """
[functions]
  directory = "netlify/functions"
"""
(project_root / "netlify.toml").write_text(netlify_toml.strip())

# 4. index.html
index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HCSS Utility CSS</title>
  <link rel="stylesheet" href="/.netlify/functions/generate-css">
</head>
<body>
  <div class="df jc-ctr ai-ctr clr-black">
    Hello Flex World!
  </div>
</body>
</html>
"""
(project_root / "index.html").write_text(index_html.strip())

# 5. requirements.txt (For Python, optional)
requirements_txt = """
# Python dependencies (example)
flask==2.0.1
requests==2.25.1
"""
(project_root / "requirements.txt").write_text(requirements_txt.strip())

# 6. package.json (For Node.js, optional)
package_json = """
{
  "name": "netlify-functions",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
"""
(project_root / "package.json").write_text(package_json.strip())

# 7. README.md
readme_md = """
# HCSS Utility CSS

This project generates utility CSS using Netlify functions. You can extend the shortcodes and modify styles for your own needs.

## Usage

- Deploy on Netlify.
- The CSS is generated via the Netlify function and applied to your website.

## License

All rights reserved. Redistribution or modification without permission is prohibited.
"""
(project_root / "README.md").write_text(readme_md.strip())

# Create zip file
zip_path = "/mnt/data/hcss-netlify-python.zip"
with ZipFile(zip_path, "w") as zipf:
    for file in project_root.rglob("*"):
        zipf.write(file, file.relative_to(project_root))

zip_path
