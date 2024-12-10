let monthNames = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Deciembre','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Deciembre','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Deciembre'];

let currentDate = new Date();
let currentDay = currentDate.getDate();
let monthNumber = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

let month = document.getElementById('month');
let year = document.getElementById('year');


let fecha1 = new Date(currentDate);
let fecha2 =new Date() ;

let fecha; 

function calcular(fecha1, fecha2) {
  
  if (!(fecha1 instanceof Date)|| !(fecha2 instanceof Date)){
  throw TypeError ('Ambos datos deben ser argumentos de fecha (Date).');
  }
    let meses = (fecha2.getFullYear() - fecha1.getFullYear())  * 12;
    meses -= fecha1.getMonth();
    meses +=fecha2.getMonth();
  return meses;
}
function enviar(){
  let a ;
  let i = monthNumber;
  while (i < monthNumber + calcular(fecha1,fecha2)) {
    let a = monthNames[i];
    month.innerHTML += `<th> ${a} </th>`
      i++;
  }
  
} 

function muestracolumna(tabla,numerocolumna){
  for (let i = 0,celda; i < tabla.rows.length; i++){
    celda = tabla.rows[i].cells[numerocolumna];
    fecha = celda.innerHTML
    tranformaciondato()   
  }
}
function tranformaciondato(){
  fecha = fecha.replace(/\D/g, ',');
  fecha2= new Date(fecha); 
  genera_celdas(); 
} 

function genera_celdas() {
  
  // Obtener la referencia del elemento body
  var body = document.getElementsByTagName("body")[0];

  var table = document.getElementsByTagName("table")[0];
 
  var tbody = document.getElementsByTagName("tbody")[0];
  //var tr = document.getElementsByTagName("tr");
  var j = monthNumber;
   // Crea las celdas
   for (var i = 0; i < 1; i++) {
    // Crea las hileras de la tabla
    var hilera = document.getElementsByTagName("tr")[i];

    for ( var j ; j < monthNumber + calcular(fecha1,fecha2); j++) {
     
      // Crea un elemento <td> y un nodo de texto, haz que el nodo de
      // texto sea el contenido de <td>, ubica el elemento <td> al final
      // de la hilera de la tabla
      let a = monthNames[j];
      var celda = document.createElement("td");
     
      
      var textoCelda = document.createTextNode( a);
      celda.appendChild(textoCelda);
      
      hilera.appendChild(celda);
    }

    // agrega la hilera al final de la tabla (al final del elemento tblbody)
    tbody.appendChild(hilera);
    table.appendChild(tbody);
  }
 

}



