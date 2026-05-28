from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database.postgres import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    age = Column(Integer)

    gender = Column(String)

    allergies = Column(Text)

    medical_history = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    sessions = relationship(
        "Session",
        back_populates="patient"
    )

    prescriptions = relationship(
        "Prescription",
        back_populates="patient"
    )


class Session(Base):

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    conversation = Column(Text)

    diagnosis = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    patient = relationship(
        "Patient",
        back_populates="sessions"
    )


class Prescription(Base):

    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    medicine = Column(String)

    dosage = Column(String)

    warnings = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    patient = relationship(
        "Patient",
        back_populates="prescriptions"
    )