from sqlalchemy import create_engine, Column, String, Date, ForeignKey, JSON, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.dialects.postgresql import UUID
from config import POSTGRESQL_URL

Base = declarative_base()

class MetricaModel(Base):
    __tablename__ = 'metricas'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    fecha = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)
    valores = Column(JSON, nullable=False)
    posteos = relationship("PosteoModel", back_populates="metrica")
    
class PosteoModel(Base):
    __tablename__ = "posteos"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    cuerpo = Column(JSON, nullable=False)
    metrica_id = Column(UUID(as_uuid=True), ForeignKey("metricas.id", ondelete="CASCADE"), nullable=False)
    metrica = relationship("MetricaModel", back_populates="posteos")

engine = create_engine(POSTGRESQL_URL)
Session = sessionmaker(bind=engine)
