from app import db

class Consulta(db.Model):

    __tablename__ = 'consulta'

    id_consulta = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.String(50), nullable=False)

    diagnostico = db.Column(db.String(300), nullable=False)

    tratamiento = db.Column(db.String(300), nullable=False)

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medico.id_medico'),
        nullable=False
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('paciente.id_paciente'),
        nullable=False
    )