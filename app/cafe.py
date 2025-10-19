import datetime

from app.errors import (NotVaccinatedError, OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("No vaccine found")
        if not visitor["vaccine"]["expiration_date"]:
            raise NotVaccinatedError("No expiration date found for vaccine")
        vac_date = visitor["vaccine"]["expiration_date"]
        today = datetime.date.today()
        if vac_date < today:
            raise OutdatedVaccineError("Outdated vaccine found")
        value = visitor.get("wearing_a_mask")
        if value is not True or (not isinstance(value, bool)):
            raise NotWearingMaskError("No mask found")
        return f"Welcome to {self.name}"
