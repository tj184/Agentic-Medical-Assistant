from loguru import logger


class PatientMemory:

    def __init__(self):

        self.patient_records = {}

    def create_patient_profile(
        self,
        patient_id: str,
        name: str,
        age: int,
        gender: str
    ):

        try:
            self.patient_records[patient_id] = {
                "name": name,
                "age": age,
                "gender": gender,
                "medical_history": [],
                "allergies": [],
                "medications": [],
                "diagnoses": []
            }

            logger.info(
                f"Patient profile created: {patient_id}"
            )

            return {
                "success": True,
                "message": "Patient profile created"
            }

        except Exception as e:

            logger.error(f"Patient Profile Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def add_medical_history(
        self,
        patient_id: str,
        history: str
    ):

        try:
            self.patient_records[patient_id][
                "medical_history"
            ].append(history)

            logger.info(
                f"Medical history added for {patient_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Medical History Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def add_allergy(
        self,
        patient_id: str,
        allergy: str
    ):

        try:
            self.patient_records[patient_id][
                "allergies"
            ].append(allergy)

            logger.info(
                f"Allergy added for {patient_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Allergy Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def add_medication(
        self,
        patient_id: str,
        medication: str
    ):

        try:
            self.patient_records[patient_id][
                "medications"
            ].append(medication)

            logger.info(
                f"Medication added for {patient_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Medication Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def add_diagnosis(
        self,
        patient_id: str,
        diagnosis: str
    ):

        try:
            self.patient_records[patient_id][
                "diagnoses"
            ].append(diagnosis)

            logger.info(
                f"Diagnosis added for {patient_id}"
            )

            return {
                "success": True
            }

        except Exception as e:

            logger.error(f"Diagnosis Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }

    def get_patient_profile(self, patient_id: str):

        try:
            profile = self.patient_records.get(patient_id)

            if not profile:

                return {
                    "success": False,
                    "message": "Patient not found"
                }

            return {
                "success": True,
                "profile": profile
            }

        except Exception as e:

            logger.error(f"Get Patient Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }