import subprocess
import json

procedure = """
!unquoted procedure {name}($alias,$desc=\" \")
rectangle $alias <<{stereo}>> as \"<${sprite}>
$desc\"
endprocedure
"""
with open("gcp_products.json", "r") as fp:
    products = json.load(fp)


with open("gcp.iuml","w") as fp:
    for product in products:
        print(product["name"]) 

        image_path = f"icons/medium/{product['name']}.png"
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
        uml = procedure.format(name="gcp_" + product["name"], stereo=product["name"], sprite="gcp_" + product["name"])
        fp.write(uml)
        fp.write("\n")
    