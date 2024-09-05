from zipfile import ZipFile
import os

def proxies(username, password, endpoint, port):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Rutas a los archivos JSON y JS
    manifest_path = os.path.join(current_dir, 'manifest.json')
    background_path = os.path.join(current_dir, 'background.js')
    content_path = os.path.join(current_dir, 'content.js')
    with open(manifest_path, 'r') as f_manifest:
        manifest_content = f_manifest.read()

    with open(background_path, 'r') as f_background:
        background_content = f_background.read()
        background_content = background_content \
            .replace("__HOST__", endpoint) \
            .replace("__PORT__", str(port)) \
            .replace("__USERNAME__", username) \
            .replace("__PASSWORD__", password)

    with open(content_path, 'r') as f_content:
        content_content = f_content.read()

    extension_name = 'proxies_extension.zip'
    extension_path = os.path.join(current_dir, extension_name)

    with ZipFile(extension_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_content)
        zp.writestr("background.js", background_content)
        zp.writestr("content.js", content_content)

    return extension_path