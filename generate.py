import os

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vêtements - Comorshop</title>
  <style>
    * { box-sizing: border-box; }
    body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f9f9f9; color: #333; }
    header { text-align: center; margin-bottom: 30px; }
    header a { text-decoration: none; color: #0066cc; font-weight: bold; }
    h1 { margin-top: 10px; }
    .categorie-title { border-bottom: 2px solid #0066cc; padding-bottom: 8px; margin-top: 40px; color: #111; text-transform: capitalize; }
    .galerie { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 15px; }
    .carte-produit { background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .carte-produit img { max-width: 100%; height: 200px; object-fit: cover; border-radius: 6px; }
  </style>
</head>
<body>

  <header>
    <a href="index.html">← Retour à l'accueil</a>
    <h1>Collection Vêtements</h1>
  </header>
"""

base_dir = "vetements"
if os.path.exists(base_dir):
    for subfolder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, subfolder)
        if os.path.isdir(folder_path):
            title = subfolder.replace('_', ' ')
            html_content += f'  <h2 class="categorie-title">{title}</h2>\n'
            html_content += '  <div class="galerie">\n'
            for file in sorted(os.listdir(folder_path)):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                    img_path = f"{base_dir}/{subfolder}/{file}"
                    html_content += '    <div class="carte-produit">\n'
                    html_content += f'      <img src="{img_path}" alt="{title}">\n'
                    html_content += '    </div>\n'
            html_content += '  </div>\n'

html_content += """
</body>
</html>
"""

with open("vetements.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Génération réussie !")
