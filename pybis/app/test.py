import pybis as pb
import argparse as ap
import requests as rq
import base64 as b64
import json
import re
import tempfile
import pathlib as pl

ap = ap.ArgumentParser()
ap.add_argument("host", help="OpenBIS host")
args = ap.parse_args()

o = pb.Openbis(args.host, verify_certificates=False)

o.login("admin", "changeit")







# # Create a new object


e1 = o.new_object(type="ENTRY", space="DEFAULT", project="/DEFAULT/DEFAULT", experiment="/DEFAULT/DEFAULT/DEFAULT")
e1.save()

out_file = pl.Path("./requirements.txt")
with open(out_file, mode="w+") as tf:
    tf.writelines("asdasdas")

#Create a new dataset
ds_new = o.new_dataset(
    type       = 'ANALYZED_DATA',
    experiment = '/DEFAULT/DEFAULT/DEFAULT',
    sample     = e1.identifier,
    files      = ["requirements.txt"],
    props      = {'$name': 'some good name'}
)
ds_new.save()