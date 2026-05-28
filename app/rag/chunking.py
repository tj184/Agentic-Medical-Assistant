from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def chunk_documents(
    documents,
    chunk_size=500,
    chunk_overlap=100
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []

    for doc in documents:

        text_chunks = splitter.split_text(
            doc["content"]
        )

        for chunk in text_chunks:

            chunks.append({
                "source": doc["source"],
                "content": chunk
            })

    return chunks