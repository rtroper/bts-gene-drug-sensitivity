import os, pandas, csv
import numpy as np
from biothings.utils.dataload import dict_convert, dict_sweep

import config
logging = config.logger

# Remove spaces in keys to make queries easier. Also, lowercase is preferred
# for a BioThings API. Define a helper function.
process_key = lambda k: k.replace(" ", "_").lower()


def load_gene_drug_associations(data_folder):
    infile = os.path.join(data_folder, 'mutation_drug_pairs.csv')
    assert os.path.exists(infile)
    dat = pandas.read_csv(infile, sep=',', squeeze=True, quoting=csv.QUOTE_NONE).to_dict(orient='records')
    results = {}
    for rec in dat:
        if not rec['Drug ID'] or pandas.isna(rec['Drug ID']):
            logging.warning('No drug information found in current record.')
            continue
        _id = rec['Drug ID']
        rec = dict_convert(rec, keyfn=process_key)
        # Remove NaN values, not indexable
        rec = dict_sweep(rec, vals=[np.nan])
        results.setdefault(_id, []).append(rec)
    for _id, docs in results.items():
        doc = {'_id': _id, 'gene_drug_associations': docs}
        yield doc


def load_drug_annotations(data_folder):
    infile = os.path.join(data_folder, 'GDSC_Drug_anno.csv')
    assert os.path.exists(infile)
    dat = pandas.read_csv(infile, sep=',', squeeze=True, quoting=csv.QUOTE_NONE).to_dict(orient='records')
    for rec in dat:
        drug_name = rec.pop('Drug_Name')
        drug_target_pathway = rec.pop('Drug_Targeted_process_or_pathway')
        drug_annotations = {
            'drug_name': drug_name,
            'target_pathway': drug_target_pathway
        }
        _id = rec['Drug_identifier']
        rec = dict_convert(rec, keyfn=process_key)
        doc = {'_id': _id, 'drug_annotations': drug_annotations}
        yield doc
