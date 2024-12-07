
Node Parser:
============

Node parser in Llamaindex is crucial component that process Raw Data to structured Node suitable for indexing and retrieval.

Documents in LlamaIndex:
========================


Document and node objects are core abstractions in llamaindex.

- they can be constructured manually or automatically by simple directory readers.
- by default, document stores text along with some attributes like metadata information.
- in LlamaIndex, a node is a basic unit of data that represents chunk of source document like text chunk,image or table etc.
- chunk consists of  2 components
     1) raw chunk contains portion  of original text from document
     2) 2 component is similar to documents they  contain metadata information like page no, filename , file path. etc
        and relation of this node to all other node.
        every node derive from a document will inherit same meta data information from that document.
        e.g file name field is propagated to every node.
 - 3 method to  create node from document.
           ![image](https://github.com/user-attachments/assets/a2f59d77-e459-426b-a3b8-d1787cc22d02)

   1) define node and all its attributes directly- manual rarely used
   2) parse source document in to nodes through node parser
   3) using an ingestion pipeline.
- once the data is ingested using data loaders next step, node parsers are responsible for chunking the
  raw data and transform to structure node and extract metadatainformation. these nodes are then
  indexed and made available for retrieval in a search or query parsers.
- Node parsers make sure when an document is broken in to nodes all of its attributes are inherited to
  children nodes, metadata text and metadata templates etc.
- Node parsers break down data into manageable pieces(nodes) based on specific rules or formats such as text,JSON or csv.
![image](https://github.com/user-attachments/assets/6b701b06-c18d-4e79-bcf8-03d4d1f93192)


commonly used Node parsers in LLamaindex:
==========================================

![image](https://github.com/user-attachments/assets/157a584d-7d6d-409b-aabf-efd36f3cda3b)

![image](https://github.com/user-attachments/assets/c60992c3-3a02-4e93-a95f-9261836df347)


      
Optionally we can have ingestion pipeline:
===========================================

ingestion pipeline takes the document and parsers to sentence spliter(node parser)

all nodes embeeddings in to vector db.

![image](https://github.com/user-attachments/assets/e1246b57-74cb-4d90-9d38-824758168315)
![image](https://github.com/user-attachments/assets/f23b5e23-53c4-432b-9860-7b9ca92a0021)

        
        
 
        
