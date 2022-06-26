from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    birth_date: str
    weight: int
    height: int
    sex: str
    uuid: str


@dataclass
class Doctor:
    name: str
    category: str
    position: str
    uuid: str


@dataclass
class Diagnosis:
    doctor: Doctor
    patient: Patient
    description: str
    treatment: str
