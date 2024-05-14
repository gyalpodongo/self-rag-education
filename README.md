1. We'll need to set up a venv with llamaindex 
2. Create pipeline
   1. Data creation of questions in the right format as well as lecture content
   2. Do function to call chatgpt and see if retrieval is needed
      1. If needed, then get top k docs using llamaindex 
      2. For each of the k docs, call chatgpt using that doc as reference and produce an output g
      3. Determine if g is relevant and supports answer, generating two toher reflection tokens
      4. Calculat ea score using all tokens to detemrine which documents to use in final output
      5. Generate final outpu
   3. If no retrieval needed, just generate output