from datetime import date
from collections import defaultdict
from typing import Optional
from uuid import UUID
from sqlalchemy import text
from domain.entidades.PosteoEntity import PosteoEntity
from infraestructure.db.models import PosteoModel, MetricaModel

class PostgresRepository():

    def __init__(self, session):
        self.session = session

    def obtener_posteo(self, posteo_id: UUID) -> Optional[PosteoEntity]:
        result = (
            self.session.query(PosteoModel, MetricaModel)
            .join(MetricaModel, PosteoModel.metrica_id == MetricaModel.id)
            .filter(PosteoModel.id == posteo_id)
            .first()
        )

        if result is None:
            return None

        posteo, metrica = result

        return PosteoEntity(
            id=posteo.id,
            fecha=metrica.fecha,
            cuerpo=posteo.cuerpo,
            tipo=metrica.tipo
        )