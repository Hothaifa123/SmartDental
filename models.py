from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from flask_login import UserMixin
Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    doctor_name = Column(String(300))
    doctor_phone = Column(String(50))
    doctor_specialty = Column(String(300))
    clinic_name = Column(String(300))
    clinic_address = Column(Text)
    logo_path = Column(Text)
    photo_path = Column(Text)
    watermark_path = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    patients = relationship('Patient', back_populates='doctor', cascade='all, delete-orphan')
    prescriptions = relationship('Prescription', back_populates='doctor', cascade='all, delete-orphan')

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)
    gender = Column(String(10))
    phone = Column(String(20))
    weight = Column(Integer)
    chronic_diseases = Column(Text)
    allergies = Column(Text)
    chronic_drugs = Column(Text)
    doctor_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    doctor = relationship('User', back_populates='patients')

class Drug(Base):
    __tablename__ = 'drugs'
    id = Column(Integer, primary_key=True)
    trade_name = Column(String(300))
    generic_name = Column(String(300))
    category = Column(String(100))
    admin_route = Column(String(50))
    adult_dose = Column(String(200))
    child_dose = Column(String(200))
    frequency = Column(String(200))
    duration = Column(String(200))
    notes = Column(Text)
    is_global = Column(Boolean, default=True)

class Prescription(Base):
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    diagnosis = Column(Text)
    items_json = Column(Text)
    is_ready = Column(Boolean, default=False)
    ready_name = Column(String(300))
    is_global_template = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    patient = relationship('Patient')
    doctor = relationship('User', back_populates='prescriptions')

class EmergencyProtocol(Base):
    __tablename__ = 'emergency_protocols'
    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    symptoms = Column(Text)
    procedure = Column(Text)
    medications = Column(Text)

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    date = Column(String(20))
    time = Column(String(10))
    reason = Column(Text)
    patient = relationship('Patient')

class ClinicalImage(Base):
    __tablename__ = 'clinical_images'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    filename = Column(String(300))
    category = Column(String(100))
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    patient = relationship('Patient')

class CaseSheet(Base):
    __tablename__ = 'case_sheets'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    sheet_type = Column(String(100))
    data_json = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    patient = relationship('Patient')
