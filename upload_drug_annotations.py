
import biothings, config
biothings.config_for_app(config)

import biothings.hub.dataload.uploader

from .parser import load_drug_annotations


class DrugAnnotationsLoader(biothings.hub.dataload.uploader.BaseSourceUploader):

    main_source = 'gene_drug_sensitivity'
    name = 'drug_annotations'
    __metadata__ = {'src_meta': {}}
    idconverter = None
    storage_class = biothings.hub.dataload.uploader.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return load_drug_annotations(data_folder)

    @classmethod
    def get_mapping(cls):
        return {
            'drug_annotations': {
                'properties': {
                    'drug_identifier': {
                        'type': 'integer',
                        'copy_to': [
                            'all'
                        ]
                    },
                    'drug_name': {
                        'type': 'text'
                    },
                    'target_pathway': {
                        'type': 'text'
                    }
                }
            }
        }
