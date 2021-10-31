import os
from flask.helpers import flash

from types import MethodType
from flask import Flask, render_template, url_for,request,flash, session, redirect
from markupsafe import escape 
import os
from db import *
from werkzeug.security import generate_password_hash, check_password_hash

from sqlite3.dbapi2 import Row
from flask_wtf import form
from wtforms.fields.core import StringField
from formulario import formulario_med_comD, formulario_med_cp,formulario_med_cc, formulario_med_comD, formulario_pac_cc, formulario_pac_conscitas, formulario_pac_rp,formulario_mec_rp,formulario_cons_pac,formulario_cons_med
import sqlite3


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('1login.html')


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        usu = request.form['txtusuario']
        passw = request.form['txtpassword']
        rol = request.form['rol']
        sql = f'SELECT * FROM User WHERE usuario = "{usu}"'
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute(sql)
        usuarios = cursorObj.fetchall()
        if len(usuarios)>0:
            contrasenaHas = usuarios[0][2]
            rol2 = usuarios[0][3]
            if (check_password_hash(contrasenaHas, passw) and (rol2=="Paciente")):
                session.clear()
                session['id'] = usuarios[0][0]
                session['user'] = usuarios[0][1]
                session['password'] = contrasenaHas
                return render_template('11interfazPacientes.html')

            elif (check_password_hash(contrasenaHas, passw) and (rol2=="Administrador")):
                session.clear()
                session['id'] = usuarios[0][0]
                session['user'] = usuarios[0][1]
                session['password'] = contrasenaHas
                return render_template('2interfazAdministrador.html')

            elif (check_password_hash(contrasenaHas, passw) and (rol2=='Médico')):
                session.clear()
                session['id'] = usuarios[0][0]
                session['user'] = usuarios[0][1]
                session['password'] = contrasenaHas
                return render_template('7interfazMedicos.html')
            
            else:
                flash(f'Usuario, clave o rol incorrecto')
                return render_template('1login.html')
        else:
            flash(f'El usuario ingresado no existe')
            return render_template('1login.html')

@app.route('/2interfazAdministrador')
def interfazAdministrador():
    return render_template('2interfazAdministrador.html')    
 
@app.route('/3registroDePacientes',methods = ['GET','POST'])
def registroDePacientes():
    form=formulario_pac_rp()
    return render_template('3registroDePacientes.html',form=form)

@app.route('/3registroDePacientes/guardar',methods = ['GET','POST'])
def guardar_pac():
    form = formulario_pac_rp()
    if request.method == 'POST':
        Id_Paciente=form.Id_Paciente.data
        Rol_P=form.Rol_P.data
        Estado_P=form.Estado_P.data
        Nombre_P=form.Nombre_P.data
        Email_P=form.Email_P.data
        Tipo_Documento_P=form.Tipo_Documento_P.data
        Num_Documento_P=form.Num_Documento_P.data
        Genero_P=form.Genero_P.data
        EPS_Paciente_P=form.EPS_Paciente_P.data
        Poliza_salud_P=form.Poliza_salud_P.data
        Tipo_afiliacion_P=form.Tipo_afiliacion_P.data
        Estado_civil_P=form.Estado_Civil_P.data
        Celular_P=form.Celular_P.data
        Telefono_Fijo_P=form.Telefono_Fijo_P.data
        Dirección_P=form.Dirección_P.data
        Fecha_nac=form.Fecha_nac.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            cur.execute('INSERT into Registro_Pacientes (Id_Paciente,Rol_P,Estado_P,Nombre_P,Email_P,Tipo_Documento_P,Num_Documento_P,Genero_P,EPS_Paciente_P,Poliza_salud_P,Tipo_afiliacion_P,Estado_civil_P,Celular_P,Telefono_Fijo_P,Dirección_P,Fecha_nac) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[Id_Paciente,Rol_P,Estado_P,Nombre_P,Email_P,Tipo_Documento_P,Num_Documento_P,Genero_P,EPS_Paciente_P,Poliza_salud_P,Tipo_afiliacion_P,Estado_civil_P,Celular_P,Telefono_Fijo_P,Dirección_P,Fecha_nac])
            conexion.commit()
            return('el paciente se ha guardado')
    return("ERROR - ERROR - ERROR") 

@app.route('/3registroDePacientes/editar',methods = ['GET','POST'])
def editar_pac():
    form = formulario_pac_rp()
    if request.method == 'POST':
        Id_Paciente=form.Id_Paciente.data
        Rol_P=form.Rol_P.data
        Estado_P=form.Estado_P.data
        Nombre_P=form.Nombre_P.data
        Email_P=form.Email_P.data
        Tipo_Documento_P=form.Tipo_Documento_P.data
        Num_Documento_P=form.Num_Documento_P.data
        Genero_P=form.Genero_P.data
        EPS_Paciente_P=form.EPS_Paciente_P.data
        Poliza_salud_P=form.Poliza_salud_P.data
        Tipo_afiliacion_P=form.Tipo_afiliacion_P.data
        Estado_civil_P=form.Estado_Civil_P.data
        Celular_P=form.Celular_P.data
        Telefono_Fijo_P=form.Telefono_Fijo_P.data
        Dirección_P=form.Dirección_P.data
        Fecha_nac=form.Fecha_nac.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            cur.execute('update Registro_Pacientes set  Rol_P=?, Estado_P=?, Nombre_P=?, Email_P=?, Tipo_Documento_P=?, Num_Documento_P=?, Genero_P=?, EPS_Paciente_P=?, Poliza_salud_P=?, Tipo_afiliacion_P=?, Estado_Civil_P=?, Celular_P=?, Telefono_Fijo_P=?, Dirección_P=?, Fecha_Nac=? where Id_Paciente=?',[Rol_P,Estado_P,Nombre_P,Email_P,Tipo_Documento_P,Num_Documento_P,Genero_P,EPS_Paciente_P,Poliza_salud_P,Tipo_afiliacion_P,Estado_civil_P,Celular_P,Telefono_Fijo_P,Dirección_P,Fecha_nac,Id_Paciente])
            conexion.commit()
            return(f'el paciente con Id {Id_Paciente} y nombre {Nombre_P} se ha editado correctamente')
    return("ERROR - ERROR - ERROR") 

@app.route('/3registroDePacientes/eliminar',methods = ['POST','GET'])
def eliminar_pac():
    form=formulario_pac_rp()
    if request.method=='POST':
        Id_Paciente=form.Id_Paciente.data
        Rol_P=form.Rol_P.data
        Estado_P=form.Estado_P.data
        Nombre_P=form.Nombre_P.data
        Email_P=form.Email_P.data
        Tipo_Documento_P=form.Tipo_Documento_P.data
        Num_Documento_P=form.Num_Documento_P.data
        Genero_P=form.Genero_P.data
        EPS_Paciente_P=form.EPS_Paciente_P.data
        Poliza_salud_P=form.Poliza_salud_P.data
        Tipo_afiliacion_P=form.Tipo_afiliacion_P.data
        Estado_civil_P=form.Estado_Civil_P.data
        Celular_P=form.Celular_P.data
        Telefono_Fijo_P=form.Telefono_Fijo_P.data
        Dirección_P=form.Dirección_P.data
        Fecha_nac=form.Fecha_nac.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur=conexion.cursor()
            cur.execute('delete from Registro_Pacientes where Id_paciente=?',[Id_Paciente])
            conexion.commit()
            if conexion.total_changes>0:
                return (f'el paciente con Id {Id_Paciente} y nombre {Nombre_P} se ha eliminado de la base de datos')
            return ('No se elimino el paciente')
    return ('Se presento un error')


@app.route('/4registroDeMedicos',methods = ['GET','POST'])
def registroDeMedicos():
    form=formulario_mec_rp()
    return render_template('4registroDeMedicos.html', form=form)


@app.route('/4registroDeMedicos/guardar',methods = ['GET','POST'])
def guardar_med():
    form = formulario_mec_rp()
    if request.method=='POST':
        Id_Medico = form.Id_Medico.data
        Rol_M = form.Rol_M.data
        Estado_M = form.Estado_M.data
        Nombre_M = form.Nombre_M.data
        Email_M = form.Email_M.data
        Tipo_Documento_M = form.Tipo_Documento_M.data
        Num_Documento_M = form.Num_Documento_M.data
        Genero_M = form.Genero_M.data
        EPS_Paciente_M = form.EPS_Paciente_M.data
        Poliza_salud_M = form.Poliza_salud_M.data
        Tipo_afiliacion_M = form.Tipo_afiliacion_M.data
        Estado_Civil_M = form.Estado_Civil_M.data
        Celular_M = form.Celular_M.data
        Telefono_Fijo_M = form.Telefono_Fijo_M.data
        Dirección_M = form.Dirección_M.data
        Fecha_nacimiento_M = form.Fecha_nacimiento_M.data
        Titulo_Universitario =form.Titulo_Universitario.data
        Universidad = form.Universidad.data
        Matricula_profesional = form.Matricula_profesional.data
        Cargo = form.Cargo.data
        Especialidad_M = form.Especialidad_M.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            cur.execute('insert into Registro_Medico (Id_medico,Rol_M,Estado_M,Nombre_M,Email_M,Tipo_Documento_M,Num_Documento_M,Genero_M,EPS_Paciente_M,Poliza_salud_M,Tipo_afiliacion_M,Estado_Civil_M,Celular_M,Telefono_Fijo_M,Dirección_M,Fecha_nacimiento_M,Titulo_Universitario,Universidad,Matricula_profesional,Cargo,Especialidad_M) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[Id_Medico,Rol_M,Estado_M,Nombre_M,Email_M,Tipo_Documento_M,Num_Documento_M,Genero_M,EPS_Paciente_M,Poliza_salud_M,Tipo_afiliacion_M,Estado_Civil_M,Celular_M,Telefono_Fijo_M,Dirección_M,Fecha_nacimiento_M,Titulo_Universitario,Universidad,Matricula_profesional,Cargo,Especialidad_M])
            conexion.commit()
            return('el medico se ha guardado')
    return("ERROR - ERROR - ERROR")    

@app.route('/4registroDeMedicos/editar', methods = ['GET','POST'])
def editar_med():
    form = formulario_mec_rp()
    if request.method == 'POST':
        Id_Medico = form.Id_Medico.data
        Rol_M = form.Rol_M.data
        Estado_M = form.Estado_M.data
        Nombre_M = form.Nombre_M.data
        Email_M = form.Email_M.data
        Tipo_Documento_M = form.Tipo_Documento_M.data
        Num_Documento_M = form.Num_Documento_M.data
        Genero_M = form.Genero_M.data
        EPS_Paciente_M = form.EPS_Paciente_M.data
        Poliza_salud_M = form.Poliza_salud_M.data
        Tipo_afiliacion_M = form.Tipo_afiliacion_M.data
        Estado_Civil_M = form.Estado_Civil_M.data
        Celular_M = form.Celular_M.data
        Telefono_Fijo_M = form.Telefono_Fijo_M.data
        Dirección_M = form.Dirección_M.data
        Fecha_nacimiento_M = form.Fecha_nacimiento_M.data
        Titulo_Universitario =form.Titulo_Universitario.data
        Universidad = form.Universidad.data
        Matricula_profesional = form.Matricula_profesional.data
        Cargo = form.Cargo.data
        Especialidad_M = form.Especialidad_M.data

        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            #colocar todas las variables
            cur.execute('update Registro_Medico set Rol_M=?, Estado_M=?,Nombre_M=?,Email_M=?,Tipo_Documento_M=?,Num_Documento_M=?,Genero_M=?,EPS_Paciente_M=?,Poliza_salud_M=?,Tipo_afiliacion_M=?,Estado_Civil_M=?,Celular_M=?,Telefono_Fijo_M=?,Dirección_M=?,Fecha_nacimiento_M=?,Titulo_Universitario=?,Universidad=?,Matricula_profesional=?,Cargo=?,Especialidad_M=? where Id_Medico=?',[Rol_M,Estado_M,Nombre_M,Email_M,Tipo_Documento_M,Num_Documento_M,Genero_M,EPS_Paciente_M,Poliza_salud_M,Tipo_afiliacion_M,Estado_Civil_M,Celular_M,Telefono_Fijo_M,Dirección_M,Fecha_nacimiento_M,Titulo_Universitario,Universidad,Matricula_profesional,Cargo,Especialidad_M,Id_Medico])
            conexion.commit()
            return(f'el medico con Id {Id_Medico} y nombre {Nombre_M} se ha editado correctamente')
    return ("ERROR - ERROR - ERROR")

@app.route('/4registroDeMedicos/eliminar',methods = ['POST','GET'])
def eliminar_med():
    form=formulario_mec_rp()
    if request.method=='POST':
        Id_Medico = form.Id_Medico.data
        Nombre_M = form.Nombre_M.data

        with sqlite3.connect('DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur=conexion.cursor()
            cur.execute('delete from Registro_Medico where Id_Medico=?',[Id_Medico])
            conexion.commit()
            if conexion.total_changes>0:
                return (f'el paciente con Id {Id_Medico} y nombre {Nombre_M} se ha eliminado de la base de datos')
            return ('No se pudo eliminar el registro de este Medico')
    return ('Se presento un error')

@app.route('/5verRegistroDePacientes',methods = ['GET','POST'])
def verRegistroDePacientes():
    form=formulario_cons_pac()
    if request.method =='POST':

        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('select * from Registro_Pacientes')
            row =cur.fetchall()
            if row == None:
                return('No se registran pacientes')
            return render_template('5verRegistroDePacientes.html',row=row, form = form)
    return render_template('5verRegistroDePacientes.html',form = form)



@app.route('/6verRegistroDeMedicos',methods = ['GET','POST'])
def verRegistroDeMedicos():
    form=formulario_cons_med()
    if request.method =='POST':

        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('select * from Registro_Medico')
            row =cur.fetchall()
            if row == None:
                return('No se registran medicos')
            return render_template('6verRegistroDeMedicos.html',row=row, form = form)
    return render_template('6verRegistroDeMedicos.html',form = form)




@app.route('/7interfazMedicos')
def interfazMedicos():
    return render_template('7interfazMedicos.html')  

@app.route('/8consultaPacientes',methods = ['GET','POST'])
def CP_mostrarPacientes():
    form = formulario_med_cp()
    if request.method =='POST':
        tipo_doc_pac=form.tipo_doc_pac.data
        num_doc_pac=form.num_doc_pac.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('select * from Registro_Pacientes where Num_Documento_P=?',[num_doc_pac])
            row =cur.fetchone()
            if row == None:
                return('Paciente no encontrado')
            return render_template('8consultaPacientes.html',row=row, form = form)
    return render_template('8consultaPacientes.html',form = form)

@app.route('/9consultaCitas',methods = ['GET','POST'])
def consultaCitas():
    form =formulario_med_cc()
    if request.method =='POST':
        Id_Medico=form.Id_Medico.data
        Num_Documento_P=form.Num_Documento_P.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('select * from Citas_medicas where Num_Documento_P=? or Id_Medico=?',[Num_Documento_P,Id_Medico])
            row =cur.fetchall()
            if row == None:
                return('Paciente no encontrado')
            return render_template('9consultaCitas.html',row=row, form = form)
    return render_template('9consultaCitas.html',form=form)


@app.route('/10consultaComentarios',methods = ['GET','POST'])
def consulta_Comentarios():
    form = formulario_med_comD()
    if request.method=='POST':
        Num_Documento_P=form.Num_Documento_P.data
        Id_paciente=form.Id_paciente.data
        Id_Medico=form.Id_Medico.data
        Nombre_p=form.Nombre_p.data
        Nombre_M=form.Nombre_M.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur=conexion.cursor()
            cur.execute('select * from Comentarios where Num_Documento_P=?',[Num_Documento_P])
            row=cur.fetchall()
            if row ==None:
                return ('Comentario no encontrado')
            return render_template('10consultaComentarios.html',row=row, form = form)
    return render_template('10consultaComentarios.html', form=form)  

@app.route('/10consultaComentarios/guardar',methods = ['POST','GET'])
def guardar_comentarios():
    form=formulario_med_comD()
    if request.method =='POST':
        Id_paciente=form.Id_paciente.data
        Id_Medico=form.Id_Medico.data
        Id_Comentarios=form.Id_Comentarios.data
        Nombre_p=form.Nombre_p.data
        Num_Documento_P=form.Num_Documento_P.data
        Nombre_M=form.Nombre_M.data
        Fecha_C=form.Fecha_C.data
        Comentario=form.Comentario.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            cur.execute('insert into Comentarios (Id_Paciente, Id_Medico, Id_Comentarios, Nombre_P,Num_Documento_P, Nombre_M, Fecha_C,Comentario) values (?,?,?,?,?,?,?,?)',[Id_paciente, Id_Medico, Id_Comentarios, Nombre_p,Num_Documento_P, Nombre_M, Fecha_C,Comentario])
            conexion.commit()
            return('El comentario se guardo de manera satisfactoria')
    return ("ERROR - ERROR - ERROR")

@app.route('/10consultaComentarios/editar',methods = ['POST','GET'])
def editar_comentarios():
    form=formulario_med_comD()
    if request.method =='POST':
        Id_paciente=form.Id_paciente.data
        Id_Medico=form.Id_Medico.data
        Id_Comentarios=form.Id_Comentarios.data
        Nombre_p=form.Nombre_p.data
        Num_Documento_P=form.Num_Documento_P.data
        Nombre_M=form.Nombre_M.data
        Fecha_C=form.Fecha_C.data
        Comentario=form.Comentario.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            """cur.execute('update Comentarios set Id_Paciente=?, Id_Medico=?, Nombre_P=?,Num_Documento_P=?, Nombre_M=?, Fecha_C=?,Comentario=? where Id_Comentarios=?',[Id_paciente, Id_Medico, Nombre_p,Num_Documento_P, Nombre_M, Fecha_C,Comentario, Id_Comentarios])"""
            cur.execute('update Comentarios set Comentario=? where Id_Comentarios=? and Num_Documento_P=? ',[Comentario, Id_Comentarios,Num_Documento_P])
            conexion.commit()
            return('El comentario se modifico de manera satisfactoria')
    return ("ERROR - ERROR - ERROR")

@app.route('/10consultaComentarios/eliminar',methods = ['POST','GET'])
def eliminar_comentarios():
    form=formulario_med_comD()
    if request.method=='POST':
        Num_Documento_P=form.Num_Documento_P.data
        Id_paciente=form.Id_paciente.data
        Id_Comentarios=form.Id_Comentarios.data
        Id_Medico=form.Id_Medico.data
        Nombre_p=form.Nombre_p.data
        Nombre_M=form.Nombre_M.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur=conexion.cursor()
            cur.execute('delete from Comentarios where Id_Comentarios=?',[Id_Comentarios])
            conexion.commit()
            if conexion.total_changes>0:
                return ('El comentario se elimino de manera satisfactoria')
            return ('No se elimino el comentario')
    return ('Se presento un error')

@app.route('/11interfazPacientes')
def interfazPacientes():
    return render_template('11interfazPacientes.html')  

@app.route('/12crearCitas',methods = ['GET','POST'])
def crearCitas():
    form= formulario_pac_cc()
    return render_template('12crearCitas.html', form=form) 
    

@app.route('/12crearCitas/guardar',methods = ['GET','POST'])
def crearCitas_guardar():
    form= formulario_pac_cc()
    if request.method =='POST':
        Id_Citas=form.Id_Citas.data
        Id_Paciente=form.Id_Paciente.data
        Id_Medico=form.Id_Medico.data
        Nombre_P=form.Nombre_P.data
        Num_Documento_P=form.Num_Documento_P.data
        Nombre_M=form.Nombre_M.data
        Fecha_C=form.Fecha_C.data
        Hora_C=form.Hora_C.data
        Calificacion_cit=form.Calificacion_cit.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur = conexion.cursor()
            cur.execute('insert into Citas_medicas (Id_Citas, Id_Paciente, Id_Medico, Nombre_P,Num_Documento_P, Nombre_M, Fecha_C,Hora_C,Calificacion_cit) values (?,?,?,?,?,?,?,?,?)',[Id_Citas,Id_Paciente, Id_Medico, Nombre_P,Num_Documento_P, Nombre_M, Fecha_C,Hora_C,Calificacion_cit])
            conexion.commit()
            return('Cita registrada de manera satisfactoria')
    return ("ERROR - ERROR - ERROR") 

@app.route('/12crearCitas/eliminar',methods = ['GET','POST'])
def crearCitas_eliminar():
    form=formulario_pac_cc()
    if request.method=='POST':
        Id_Citas=form.Id_Citas.data
        Id_Paciente=form.Id_Paciente.data
        Id_Medico=form.Id_Medico.data
        Nombre_P=form.Nombre_P.data
        Num_Documento_P=form.Num_Documento_P.data
        Nombre_M=form.Nombre_M.data
        Fecha_C=form.Fecha_C.data
        Hora_C=form.Hora_C.data
        Calificacion_cit=form.Calificacion_cit.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur=conexion.cursor()
            cur.execute('delete from Citas_medicas where Id_Citas=?',[Id_Citas])
            conexion.commit()
            if conexion.total_changes>0:
                return ('La cita medica se elimino de manera satisfactoria')
            return ('No se elimino la cita medica')
    return ('Se presento un error')


@app.route('/13buscarCitas',methods = ['GET','POST'])
def buscarCitas():
    form = formulario_pac_conscitas()
    if request.method =='POST':
        tipo_doc_pac=form.tipo_doc_pac.data
        num_doc_pac=form.num_doc_pac.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            conexion.row_factory=sqlite3.Row
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('select * from Citas_medicas where Num_Documento_P=?',[num_doc_pac])
            row =cur.fetchall()
            if row == None:
                return('El paciente no registra citas ')
            return render_template('13buscarCitas.html',row=row, form = form)
    return render_template('13buscarCitas.html',form = form)

@app.route('/13buscarCitas/Calificacion',methods = ['GET','POST'])
def Calificar_citas():
    form = formulario_pac_conscitas()
    if request.method =='POST':
        Id_Citas=form.Id_Citas.data
        Calificacion_cit=form.Calificacion_cit.data
        with sqlite3.connect('database/DB_CUDAC.db') as conexion:
            cur =conexion.cursor()
            #Sentencia preparada
            cur.execute('update Citas_medicas set Calificacion_cit=? where Id_Citas=?',[Calificacion_cit,Id_Citas])
            conexion.commit()
            return ("La calificación de la cita se modifico de manera satisfactoria")
    return ("ERROR - ERROR - ERROR") 

@app.route('/14citasCumplidas',methods = ['GET','POST'])
def citasCumplidas():
    return render_template('14citasCumplidas.html')  

@app.route('/15citasPendientes',methods = ['GET','POST'])
def citasPendientes():
    return render_template('15citasPendientes.html')

@app.route('/16asignarRoles',methods = ['GET','POST'])
def asignarRoles1():
    if request.method == 'POST':
        usuarios = request.form['registrousuario']
        contraseñas = request.form['registrocontraseña']
        roles = request.form['registroroles']
        contraseñasHas = generate_password_hash(contraseñas)
        sql = 'INSERT INTO User (usuario, contrasena, roles) VALUES (?,?,?)'
        db = get_db()
        result = db.execute(sql, (usuarios, contraseñasHas, roles)).rowcount
        db.commit()
        if result!= 0:
            flash('Registro exitoso')
        else:
            flash('Hubo un error. Intenta nuevamente')         
    return render_template('16asignarRoles.html')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return render_template('1login.html')


if __name__=='__main__':
    app.run(debug=True)


