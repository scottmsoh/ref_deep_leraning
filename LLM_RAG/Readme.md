
## LLM_RAG
Langchian:</br>
https://python.langchain.com/v0.1/docs/modules/data_connection/</br>

Many LLM applications require user-specific data that is not part of the model's training set.</br> 
The primary way of accomplishing this is through Retrieval Augmented Generation (RAG).</br>
In this process, external data is retrieved and then passed to the LLM when doing the generation step.</br>

** Steps (with Langchain)

1. Documents loading
- Library: Document Loader
  1) WebBaseLoader
  2) CSVLoader
  3) DirectoryLoader
  4) HTMLLoader
  5) JSONLoader
  6) MarkdownLoader
  7) PDFLoader

2. Spliting
- Library: Document Transformers
  1) RecursiveCharacterTextSpliter
  2) HTMLHeaderTextSplitter
  3) CodeTextSplitter
  4) MarkdownHeaderTextSplitter
 
3. Embedding
- 
   
4. Storage (Vector store)
- Vector DBs: Pinecone, Faiss, Chroma

5. Query processing


6. Similarity Search

  
4. Context Retrieval
- Library:

  
5. Outputs (Generation)
- Library:


<img width="815" alt="image" src="https://github.com/user-attachments/assets/2d14beea-b960-445c-aaf4-bf94f20cd9ff">
