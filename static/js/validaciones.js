function consultar_pac(){
    document.getElementById('formulario_cons_pac').action ='/8consultaPacientes';
}
function consultar_comentarios(){
    document.getElementById('formulario_cons_com').action ='/10consultaComentarios';
}
function guardar_comentario(){
    document.getElementById('formulario_cons_com').action ='/10consultaComentarios/guardar';
}
function editar_comentario(){
    document.getElementById('formulario_cons_com').action ='/10consultaComentarios/editar';
}
function eliminar_comentarios(){
    document.getElementById('formulario_cons_com').action ='/10consultaComentarios/eliminar';
}
function consultar_citas(){
    document.getElementById('formulario_cons_cit').action ='/9consultaCitas';
}

function Crearcitas_guardar(){
    document.getElementById('formulario_pac_cc').action ='/12crearCitas/guardar';
}
function Crearcitas_eliminar(){
    document.getElementById('formulario_pac_cc').action ='/12crearCitas/eliminar';
}
function cons_citas_paciente(){
    document.getElementById('formulario_cons_cit_pac').action ='/13buscarCitas';
}
function calif_citas_paciente(){
    document.getElementById('formulario_cons_cit_pac').action ='/13buscarCitas/Calificacion';
}

function guardar_paciente(){
    document.getElementById('register_pac').action = '/3registroDePacientes/guardar';
}
function editar_paciente(){
    document.getElementById('register_pac').action = '/3registroDePacientes/editar';
}
function eliminar_paciente(){
    document.getElementById('register_pac').action = '/3registroDePacientes/eliminar';
}
function guardar_medico(){
    document.getElementById('register_med').action = '/4registroDeMedicos/guardar';
}
function editar_medico(){
    document.getElementById('register_med').action = '/4registroDeMedicos/editar';
}
function eliminar_medico(){
    document.getElementById('register_med').action = '/4registroDeMedicos/eliminar';
}
function Cons_Adm_paciente(){
    document.getElementById('formulario_cons_rp').action = '/5verRegistroDePacientes';
}
function Cons_Adm_medico(){
    document.getElementById('formulario_cons_rm').action = '/6verRegistroDeMedicos';
}

