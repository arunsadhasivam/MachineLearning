
<p>
  <details><summary> 1. Relation Based Node Parsers</summary>


Relation -Based Node parser
=============================

it is most important parser.

if we are chunking the book, we want the hierarchial structures to be maintained. 
like chapters.

![image](https://github.com/user-attachments/assets/94584c7c-4e24-49d9-8958-d7cff8cf252a)

 ![image](https://github.com/user-attachments/assets/0b5f0ae4-13f2-4b71-87f4-4a62e6725a82)


</details> 
</p>



<p>
  <details><summary> 2.NodeParser Vs Text parser</summary>

1)Text Splitter
===============

- Text Splitters such as SentenceSplitters can divide long flat texts into nodes, based on certain rules or
  limitations, such as **chunk_size or chunk_overlap**.The nodes could represent lines, paragraphs or sentences
  and may also include additional metadata or links the original document.
  
2)Node Parsers
================

- Node parsers are more sophisticated can involve additonal data processing logic. Beyond **simply divide
  text in to nodes**, they can perform extra tasks such as **analyzing the structure of the  HTML** or json
  files and producing **nodes enriched with contextual information**.



    
![image](https://github.com/user-attachments/assets/25b4e5ed-fd64-4cee-ad22-1575c26abeef)
</details> 
</p>
