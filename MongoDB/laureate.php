<?php $parameter=$_SERVER["QUERY_STRING"];
$url= 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
parse_str(parse_url($url)['query'],$query_arr);
$id= $query_arr['id'];
?>

<?php


// set the Content-Type header to JSON, 
// so that the client knows that we are returning JSON data
header('Content-Type: application/json');

$mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");

$filter = ["id"=> strval($id) ];
$options = ["projection" => ['_id' => 0]];
$query = new MongoDB\Driver\Query($filter, $options); 
$rows = $mng->executeQuery("nobel.laureates", $query);

$result= current($rows->toArray());                
//returned object type data should be tansformed to array type before going to json_encode method




echo json_encode($result, JSON_PRETTY_PRINT);





?>