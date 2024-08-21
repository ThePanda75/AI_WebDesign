from jinja2 import Template

def generate_html(description):
    # Exemple simple de template HTML
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Generated Site</title>
    </head>
    <body>
        <h1>{{ description }}</h1>
    </body>
    </html>
    """

    # Crée un template Jinja2
    template = Template(html_template)
    
    # Génère le HTML avec la description
    return template.render(description=description)

# Exemple d'utilisation
if __name__ == "__main__":
    description = "Welcome to My New Website"
    html_content = generate_html(description)
    
    # Enregistrer le HTML dans un fichier
    with open("index.html", "w") as file:
        file.write(html_content)

    print("HTML file generated successfully.")