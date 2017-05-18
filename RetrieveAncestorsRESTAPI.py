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

'''
def close_window():
    global entry
    entry = E.get()
    root.destroy()

root = Tk()
root.resizable(width=False, height=False)
L1 = Label(root, text="Enter Ontological term URI")
L1.pack()
E = Entry(root,font="Calibri 12",justify="center", width=100, bg="#1E6FBA",fg="yellow",disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=0)
E.pack(anchor = CENTER)
B = Button(root, text = "OK", command = close_window)
B.pack(anchor = S)
root.mainloop()
'''



cptFMA=[]
cptCHEBI=[]
cptGO=[]
cptOPB=[]
cptSNOMED=[]
cptLOINC=[]


wb = openpyxl.load_workbook('C:\\Users\\rkal762\\Desktop\\cptTerms.xlsx')
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

'''
    
    for j in range(5):    
        js = r.json()['_embedded']['terms'][j]['iri']
        print(js)
'''

print("""<?xml version="1.0"?><rdf:RDF xmlns="http://purl.obolibrary.org/obo/fma.owl#"
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
                 print("<owl:Class rdf:about=\"%s\"/>" %js[j] )
                 print("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %(js[j+1]))
                 print("<owl:Class rdf:about=\"%s\">" %js[j] +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %label[j])


print("</rdf:RDF>")




'''

for i in range(len(cptFMA)):
            #print (cptFMA[i])
            # termm = URIRef("http://identifiers.org/fma/FMA:84669#RezaSub")
            #   "http://www.w3.org/TR/2003/PR-owl-guide-20031209/wine#WineBodyFrenchParis""
            termCore = URIRef(cptFMA[i])
            termm = URIRef(cptFMA[i])
            namess=[]


            for s,p,o in g.triples((termm, rdflib.RDFS.subClassOf, None)):
                        if o.startswith("http")>0:     
                            namess.append(o)
                            f.write("<owl:Class rdf:about=\"%s\"/>" %s )
                            f.write("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %o)
                            


# ***************************************FMA***************************************************************
###########################################################################################################
g = rdflib.Graph()
result = g.parse("C:\\Users\\rkal762\\Google Drive\\Reza\\1.Literature\\PhysioMedApp development\\Ontologies\\fma.owl")

f = open('C:\\Users\\rkal762\\Desktop\\SubFMA.owl', 'w')
f.write("""<?xml version="1.0"?>
<rdf:RDF xmlns="http://purl.obolibrary.org/obo/fma.owl#"
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


for i in range(len(cptFMA)):
            #print (cptFMA[i])
            # termm = URIRef("http://identifiers.org/fma/FMA:84669#RezaSub")
            #   "http://www.w3.org/TR/2003/PR-owl-guide-20031209/wine#WineBodyFrenchParis""
            termCore = URIRef(cptFMA[i])
            termm = URIRef(cptFMA[i])
            namess=[]


            for s,p,o in g.triples((termm, rdflib.RDFS.subClassOf, None)):
                        if o.startswith("http")>0:     
                            namess.append(o)
                            f.write("<owl:Class rdf:about=\"%s\"/>" %s )
                            f.write("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %o)
                            

            count = 0
            while (count<len(namess)):        
             for i in range(len(namess)):
                    termm=namess[i]
                    for s,p,o in g.triples((namess[i], rdflib.RDFS.subClassOf, None)):
                                    namess.append(o)
                                    f.write("<owl:Class rdf:about=\"%s\"/>" %s )
                                    f.write("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %o)
                                    #print("%s count" %count)
                    count=count+1
            myset=set(namess)
            namess=list(myset)

            for i in range(len(namess)):
                    termm=namess[i]
                    for s,p,o in g.triples((namess[i], rdflib.RDFS.label, None)):
                            f.write("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %o)
            for s,p,o in g.triples((termCore, rdflib.RDFS.label, None)):
                            f.write("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %o)

f.write("</rdf:RDF>")
f.close()

print("FMA done at:")
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''
