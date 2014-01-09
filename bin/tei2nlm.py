#!/usr/bin/env python
#@Author Dulip Withanage
import globals as gv
import subprocess
import shutil


class TEI2NLM:
    def __init__(self, gv):
        self.gv = gv

    def saxon_tei2nlm(self):
            cmd = ["java", "-classpath", self.gv.java_class_path,
                   "-Dxml.catalog.files=" + self.gv.runtime_catalog_path,
                   "net.sf.saxon.Transform",
                   "-x", "org.apache.xml.resolver.tools.ResolvingXMLReader",
                   "-y", "org.apache.xml.resolver.tools.ResolvingXMLReader",
                   "-r", "org.apache.xml.resolver.tools.CatalogResolver",
                   "-o", self.gv.nlm_temp_file_path,
                   self.gv.tei_file_path,
                   self.gv.nlm_style_sheet_dir,
                   'autoBlockQuote=true'
                   ]
            return ' '.join(cmd)

    def run(self):
        #assumes ouput path exists after tei conversion
        self.gv.mk_dir(self.gv.nlm_folder_path)
        java_command = self.saxon_tei2nlm()
        print "INFO: Running saxon transform (TEI->NLM)"
        subprocess.call(java_command, stdin=None, shell=True)
        shutil.copy2(self.gv.nlm_temp_file_path, self.gv.nlm_file_path)
