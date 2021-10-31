#tipo de documento ----> selectfield
#Numero de documento ----> string field
#Nombre de paciente ----->string field

#Se importa la clase para trabajar con los formularios.
from flask_wtf import FlaskForm
#importar los componenentes del formulario
from wtforms import StringField,SelectField,BooleanField,SubmitField,DateField,TextAreaField

# 1. Se crea el formulario
# 2. Se crea la ruta
# 3. Se crea el html 

class formulario_med_cp(FlaskForm):
    tipo_doc_pac =SelectField('Tipo de documento',choices={('Cédula de ciudadania'),('Tarjeta de identidad'),('Cédula de extranjeria'),('Registro civil'),('Cárne Diplomatico'),('Pasaporte'),('Permiso especial de permanencia'),('Salvoconducto de permanencia'),('Nit'),('Pasaporte de la ONU'),('Certificado Nacido vivo')})
    num_doc_pac = StringField('Número de documento')
    botonBuscar =SubmitField('Buscar',render_kw={'onmouseover':'consultar_pac()'})


class formulario_med_cc(FlaskForm):
    Id_Medico = StringField('Id del Medico')
    Num_Documento_P = StringField('Número de documento del paciente')
    botonBuscar2 =SubmitField('Buscar',render_kw={'onmouseover':'consultar_citas()'})


class formulario_med_comD(FlaskForm):
    Id_paciente = StringField('Id paciente')
    Id_Medico = StringField('Id Medico')
    Id_Comentarios = StringField('Id Comentario')
    Nombre_p = StringField('Nombre de paciente')
    Num_Documento_P = StringField('Numero de documento paciente')
    Nombre_M = StringField('Nombre de Medico')
    Fecha_C = DateField(' Fecha de la cita')
    Comentario = TextAreaField('Comentario')
    botonCrear = SubmitField('Guardar',render_kw={'onmouseover':'guardar_comentario()'})
    botonActualizar = SubmitField('Actualizar',render_kw={'onmouseover':'editar_comentario()'})
    botonEliminar = SubmitField('Eliminar',render_kw={'onmouseover':'eliminar_comentarios()'})
    botonListarTodos = SubmitField('Consultar',render_kw={'onmouseover':'consultar_comentarios()'})

class formulario_pac_cc(FlaskForm):
    Id_Citas = StringField('Id Citas')
    Id_Paciente= StringField('Id paciente')
    Id_Medico = StringField('Id Medico')
    Nombre_P= StringField('Nombre de paciente')
    Num_Documento_P = StringField('Numero de documento paciente')
    Nombre_M = StringField('Nombre de Medico')
    Fecha_C = DateField(' Fecha de la cita')
    Hora_C= SelectField('Hora de la cita',choices={('8:00-8:30'),('8:30-9:00'),('8:30-9:00'),('9:00-9:30'),('9:30-10:00'),('10:00-10:30'),('10:30-11:00'),('11:00-11:30'),('11:30-12:00'),('14:00-14:30'),('14:30 -15:00'),('15:00 -15:30'),('15:30 -14:00')})
    Calificacion_cit= SelectField('Calificiación de la cita',choices={('Sin calificar'),('1 Mala'),('2 regular'),('3 Buena'),('4 Sobresaliente'),('5 Excelente')})
    botonGuardar = SubmitField('Guardar',render_kw={'onmouseover':'Crearcitas_guardar()'})
    botonEliminar = SubmitField('Eliminar',render_kw={'onmouseover':'Crearcitas_eliminar()'})

class formulario_pac_conscitas(FlaskForm):
    tipo_doc_pac =SelectField('Tipo de documento',choices={('Cédula de ciudadania'),('Tarjeta de identidad'),('Cédula de extranjeria'),('Registro civil'),('Cárne Diplomatico'),('Pasaporte'),('Permiso especial de permanencia'),('Salvoconducto de permanencia'),('Nit'),('Pasaporte de la ONU'),('Certificado Nacido vivo')})
    num_doc_pac = StringField('Número de documento')
    botonBuscar =SubmitField('Buscar',render_kw={'onmouseover':'cons_citas_paciente()'})
    Id_Citas = StringField('Id Citas')
    Calificacion_cit= SelectField('Calificiación de la cita',choices={('Sin calificar'),('1 Mala'),('2 regular'),('3 Buena'),('4 Sobresaliente'),('5 Excelente')})
    botonCalificar =SubmitField('Calificar',render_kw={'onmouseover':'calif_citas_paciente()'})



class formulario_pac_rp(FlaskForm):
    Id_Paciente = StringField('Id_paciente')
    Rol_P = SelectField('Rol', choices=[('Paciente')])
    Estado_P = SelectField('Estado',choices=[('Activo'),('Inactivo')])
    Nombre_P = StringField('Nombre del paciente')
    Email_P = StringField('Email del paciente')
    Tipo_Documento_P = SelectField('Documento del paciente', choices=[('Cedula de ciudadania'),('Cedula de extranjeria'),('Pasaporte'),('Tarjeta de identidad')])
    Num_Documento_P = StringField('Numero de documento')
    Genero_P = SelectField('Genero del paciente',choices=[('Masculino'),('Femenino'),('No especifica')])
    EPS_Paciente_P = SelectField('Eps del paciente', choices=[('Coomeva'),('Sura'),('Nueva eps'),('Salud total'),('Medimas'),('Comparta'),('Famisanar'),('Sanitas'),('Capital salud')])
    Poliza_salud_P = StringField('Poliza del paciente')
    Tipo_afiliacion_P = SelectField('Tipo de afiliacion',choices=[('Contributivo'),('Subsidiado')])
    Estado_Civil_P = SelectField('Estado civil del paciente', choices=[('Soltero(a)'),('Casado(a)'),('No especifica')])
    Celular_P = StringField('Celular del paciente')
    Telefono_Fijo_P = StringField('Telefono del paciente')
    Dirección_P = StringField('Direccion')
    Fecha_nac = StringField('Fecha de nacimiento')
    boton_guardar = SubmitField('Guardar', render_kw={'onmouseover':'guardar_paciente()'})
    boton_editar = SubmitField('Editar',render_kw={'onmouseover':'editar_paciente()'})
    boton_eliminar = SubmitField('Eliminar',render_kw={'onmouseover':'eliminar_paciente()'})

class formulario_mec_rp(FlaskForm):
    Id_Medico = StringField('Id_medico')
    Rol_M = SelectField('Rol', choices=[('Medico')])
    Estado_M = SelectField('Estado', choices=[('Activo'), ('Inactivo')])
    Nombre_M = StringField('Nombre')
    Email_M = StringField('Email')
    Tipo_Documento_M = SelectField('Documento', choices=[('cedula de ciudadania'),('cedula de extranjeria'),('pasaporte'),('tarjeta de identidad')])
    Num_Documento_M = StringField('Numero De Documento')
    Genero_M = SelectField('Genero',choices=[('masculino'),('femenino'),('no especifica')])
    EPS_Paciente_M = SelectField('EPS', choices=[('coomeva'),('sura'),('nueva eps'),('salud total'),('medimas'),('comparta'),('famisanar'),('sanitas'),('capital salud')])
    Poliza_salud_M = StringField('Poliza')
    Tipo_afiliacion_M = SelectField('Regimen',choices=[('contributivo'),('subsidiado')])
    Estado_Civil_M = SelectField('Estado civil ', choices=[('soltero(a)'),('casado(a)'),('no especifica')])
    Celular_M = StringField('Celular')
    Telefono_Fijo_M = StringField('Telefono')
    Dirección_M = StringField('Direccion')
    Fecha_nacimiento_M = StringField('Dia de Nacimiento')
    Titulo_Universitario = StringField('Titulo Profesional')
    Universidad = StringField('Universidad')
    Matricula_profesional = StringField('Matricula')
    Cargo = StringField('Cargo')
    Especialidad_M = StringField('Especialidad')
    boton_guardar = SubmitField('Guardar', render_kw={'onmouseover':'guardar_medico()'})
    boton_editar = SubmitField('Editar',render_kw={'onmouseover':'editar_medico()'})
    boton_eliminar = SubmitField('Eliminar',render_kw={'onmouseover':'eliminar_medico()'})


class formulario_cons_pac(FlaskForm):
    boton_buscar3 = SubmitField('    Lista de pacientes Registrados    ', render_kw={'onmouseover':'Cons_Adm_paciente()'})

class formulario_cons_med(FlaskForm):
    boton_buscar4 = SubmitField('    Lista de medicos Registrados    ', render_kw={'onmouseover':'Cons_Adm_medico()'})