<?php $parameter=$_SERVER["QUERY_STRING"];
$url= 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
parse_str(parse_url($url)['query'],$query_arr);
$id= $query_arr['id'];

?>

<?php    
header('Content-Type: application/json');
 
$db = new mysqli('localhost', 'cs143', '', 'class_db');
if ($db->connect_errno > 0) { 
    die('Unable to connect to database [' . $db->connect_error . ']'); 
}    

$statement = $db->prepare("SELECT id FROM org" );

$statement->execute();
$statement->bind_result($id_org);
$org_id=array();
while($statement->fetch()){
      $org_id[]=$id_org;                                                                 //get the id of all the organizations
}


if (in_array($id,$org_id)){                             //check if it is organization or person
$statement = $db->prepare("SELECT o.name_org, o.dof, o.city,o.country, a.awardYear, a.category, a.sortorder FROM org o, award a WHERE o.id=a.id AND o.id=?" );
$statement->bind_param('i', $id);
$statement->execute();
$statement->bind_result( $name_org,$dof,$city_org,$country_org,$year,$category,$sortorder);
$array1=array();
$i=0;
$array_prize=array();
while($statement->fetch()){

$array_prize[$i]=array(
     "awardYear" => strval($year),
     "category" => (object) [  "en" => $category ] ,
     "sortOrder" => strval($sortorder)
) ;

array_push($array1,$array_prize[$i]);

$output = (object) [
    "id" => strval($id),
    "orgName" => (object) [
        "en" => strval($name_org)
    ],
   "founded" => (object) [
        "date" => strval($dof),
        "place" => (object) [
         "city" =>(object) [  "en" => strval($city_org)],
         "country" =>(object) [  "en" => strval($country_org)]
    ]
    ],
    "nobelPrizes" => $array1
];  

$i=$i+1;

}  

//$array =  (array) $output;
$array_org = json_decode(json_encode($output), true);      //transform the output from object type into array type

function array_filter_recursive(array &$arr)            //define a function that delete the empty attributes
{
    if (count($arr) < 1) {
        return [];
    }
    foreach ($arr as $k => $v) {
        if (is_array($v)) {
            $arr[$k] = array_filter_recursive($v);
        }
        if (is_null($arr[$k]) && $arr[$k] == '') {
            unset($arr[$k]);
        }
    }
    return array_filter($arr);
}

$array_org = array_filter_recursive($array_org);
echo json_encode((object)$array_org, JSON_PRETTY_PRINT);


} 





else{
$statement = $db->prepare("SELECT p.gname_person, p.fname_person, p.gender, p.dob, p.city,p.country, a.awardYear, a.category, a.sortorder, f.name_aff, f.city, f.country FROM person p, award a, affiliations f WHERE p.id=a.id  AND f.id= p.id AND p.id=?" );
$statement->bind_param('i', $id);
$statement->execute();
$statement->bind_result( $gname_person,$fname_person,$gender,$dob,$city_person,$country_person,$awardyear,$category_person,$sortorder_person,$name_aff,$city_aff,$country_aff);

$array1=array();
$i=0;
$array_prize=array();
while($statement->fetch()){

$array_prize[$i]=array(
     "awardYear" => strval($awardyear),
     "category" => (object) ["en" => $category_person ],
     "sortOrder" => strval($sortorder_person),
     "affiliations" => (object) [array(
           "name" => (object) [ "en" => $name_aff ],
           "city" => (object) [ "en" => $city_aff ],           
           "country" => (object) [ "en" => $country_aff ]
)]
) ;

array_push($array1,$array_prize[$i]);

$output = (object) [
    "id" => strval($id),
    "givenName"=> (object) [
        "en" => strval($gname_person)
    ],
    "familyName"=> (object) [
        "en" => strval($fname_person)
    ],
    "gender" => strval($gender), 
    "birth" => (object) [
        "date" => strval($dob),
        "place" => (object) [
         "city" =>(object) [  "en" => strval($city_person)],
         "country" =>(object) [  "en" => strval($country_person)]
    ]
    ],
    "nobelPrizes" => $array1
];  

$i=$i+1;
}  

$array = json_decode(json_encode($output), true);      //transform the output from object type into array type

function array_filter_recursive(array &$arr)            //define a function that delete the empty attributes
{
    if (count($arr) < 1) {
        return [];
    }
    foreach ($arr as $k => $v) {
        if (is_array($v)) {
            $arr[$k] = array_filter_recursive($v);
        }
        if (is_null($arr[$k]) && $arr[$k] == '') {
            unset($arr[$k]);
        }
    }
    return array_filter($arr);
}

$array = array_filter_recursive($array);
//print_r ($array);
echo json_encode((object)$array, JSON_PRETTY_PRINT);
}


?>






