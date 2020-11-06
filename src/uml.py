import subprocess
import json
from pathlib import Path

procedure = """
!unquoted procedure {name}($alias={name},$label=\"\")
gcp_component($alias,$label,$stereo="{name}",$sprite="{sprite}")
gcp_style({name})
!endprocedure
"""

filePathName = Path.cwd() / "src" / "gcp_products.json"
with open(filePathName, "r") as fp:
    products = json.load(fp)

filePathName = Path.cwd() / "dist" / "gcp_sprites.iuml"
with open(filePathName, "w") as fp:
    for product in products:
        print(product["name"]) 

        image_path = f"{Path.cwd()}/icons/medium/{product['name']}.png"
        cmd = ['java', '-Djava.awt.headless=true', 
            '-jar', 
            '/home/karl/Documents/plantuml.1.2020.18.jar',
            '-encodesprite',
            '16z',
            image_path]
        output = subprocess.check_output(cmd, universal_newlines=True)
        output = output.replace("sprite $", "sprite $gcp_")
        #print(output)
        fp.write(output)


filePathName = Path.cwd() / "dist" / "gcp_products.iuml"
with open(filePathName, "w") as fp:
    for product in products:

        uml = procedure.format(name="gcp_" + product["name"], stereo=product["name"], sprite="gcp_" + product["name"])
        fp.write(uml)
        fp.write("\n")
    