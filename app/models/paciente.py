from app import db

class Paciente(db.Model):

    __tablename__ = 'paciente'

    id_paciente = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    edad = db.Column(db.Integer)

    direccion = db.Column(db.String(200))

    telefono = db.Column(db.String(20))

    consultas = db.relationship('Consulta', backref='paciente', lazy=True)