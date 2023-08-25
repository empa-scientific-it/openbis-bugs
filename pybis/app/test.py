import pybis as pb
import argparse as ap
import requests as rq
import base64 as b64
ap = ap.ArgumentParser()
ap.add_argument("host", help="OpenBIS host")
args = ap.parse_args()

o = pb.Openbis(args.host, verify_certificates=False)

o.login("admin", "changeit")


#Download a file
r = rq.get("https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg", verify=False)
r.raise_for_status()

img = b64.b64encode(r.content).decode('utf-8')
# Create a new object
e1 = o.new_object(type="ENTRY", space="DEFAULT", project="/DEFAULT/DEFAULT", experiment="/DEFAULT/DEFAULT/DEFAULT", 
                  props={"$document":f"""<?xml version="1.0" encoding="UTF-8"?><html><head></head><body><img src="data:image/jpg;base64, ${img}"/></body></html></xml>"""})
e1.save()
