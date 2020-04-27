<?php

header( 'Content-Type: application/json' );

if ( 
    # La letra X se refiere a encabezados no estandar
	!array_key_exists('HTTP_X_HASH', $_SERVER) || 
	!array_key_exists('HTTP_X_TIMESTAMP', $_SERVER) || 
	!array_key_exists('HTTP_X_UID', $_SERVER)  
    )  {
		header( 'Status-Code: 403' );
	
		echo json_encode(
			[
				'error' => "No autorizado",
			]
		);
		
		die;
    }
    
list( $hash, $uid, $timestamp) = [
    $_SERVER['HTTP_X_HASH'],
    $_SERVER['HTTP_X_TIMESTAMP'],
    $_SERVER['HTTP_X_UID'],
];

$secret = 'Sh!! No se lo cuentes a nadie!';

$newHash = sha1($uid.$timestamp.$secret);

if($newHash !== $hash) {
    die;
}

// Se define los recursos disponibles
$allowedResorceTypes = [
    'books',
    'authors',
    'genres'
];


if ( $user !== 'korkux' || $password !== '123') {
    echo "Logueate para poder usar la aplicación";
}

# Verificar si el tipo de recurso solicitado está dentro de los posibles
$resourceType = $_GET['resource_type'];

if(!in_array($resourceType, $allowedResorceTypes)){
    die;
}

//Defino los recursos
$books = [
    1 => [
        'title' =>  'Lo que el viento se llevo',
        'id_author' => 2,
        'id_genre' => 2
    ],
    2 => [
        'title' =>  'La Iliada',
        'id_author' => 1,
        'id_genre' => 1
    ],
    3 => [
        'title' =>  'La Odisea',
        'id_author' => 1,
        'id_genre' => 1
    ],
];

header('Content-Type: application/json');

// Obtenemos el Id del recurso
$resourceId = array_key_exists('resource_id', $_GET) ? $_GET['resource_id']: '';

// Generamos la respuesta asumiendo que el pedido es correcto
switch( strtoupper($_SERVER['REQUEST_METHOD']) ) {
    case 'GET':
        if ( empty( $resourceId ) ){
            echo json_encode( $books );
        }else{
             // si llegan a pedir un recurso en especifico
            if( array_key_exists( $resourceId, $books) ){
                echo json_encode( $books[ $resourceId ] );
            }
        }
        break;
    case 'POST':
        $json = file_get_contents('php://input');
        $books[] = json_decode($json, true);

        echo array_keys($books)[count($books)-1];
    break;
    case 'PUT':
        // Validamos que el recurso enviado exista
        if (!empty($resourceId) && array_key_exists($resourceId, $books)){
            // Tomamos la entrada cruda
            $json = file_get_contents('php://input');
             // transformamos el json recibido a un nuevo elemento del arreglo
            $books[$resourceId] = json_decode($json, true);
            // Retornamos la coleccion modificada en formato json
            echo json_encode($books);
        }
    break;
    case 'DELETE':
        if (!empty($resourceId) && array_key_exists($resourceId, $books)){
            // Eliminamos el recurso
            unset( $books[ $resourceId]);    
            // Aquí verificamos que los cambios se han realizado  
            echo json_encode($books);      
        }
    break;
    default:
        # code...
        break;
}