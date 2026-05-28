from loguru import logger


class DrugChecker:

    def __init__(self):

        # Sample interaction database
        self.interactions = {
            ("paracetamol", "ibuprofen"):
                "Generally safe when used correctly.",
            
            ("aspirin", "warfarin"):
                "High bleeding risk detected.",

            ("metformin", "alcohol"):
                "Risk of lactic acidosis."
        }

    def check_interactions(self, medicines: list):

        try:
            warnings = []

            lower_meds = [med.lower() for med in medicines]

            for i in range(len(lower_meds)):
                for j in range(i + 1, len(lower_meds)):

                    pair = (
                        lower_meds[i],
                        lower_meds[j]
                    )

                    reverse_pair = (
                        lower_meds[j],
                        lower_meds[i]
                    )

                    if pair in self.interactions:
                        warnings.append({
                            "drugs": pair,
                            "warning": self.interactions[pair]
                        })

                    elif reverse_pair in self.interactions:
                        warnings.append({
                            "drugs": reverse_pair,
                            "warning": self.interactions[reverse_pair]
                        })

            logger.info("Drug interaction check completed")

            return {
                "success": True,
                "warnings": warnings
            }

        except Exception as e:

            logger.error(f"Drug Checker Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }