#funcion para separar un numero telefonico por un "-" creando una estructura similar 1-23-456-7891


function separa_numero_telefonico($numero){
$separar = 1;
$cadena = (string)$numero;
$long = strlen($cadena);
for($i=0; $i<$long; $separar++) {
	if ($i==0){
		$telefono= substr($cadena, $i, $separar);
	}
	else {
		 $telefono = $telefono."-".substr($cadena, $i, $separar);
	}
    $i+= $separar;
}
return $telefono; }
