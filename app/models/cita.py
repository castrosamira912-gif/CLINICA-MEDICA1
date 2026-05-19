from app import db

class Cita(db.Model):

    id_cita = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha = db.Column(
        db.String(50),
        nullable=False
    )

    hora = db.Column(
        db.String(20),
        nullable=False
    )

    motivo = db.Column(
        db.String(200),
        nullable=False
    )

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medico.id_medico')
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('paciente.id_paciente')
    )

    medico = db.relationship('Medico')

    paciente = db.relationship('Paciente')