from app.tools.symptom_parser import (
    SymptomParser
)

from app.tools.drug_checker import (
    DrugChecker
)


def test_symptom_parser():

    parser = SymptomParser()

    result = parser.extract_symptoms(
        "Patient has fever and cough"
    )

    assert "fever" in result["symptoms"]


def test_drug_checker():

    checker = DrugChecker()

    result = checker.check_interactions([
        "Aspirin",
        "Warfarin"
    ])

    assert len(result["warnings"]) > 0