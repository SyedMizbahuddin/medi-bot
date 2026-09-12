
# Project 
1. RBAC at retrieval
2. Docling Hierarichal
3. Hybrid RAG BM25
4. cross encoder
5. analytical to SQL RAG
6. FastAPI + Next.js 


# User role and access

1. Doctor - Clinical, drug, diagnostic + general
2. Nurse - Nurse, patient, general
3. billing - insurance, clain, billing faq, general
4. technicain - equipme....
5. admin - all

# Data source
general,
clinical,
nursing,
billing
equipment

db - (claims, maintenance - equipments)

{
    source_document,
    collection,
    access_roles,
    section_title,
    chunk_type
}

# Tech Req

1. Ingestion
  general stuff

2. Retrieval
  same

3. cross encoder

4. SQL RAG
olny billing_exec and admin

# FASTAPI

/login,
/collections/role 

 /chat 
 {
    answer
    sources
    retrieval_type
    role
 }

# Frontend



=====================================================

Chunking + ingestion
1. main in ingestion
ingest a file
 create chunks for that doc (with strategy here) -> 
      use docling -> return chunks
 generate embeddings for each chunk and store per file
 populate it to the DB

docling parse  + hybrid chunks
2. 