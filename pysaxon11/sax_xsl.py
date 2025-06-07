def sax_xsl(xml_in, xsl_in, xml_out) :
    from pysaxon11 import transform, file_path
    transform(xml_in, xsl_in, xml_out)
    
#sax_xsl("OpenAIRE_ExplorePage.mm","XML/mm2doc.xsl","prueba_sax.xml")
