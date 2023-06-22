import pybis as pb
import argparse as ap

ap = ap.ArgumentParser()
ap.add_argument("host", help="OpenBIS host")
args = ap.parse_args()

o = pb.Openbis(args.host, verify_certificates=False)

o.login("admin", "changeit")

# Create a new object
e1 = o.new_object(type="ENTRY", space="DEFAULT", project="/DEFAULT/DEFAULT")
e1.save()
e2 = o.new_object(type="ENTRY", space="DEFAULT", project="/DEFAULT/DEFAULT")
e2.set_children([e1])
e2.save()
print(e2)

e2.del_children([e1])