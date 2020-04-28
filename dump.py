import os

import biothings, config
biothings.config_for_app(config)
#from config import DATA_ARCHIVE_ROOT

from biothings.utils.common import uncompressall

import biothings.hub.dataload.dumper

# Hard-code data archive root
data_archive_root = './gene_drug_associations'


class GeneDrugAssociationsDumper(biothings.hub.dataload.dumper.LastModifiedBaseDumper):

    SRC_NAME = 'gene_drug_associations'
    #SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    SRC_ROOT_FOLDER = os.path.join(data_archive_root, SRC_NAME)
    SCHEDULE = None
    UNCOMPRESS = False

    __metadata__ = {'src_meta': {}}

    def post_dump(self, *args, **kwargs):
        if self.__class__.UNCOMPRESS:
            self.logger.info("Uncompress all archive files in '%s" %
                             self.new_data_folder)
            uncompressall(self.new_data_folder)
