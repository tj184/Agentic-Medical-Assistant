from pathlib import Path

from pypdf import PdfReader

from app.rag.chunking import (
    chunk_documents
)

from app.rag.embeddings import (
    EmbeddingModel
)

from app.rag.vector_store import (
    VectorStore
)


DATA_PATH = "data/raw"

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".txt"
]


def load_documents():

    documents = []

    data_dir = Path(DATA_PATH)

    for file_path in data_dir.rglob("*"):

        if (
            file_path.suffix.lower()
            not in SUPPORTED_EXTENSIONS
        ):
            continue

        try:

            # -------------------------
            # PDF FILES
            # -------------------------

            if (
                file_path.suffix.lower()
                == ".pdf"
            ):

                reader = PdfReader(
                    str(file_path)
                )

                text = ""

                for page in reader.pages:

                    extracted = (
                        page.extract_text()
                    )

                    if extracted:

                        text += (
                            extracted + "\n"
                        )

            # -------------------------
            # TXT FILES
            # -------------------------

            else:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

            documents.append({
                "source": str(file_path),
                "content": text
            })

            print(
                f"Loaded: {file_path}"
            )

        except Exception as e:

            print(
                f"Failed loading "
                f"{file_path}: {e}"
            )

    return documents


def run_ingestion():

    print(
        "\nLoading documents...\n"
    )

    documents = load_documents()

    if not documents:

        print("No documents found!")

        return

    print(
        f"\nLoaded "
        f"{len(documents)} documents"
    )

    # -------------------------
    # CHUNKING
    # -------------------------

    print(
        "\nChunking documents...\n"
    )

    chunks = chunk_documents(
        documents
    )

    print(
        f"Generated "
        f"{len(chunks)} chunks"
    )

    # -------------------------
    # EMBEDDINGS
    # -------------------------

    print(
        "\nLoading embedding model...\n"
    )

    embedding_model = EmbeddingModel()

    print(
        "\nGenerating embeddings...\n"
    )

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = (
        embedding_model.embed_documents(
            texts
        )
    )

    # -------------------------
    # VECTOR STORE
    # -------------------------

    print(
        "\nStoring vectors...\n"
    )

    vector_store = VectorStore()

    vector_store.add_documents(
        chunks,
        embeddings
    )

    print(
        "\nIngestion completed "
        "successfully!"
    )


if __name__ == "__main__":

    run_ingestion()