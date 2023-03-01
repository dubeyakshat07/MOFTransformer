from mp_api.client import MPRester
from pymatgen.io.cif import CifWriter
from moftransformer.utils import prepare_data
import os
import json
import shutil
import glob

def query_mp(mp_id):
    print(os.getcwd())
    os.mkdir("new")
    
    with MPRester("4XZe4xvgqT4R4o4i0ZnTmct4xDklMq9d") as mpr:
      docs = mpr.summary.search(material_ids=[mp_id])
      cif_struct = CifWriter(docs[0].structure)
      cif_struct.write_file(f"new/{mp_id}.cif")
    dict_mp_id = dict()
    dict_mp_id[mp_id] = 0
    with open("new/raw_qpi.json","w") as file:
      json.dump(dict_mp_id, file)
      file.close()


def prep_data(root_dataset):
   root_cifs = "new"
   root_dataset = "prepared_data"
   test_fraction = 1
   val_fraction = 0
   train_fraction = 0
   downstream = "qpi"
   prepare_data(root_cifs, root_dataset,downstream = downstream, test_fraciton=test_fraction,
                train_fraction = train_fraction, val_fraction = val_fraction)
   shutil.rmtree("prepared_data/test")
   os.rename("prepared_data/total","prepared_data/test")
   os.remove("prepared_data/test_qpi.json")
   os.rename("prepared_data/val_qpi.json","prepared_data/test_qpi.json")


def remove_dir():
   shutil.rmtree("new")
   shutil.rmtree("prepared_data")