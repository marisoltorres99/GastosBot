from datetime import date
from utils.datetime_utils import now

from models import Vencimiento
from database import db
from services.telegram_service import enviarMensaje

def verificar_vencimientos(app):

    with app.app_context():

        hoy = now().date()

        vencimientos = Vencimiento.query.filter_by(Avisado=False).all()

        for v in vencimientos:

            dias_restantes = (v.FechaVencimiento - hoy).days

            if dias_restantes <= 1:

                enviarMensaje(
                    v.usuario.IdChat,
                    f"⏰ Recordatorio:\nTu vencimiento '{v.Nombre}' vence el {v.FechaVencimiento}"
                )

                v.Avisado = True

        db.session.commit()