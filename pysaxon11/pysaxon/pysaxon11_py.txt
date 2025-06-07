#pysaxon11/pysaxon11.py
import os
import subprocess
import sys
import streamlit as st

def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

#def transform(xml_file, xsl_file, output_file, sx_params): ADVANCED.
def transform(xml_file, xsl_file, output_file, calling_path):
    XML_FILE     = str(xml_file)
    XSL_FILE     = str(xsl_file)
    OUTPUT_FILE  = str(output_file)
    CALLING_PATH = str(calling_path)
    st.write("**transform**")
    st.write(f"{XML_FILE=} {XSL_FILE=} {OUTPUT_FILE=} {CALLING_PATH=}" )
    """all args take relative paths from Python script"""
    XML_FILE_IN  = CALLING_PATH + XML_FILE
    input        = XML_FILE_IN
    XML_OUT      = CALLING_PATH + OUTPUT_FILE
    output       = XML_OUT
    XSL_IN       = CALLING_PATH + XSL_FILE
    xslt         = XSL_IN
    st.write(f"{calling_path}")

#    runcomm = "java net.sf.saxon.Transform -s:" + input + " -xsl:" + xslt + " -o:" + output + " " + sx_params # ADVANCED
    runcomm = "java net.sf.saxon.Transform -s:" + input + " -xsl:" + xslt + " -o:" + output
    st.write(f"{runcomm=}")
    subprocess.run(runcomm, shell=True, check=True)

def sax_xsl(xml_in, xsl_in, xml_out) :
    XML_IN   = str(xml_in)
    XSL_IN   = str(xsl_in)
    XML_OUT  = str(output_in)
    st.write(f"{XML_IN=} {XSL_IN=} {XML_OUT=}" )
    from pysaxon11 import transform, file_path
    transform(xml_in, xsl_in, xml_out)
#    input = xml_file
#    output = output_file
#    xslt = xsl_file
#
#    subprocess.call(f"java -cp C:saxonsaxon9he.jar net.sf.saxon.Transform -t -s:{input} -xsl:{xslt} -o:{output}")
#    CLASSPATH=/var/www/html/saxon/*::/var/www/html/stanford-corenlp/*
#    print(input)
#    print(xslt)
#    print(output)
#    subprocess.call(f"java net.sf.saxon.Transform -cp /var/www/html/saxon/* -t -s:{input} -xsl:{xslt} -o:{output}")
    # java net.sf.saxon.Transform -s:source -xsl:stylesheet -o:output
    # https://www.saxonica.com/documentation9.5/using-xsl/commandline.html
    #subprocess.run(f"touch 'output1.xml'", shell=True, check=True)
#    subprocess.run(f"java net.sf.saxon.Transform -s:{input} -xsl:{xslt} -o:{output}", shell=True, check=True)
    #java net.sf.saxon.Transform -t -s:{input} -xsl:{xslt} -o:{output}
    runcomm = "java net.sf.saxon.Transform -s:" + input + " -xsl:" + xslt + " -o:" + output
    st.write(f"{runcomm=}")
    subprocess.run(runcomm, shell=True, check=True)
