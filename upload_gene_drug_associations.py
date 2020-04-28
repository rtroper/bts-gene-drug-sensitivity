
import biothings, config
biothings.config_for_app(config)

import biothings.hub.dataload.uploader

from .parser import load_gene_drug_associations


class GeneDrugAssociationsLoader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source = 'gene_drug_sensitivity'
    name = 'gene_drug_associations'
    __metadata__ = {'src_meta': {}}
    idconverter = None
    storage_class = biothings.hub.dataload.uploader.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s" % data_folder)
        return load_gene_drug_associations(data_folder)

    @classmethod
    def get_mapping(cls):
        return {
            'gene_drug_associations': {
                'properties': {
                    'gene': {
                        'type': 'text'
                    },
                    'drug_id': {
                        'type': 'integer'
                    },
                    'p_value': {
                        'type': 'float'
                    },
                    'se': {
                        'type': 'float'
                    },
                    'fdr': {
                        'type': 'float'
                    },
                    '-logp': {
                        'type': 'float'
                    }
                }
            }
        }
