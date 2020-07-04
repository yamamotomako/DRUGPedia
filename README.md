# DRUGPedia

This is the web tool that shows the kind of drugs not called by wfg system.<br>
Wfg is the famous thrid parties AI medical system, but it targets only to international molecullar targeting drug.<br>
It's not good at calling other drugs such as domestical OTC ..etc , so it need to be customized to apply to the real hospital system.<br>

The usages are.. <br>
users upload the .vcf .dge .excel(results of mutations listed at the specific format given from GENOMON) files saved in the computers from this interfase and click the "GO" bottom, then the related drugs that were displayed.<br>
The internal file drug_list.txt was created by docters actually.<br>
The system firstly read the uploaded .vcf or .dge files, converted ids into other ids (or ids into names), then converted id/names were subject to search within 'my' drug databases and finally the clinical trials data are shown.
