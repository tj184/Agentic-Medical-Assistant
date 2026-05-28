from app.services.rag_service import (
    RAGService
)


def test_rag_pipeline():

    rag = RAGService()

    result = rag.retrieve_medical_context(
        "Symptoms of pneumonia"
    )

    assert result["success"] is True