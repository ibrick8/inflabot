from typing import Optional
from uuid import UUID

from domain.entidades.PosteoEntity import PosteoEntity
from infraestructure.db.models import PosteoModel, MetricaModel


class PostgresRepository:
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
            tipo=metrica.tipo,
        )

    def actualizar_post_url(self, posteo_id: UUID, post_url: str) -> None:
        posteo = self.session.query(PosteoModel).filter_by(id=posteo_id).first()
        if not posteo:
            raise ValueError(f"Posteo con id {posteo_id} no encontrado")
        posteo.post_url = post_url
        self.session.commit()
