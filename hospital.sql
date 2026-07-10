--------------------------------------------------
-- Base de datos: Sistema de Gestión Hospitalaria
--------------------------------------------------

CREATE TABLE IF NOT EXISTS doctores (

    id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,

    nombre TEXT NOT NULL,

    especialidad TEXT NOT NULL

);

CREATE TABLE IF NOT EXISTS pacientes (

    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,

    nombre TEXT NOT NULL,

    sintomas TEXT NOT NULL

);

CREATE TABLE IF NOT EXISTS citas (

    id_cita INTEGER PRIMARY KEY AUTOINCREMENT,

    id_doctor INTEGER NOT NULL,

    id_paciente INTEGER NOT NULL,

    fecha TEXT NOT NULL,

    hora TEXT NOT NULL,

    FOREIGN KEY (id_doctor)
        REFERENCES doctores(id_doctor),

    FOREIGN KEY (id_paciente)
        REFERENCES pacientes(id_paciente)

);