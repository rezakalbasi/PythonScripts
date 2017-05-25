import os
import tkinter
import rdflib
import rdflib.util
import openpyxl
from rdflib import Graph, URIRef, Literal
from tkinter import *
from rdflib import URIRef
from rdflib.namespace import RDF
from time import gmtime, strftime
import requests
import json
import pprint


print ("computations start at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None
'''


'''
Date: 03/05/2017
Author: Reza Kalbasi
Project: PhysioMed App Develeopment; University of Auckland; ABI
This code extracts a subtree of an ontology from a conecept (as a child/subclass) to its ancestors (Parents).

'''





cptFMA=[]
cptCHEBI=[]
cptGO=[]
cptOPB=[]
cptSNOMED=[]
cptLOINC=[]


wb = openpyxl.load_workbook('C:\\Users\\rkal762\\Google Drive\\Reza\\1.Literature\\PhysioMedApp development\\Ontologies\\cptTerms.xlsx')
sheet = wb.active
for i in range(sheet.max_row):
    if sheet['A%s'%(i+1)].value == 'fma':
        cptFMA.append(sheet['B%s'%(i+1)].value)
    elif  sheet['A%s'%(i+1)].value == 'chebi':
        cptCHEBI.append(sheet['B%s'%(i+1)].value)
    elif  sheet['A%s'%(i+1)].value == 'go':
            cptGO.append(sheet['B%s'%(i+1)].value)
    elif  sheet['A%s'%(i+1)].value == 'opb':
            cptOPB.append(sheet['B%s'%(i+1)].value)

# ***************************************FMA***************************************************************
###########################################################################################################
f = open('C:\\Users\\rkal762\\Desktop\\SubFMA.owl', 'w')
f.write("""<?xml version="1.0"?><rdf:RDF xmlns="http://purl.obolibrary.org/obo/fma.owl#"
     xml:base="http://purl.obolibrary.org/obo/fma.owl"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:obo="http://purl.obolibrary.org/obo/">
    <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/fma.owl">
        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/fma/releases/2017-03-18/fma.owl"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">this is an ALPHA version of the FMA2.0 in obo. Conversion based on http://www.bioontology.org/wiki/index.php/FMAInOwl</rdfs:comment>
        <oboInOwl:date rdf:datatype="http://www.w3.org/2001/XMLSchema#string">24:07:2008 15:29</oboInOwl:date>
        <oboInOwl:default-namespace rdf:datatype="http://www.w3.org/2001/XMLSchema#string">fma</oboInOwl:default-namespace>
        <oboInOwl:hasOBOFormatVersion rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.2</oboInOwl:hasOBOFormatVersion>
    </owl:Ontology>""")
f.write('\n')


url=[]


for i in range(len(cptFMA)):
    url.append('http://www.ebi.ac.uk/ols/api/ontologies/fma/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F'+cptFMA[i]+'/ancestors')
    #print(url[i])
    r = requests.get(url[i])


    js=[]
    label=[]

    for t in range(20):
                 js.append(r.json()['_embedded']['terms'][t]['iri'])
                 label.append(r.json()['_embedded']['terms'][t]['label'])
                 if (r.json()['_embedded']['terms'][t]['iri']=='http://www.w3.org/2002/07/owl#Thing'):
                     break
                                      
                 
    for j in range(len(js)-1):
                 f.write("<owl:Class rdf:about=\"%s\"/>" %js[j] )
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %(js[j+1]))
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %label[j])


f.write("</rdf:RDF>")
f.close()

print("FMA done at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


'''
# ***************************************OPB***************************************************************
###########################################################################################################
f = open('C:\\Users\\rkal762\\Desktop\\SubOPB.owl', 'w')
f.write("""<?xml version="1.0"?>
<!DOCTYPE rdf:RDF [
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY OPB "http://bhi.washington.edu/OPB#" >
    <!ENTITY dc "http://purl.org/dc/elements/1.1/" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
]>
<rdf:RDF xmlns="http://bhi.washington.edu/OPB#"
     xml:base="http://bhi.washington.edu/OPB"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:OPB="http://bhi.washington.edu/OPB#">
    <owl:Ontology rdf:about="http://bhi.washington.edu/OPB"/>""")
f.write('\n')


url=[]


for i in range(len(cptOPB)):
    url.append('http://www.ebi.ac.uk/ols/api/ontologies/opb/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F'+cptOPB[i]+'/ancestors')
    #print(url[i])
    r = requests.get(url[i])


    js=[]
    label=[]

    for t in range(20):
                 js.append(r.json()['_embedded']['terms'][t]['iri'])
                 label.append(r.json()['_embedded']['terms'][t]['label'])
                 if (r.json()['_embedded']['terms'][t]['iri']=='http://www.w3.org/2002/07/owl#Thing'):
                     break
                                      
                 
    for j in range(len(js)-1):
                 f.write("<owl:Class rdf:about=\"%s\"/>" %js[j] )
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %(js[j+1]))
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %label[j])


f.write("</rdf:RDF>")
f.close()

print("OPB done at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''


# ***************************************CHEBI***************************************************************
###########################################################################################################
f = open('C:\\Users\\rkal762\\Desktop\\SubCHEBI.owl', 'w')
f.write("""<?xml version="1.0"?>
<rdf:RDF xmlns="http://purl.obolibrary.org/obo/chebi.owl#"
     xml:base="http://purl.obolibrary.org/obo/chebi.owl"
     xmlns:chebi3="http://purl.obolibrary.org/obo/chebi#2"
     xmlns:chebi4="http://purl.obolibrary.org/obo/chebi#3"
     xmlns:obo="http://purl.obolibrary.org/obo/"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:chebi="http://purl.obolibrary.org/obo/chebi#"
     xmlns:chebi2="http://purl.obolibrary.org/obo/chebi#1"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#">
    <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/chebi.owl">
        <oboInOwl:date rdf:datatype="http://www.w3.org/2001/XMLSchema#string">01:03:2017 03:30</oboInOwl:date>
        <oboInOwl:hasOBOFormatVersion rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.2</oboInOwl:hasOBOFormatVersion>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Author: ChEBI curation team</rdfs:comment>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ChEBI Release version 149</rdfs:comment>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ChEBI subsumes and replaces the Chemical Ontology first</rdfs:comment>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">For any queries contact chebi-help@ebi.ac.uk</rdfs:comment>
        <oboInOwl:saved-by rdf:datatype="http://www.w3.org/2001/XMLSchema#string">chebi</oboInOwl:saved-by>
        <oboInOwl:default-namespace rdf:datatype="http://www.w3.org/2001/XMLSchema#string">chebi_ontology</oboInOwl:default-namespace>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">developed by Michael Ashburner &amp; Pankaj Jaiswal.</rdfs:comment>
        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/chebi/149/chebi.owl"/>
    </owl:Ontology>""")
f.write('\n')


url=[]


for i in range(len(cptCHEBI)):
    url.append('http://www.ebi.ac.uk/ols/api/ontologies/chebi/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F'+cptCHEBI[i]+'/ancestors')
    #print(url[i])
    r = requests.get(url[i])


    js=[]
    label=[]

    for t in range(20):
                 js.append(r.json()['_embedded']['terms'][t]['iri'])
                 label.append(r.json()['_embedded']['terms'][t]['label'])
                 if (r.json()['_embedded']['terms'][t]['iri']=='http://www.w3.org/2002/07/owl#Thing'):
                     break
                                      
                 
    for j in range(len(js)-1):
                 f.write("<owl:Class rdf:about=\"%s\"/>" %js[j] )
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %(js[j+1]))
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %label[j])


f.write("</rdf:RDF>")
f.close()

print("CHEBI done at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# ***************************************Gene Ontology***************************************************************
###########################################################################################################
f = open('C:\\Users\\rkal762\\Desktop\\SubGO.owl', 'w')
f.write("""<?xml version="1.0"?>
<rdf:RDF xmlns="http://purl.obolibrary.org/obo/go.owl#"
     xml:base="http://purl.obolibrary.org/obo/go.owl"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:oboInOwl="http://www.geneontology.org/formats/oboInOwl#"
     xmlns:terms="http://www.geneontology.org/formats/oboInOwl#http://purl.org/dc/terms/"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:go="http://purl.obolibrary.org/obo/go#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:obo="http://purl.obolibrary.org/obo/"
     xmlns:dc="http://purl.org/dc/elements/1.1/">
    <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/go.owl">
        <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/go/releases/2017-05-04/go.owl"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">cvs version: $Revision: 38972 $</rdfs:comment>
        <oboInOwl:default-namespace rdf:datatype="http://www.w3.org/2001/XMLSchema#string">gene_ontology</oboInOwl:default-namespace>
        <oboInOwl:hasOBOFormatVersion rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.2</oboInOwl:hasOBOFormatVersion>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Includes Ontology(OntologyID(OntologyIRI(&lt;http://purl.obolibrary.org/obo/go/never_in_taxon.owl&gt;))) [Axioms: 18 Logical Axioms: 0]</rdfs:comment>
    </owl:Ontology>""")
f.write('\n')


url=[]


for i in range(len(cptGO)):
    url.append('http://www.ebi.ac.uk/ols/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252F'+cptGO[i]+'/ancestors')
    #print(url[i])
    r = requests.get(url[i])


    js=[]
    label=[]

    for t in range(20):
                 js.append(r.json()['_embedded']['terms'][t]['iri'])
                 label.append(r.json()['_embedded']['terms'][t]['label'])
                 if (r.json()['_embedded']['terms'][t]['iri']=='http://www.w3.org/2002/07/owl#Thing'):
                     break
                                      
                 
    for j in range(len(js)-1):
                 f.write("<owl:Class rdf:about=\"%s\"/>" %js[j] )
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %(js[j+1]))
                 f.write("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %label[j])


f.write("</rdf:RDF>")
f.close()

print("GO done at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


