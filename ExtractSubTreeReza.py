import tkinter
import rdflib
import rdflib.util
from rdflib import Graph, URIRef, Literal
from tkinter import *
from rdflib import URIRef
from rdflib.namespace import RDF


'''
Date: 03/05/2017
Author: Reza Kalbasi
Project: PhysioMed App Develeopment; University of Auckland
This code extracts a subtree of an ontology from a conecept (as a child/subclass) to its ancestors (Parents).

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


g = rdflib.Graph()
result = g.parse("C:\\Users\\rkal762\\Google Drive\\Reza\\1.Literature\\PhysioMedApp development\\Ontologies\\fmaTest.owl")
 

# termm = URIRef("http://identifiers.org/fma/FMA:84669#RezaSub")
#   "http://www.w3.org/TR/2003/PR-owl-guide-20031209/wine#WineBodyFrenchParis""
termm = URIRef(entry)
namess=[]


print("""<?xml version="1.0"?>
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


for s,p,o in g.triples((termm, rdflib.RDFS.subClassOf, None)):
                namess.append(o)
                print("<owl:Class rdf:about=\"%s\"/>" %s )
                print("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %o)
                

count = 0
while (count<len(namess)):        
   for i in range(len(namess)):
        termm=namess[i]
        for s,p,o in g.triples((namess[i], rdflib.RDFS.subClassOf, None)):
                         namess.append(o)
                         print("<owl:Class rdf:about=\"%s\"/>" %s )
                         print("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:subClassOf rdf:resource=\"%s\"/></owl:Class> " %o)
                         #print("%s count" %count)
        count=count+1

for i in range(len(namess)):
        termm=namess[i]
        for s,p,o in g.triples((namess[i], rdflib.RDFS.label, None)):
                print("<owl:Class rdf:about=\"%s\">" %s +"<rdfs:label rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\"> %s </rdfs:label> </owl:Class> " %o)


print("</rdf:RDF>")














