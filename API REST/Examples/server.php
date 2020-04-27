<?php

$user = array_key_exists('PHP_AUTH_USER', $_SERVER ) ?  $_SERVER['PHP_AUTH_USER'] : '';
$password = array_key_exists('PHP_AUTH_PW', $_SERVER ) ?  $_SERVER['PHP_AUTH_PW'] : '';

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