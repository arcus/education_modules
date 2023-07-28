<!--
author:   Peter Camacho
email:    camachop@chop.edu
version: 1.0.3
module_template_version: 2.0.0
language: en
narrator: US English Male
title: SQL, Intermediate Level
comment:  Learn how to do intermediate SQL queries on single tables, by using code, hands-on.
long_description: Do you want to learn intermediate Structured Query Language (SQL) for more precise and complex data querying on single tables?  This module will give you hands on experience with single-table queries using keywords including CASE, LIKE, REGEXP_LIKE, GROUP BY, HAVING, and WITH, along with a number of aggregate functions like COUNT and AVG.  This module is appropriate for people who are comfortable writing basic SQL queries and are ready to practice more advanced sklls.
estimated_time: 1 hour

@learning_objectives  

After completion of this module, learners will be able to:

* Create new data classifications using `CASE` statements
* Find text that matches a given pattern using `LIKE` and `REGEXP_LIKE` statements
* Use `GROUP BY` and `HAVING` statements along with aggregate functions to understand group characteristics
* Use `WITH` to create sub queries

@end


@version_history
1.0.2: Clarify group by aggregation troubleshooting

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

script: https://cdn.jsdelivr.net/npm/alasql@0.6.5/dist/alasql.min.js
attribute: [AlaSQL](https://alasql.org)
           by [Andrey Gershun](agershun@gmail.com)
           & [Mathias Rangel Wulff](m@rawu.dk)
           is licensed under [MIT](https://opensource.org/licenses/MIT)

script: https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.6.1/papaparse.min.js
attribute: [PapaParse](https://www.papaparse.com)
           by [Matthew Holt](https://twitter.com/mholt6)
           is licensed under [MIT](https://opensource.org/licenses/MIT)

script: https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js
attribute: [jQuery](https://jquery.com/)
           is licensed under [OpenJS Foundation](https://openjsf.org/)

@AlaSQL.eval
<script>
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// BUILD FUNCTIONS
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function buildHtmlTable() {
  // Builds the HTML Table out of myList, and writes output to the id attribute assigned via the "@0" argument to this marco.
  var columns = addAllColumnHeaders(myList);
  for (var i = 0 ; i < myList.length ; i++) {
    var row$ = $('<tr/>');
    for (var colIndex = 0 ; colIndex < columns.length ; colIndex++) {
      var cellValue = myList[i][columns[colIndex]];
      if (cellValue == null) { cellValue = ""; }
      row$.append($('<td/>').html(cellValue).css({
      "padding-left": "1em",
      "padding-right": "1em"
      }));
    }
    $(@0).append(row$);
  }
  try { // Error Handling for no null.
    var rowCount = document.getElementById(@0.substring(1)).rows.length - 1;
  } catch(err) {
    var cnt = 0
  }
  if (rowCount > 0) {
    var complete_message = "Query Execution Complete! (See Result Set Below)..."
  } else {
    var complete_message = "No Data to Return.."
  }
  return JSON.stringify(complete_message, null, 3);
}
function addAllColumnHeaders(myList) {
  // Creates and Returns Header Row From Array Data Provided as Input.
  var columnSet = [];
  var headerTr$ = $('<tr/>');
  for (var i = 0 ; i < myList.length ; i++) {
    var rowHash = myList[i];
    for (var key in rowHash) {
      if ($.inArray(key, columnSet) == -1){
        columnSet.push(key);
        headerTr$.append($('<th/>').html(key));
      }
    }
  }
  $(@0).append(headerTr$);
  return columnSet;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try {
    var myinput=`@input`
    myinput=myinput.replace(/;/, ""); // remove all semi-colon
    var myStriptArray= myinput.split(';');
    var arrayLength = myStriptArray.length;
    console.clear();
    for (var i = 0; i < arrayLength; i++) {
        if((myStriptArray[i].trim()).length != 0) { // ignore blank queries.
            var myList=alasql(myStriptArray[i]);
        }
        if (myList != 1  & ((myStriptArray[i].trim()).length) != 0) { // If data is returned, format output as table.
            $(@0).html(""); // clear out existing data
            buildHtmlTable();
        } else {
            $(@0).html(""); // clear out existing data
            JSON.stringify("No Data to Return..", null, 3);
        }
    }
} catch(e) {
  let error = new LiaError(e.message, 1);
  try {
    let log = e.message.match(/.*line (\d):.*\n.*\n.*\n(.*)/);
    error.add_detail(0, e.name+": "+log[2], "error", log[1] -1 , 0);
  } catch(e) {
  }
  throw error;
}
</script>
@end

@AlaSQL.buildTable_patients
<script>
    alasql("DROP TABLE IF EXISTS patients;");
    alasql("create table patients (id text,birthdate date,deathdate date,ssn text,drivers text,passport text,prefix text,first text,last text,suffix text,maiden text,marital text,race text,ethnicity text,sex text,birthplace text,address text,city text,state text,county text,zip text,lat real,lon real, expenses real, coverage real);");
    alasql("INSERT INTO patients VALUES ('03963166-b49f-4440-a80d-30abb90b4a78', '1979-08-19', 'NA', '999-53-2391', 'S99976779', 'X57420256X', 'Mr.', 'Jacob959', 'Daniel959', 'NA', 'NA', 'M', 'white', 'nonhispanic', 'M', 'Danvers  Massachusetts  US', '699 Ankunding Run Apt 36', 'Norwood', 'Massachusetts', 'Norfolk County', '02062', '42.1716590630744', '-71.2263318929621', '125695.89', '4242.12');");
alasql("INSERT INTO patients VALUES ('0982ef39-7ff9-4c24-8239-e9fc0667e8ca', '1998-12-14', 'NA', '999-87-3074', 'S99917986', 'X72211827X', 'Ms.', 'Stasia733', 'Kirlin939', 'NA', 'NA', 'NA', 'other', 'nonhispanic', 'F', 'Lynn  Massachusetts  US', '958 Robel Run Unit 83', 'Carver', 'Massachusetts', 'Plymouth County', 'NA', '41.9005925642133', '-70.7320231895707', '37492.08', '444.96');");
alasql("INSERT INTO patients VALUES ('1474f954-3781-4de1-9d5d-27a2b8688419', '1994-02-25', 'NA', '999-61-4523', 'S99953247', 'X66416063X', 'Ms.', 'Tamisha203', 'Considine820', 'NA', 'NA', 'NA', 'white', 'nonhispanic', 'F', 'Worcester  Massachusetts  US', '589 McLaughlin Route Apt 69', 'Wareham', 'Massachusetts', 'Plymouth County', 'NA', '41.7607992858186', '-70.7511725489897', '84681.47', '9639.33');");
alasql("INSERT INTO patients VALUES ('29fc389e-f454-4907-8fa5-987f312cc32a', '1982-03-07', 'NA', '999-59-4905', 'S99924114', 'X76526910X', 'Mr.', 'Eusebio566', 'Cremin516', 'NA', 'NA', 'M', 'white', 'hispanic', 'M', 'Woburn  Massachusetts  US', '915 Legros Neck Apt 5', 'Lynn', 'Massachusetts', 'Essex County', '01905', '42.4827539638704', '-70.8578543300735', '791005.88', '4364.56');");
alasql("INSERT INTO patients VALUES ('2abf5d21-8d0f-4263-b720-81d9d25f7a70', '1991-06-20', 'NA', '999-49-8301', 'S99922026', 'X65406262X', 'Mr.', 'Abram53', 'Schinner682', 'NA', 'NA', 'M', 'black', 'nonhispanic', 'M', 'Franklin  Massachusetts  US', '1071 Bahringer Park', 'Mansfield', 'Massachusetts', 'Bristol County', 'NA', '42.0170083027574', '-71.2201039521409', '667979.05', '3695.48');");
alasql("INSERT INTO patients VALUES ('344de08b-bae0-4d79-b89e-a2b6204e1a21', '1941-02-14', '1958-01-03', '999-43-4878', 'S99994390', 'NA', 'NA', 'Sibyl335', 'Zulauf375', 'NA', 'NA', 'NA', 'black', 'nonhispanic', 'F', 'Southbridge  Massachusetts  US', '449 Shields Extension Unit 55', 'Hanover', 'Massachusetts', 'Plymouth County', 'NA', '42.0829961514318', '-70.8269756491514', '449896.36', '1854');");
alasql("INSERT INTO patients VALUES ('4a50c62e-24ba-459b-993c-0959691cf96d', '1947-07-12', '1989-11-25', '999-13-8181', 'S99993186', 'X9890795X', 'Mrs.', 'Kristeen693', 'Cole117', 'NA', 'Konopelski743', 'M', 'asian', 'nonhispanic', 'F', 'Hong Kong  Hong Kong Special Administrative Region  CN', '1070 Bartoletti Neck', 'Peabody', 'Massachusetts', 'Essex County', 'NA', '42.4942259149787', '-71.0785466574374', '848337.83', '5741.8');");
alasql("INSERT INTO patients VALUES ('50ee80ee-bce0-4794-87f6-d0fb74a88f8a', '1997-10-15', 'NA', '999-42-6450', 'S99964529', 'X81391446X', 'Mr.', 'Esteban536', 'Sierra982', 'NA', 'NA', 'NA', 'black', 'nonhispanic', 'M', 'Carolina  Puerto Rico  PR', '677 Hoppe Rapid', 'Boston', 'Massachusetts', 'Suffolk County', '02134', '42.3620775494977', '-71.0746898287342', '519266.17', '3938');");
alasql("INSERT INTO patients VALUES ('55506d51-2c6a-4608-aae3-7cb2f111c926', '1941-06-14', 'NA', '999-49-7097', 'S99984057', 'X2961509X', 'Ms.', 'Rosalind66', 'Torp761', 'NA', 'NA', 'S', 'white', 'nonhispanic', 'F', 'Ludlow  Massachusetts  US', '1000 Runolfsdottir Extension', 'Lowell', 'Massachusetts', 'Middlesex County', '01851', '42.6514751630267', '-71.318674676214', '1716727.06', '7784.36');");
alasql("INSERT INTO patients VALUES ('5b891358-1bb3-4bbf-b8a6-a73fbe58efe7', '1962-12-21', 'NA', '999-58-8644', 'S99992512', 'X35458892X', 'Ms.', 'Rene434', 'Schinner682', 'NA', 'NA', 'S', 'black', 'nonhispanic', 'F', 'Lowell  Massachusetts  US', '604 Sipes Divide Unit 0', 'Boston', 'Massachusetts', 'Suffolk County', '02136', '42.2380394989987', '-71.1400184488966', '1116196.22', '3667.92');");
alasql("INSERT INTO patients VALUES ('6e20fc08-a75d-43db-b642-4f15064aeb0d', '2016-11-21', 'NA', '999-91-7902', 'NA', 'NA', 'NA', 'Cathie710', 'Beatty507', 'NA', 'NA', 'NA', 'black', 'nonhispanic', 'F', 'Marblehead  Massachusetts  US', '227 Rippin Vista', 'Walpole', 'Massachusetts', 'Norfolk County', '02081', '42.1276179917707', '-71.2445777349412', '94888.09', '1549.92');");
alasql("INSERT INTO patients VALUES ('7f9a57e5-cfc5-4970-b19f-1a7b6ce22882', '1971-09-11', 'NA', '999-59-9011', 'S99961342', 'X35775930X', 'Mrs.', 'Emilie407', 'Bednar518', 'NA', 'Keeling57', 'M', 'asian', 'nonhispanic', 'F', 'Hanoi  Hà Đông  VN', '846 Marvin Approach Unit 12', 'Lowell', 'Massachusetts', 'Middlesex County', '01854', '42.6747573365128', '-71.2862778307696', '1148999.04', '5613.64');");
alasql("INSERT INTO patients VALUES ('88ea8573-863c-47e3-b144-b810c63156a0', '1962-10-25', 'NA', '999-64-2812', 'S99970548', 'X27386052X', 'Mrs.', 'Mayte822', 'Candelaria844', 'NA', 'Hernandes724', 'M', 'other', 'hispanic', 'F', 'Santo Domingo  National District  DO', '222 Weimann Parade Apt 21', 'Billerica', 'Massachusetts', 'Middlesex County', 'NA', '42.5605178544939', '-71.2305090816335', '1198802.9', '49212.96');");
alasql("INSERT INTO patients VALUES ('8d236c5c-485e-4030-b3e8-20e580afbb0a', '2010-03-11', 'NA', '999-37-4171', 'NA', 'NA', 'NA', 'Donn979', 'Casper496', 'NA', 'NA', 'NA', 'asian', 'nonhispanic', 'M', 'Westford  Massachusetts  US', '330 Hermiston Trafficway', 'Westborough', 'Massachusetts', 'Worcester County', 'NA', '42.3146913804637', '-71.6092388699133', '232331.46', '2698.17');");
alasql("INSERT INTO patients VALUES ('99b1c709-00fc-4be2-97ba-a6222e567305', '1992-10-05', 'NA', '999-72-9974', 'S99975875', 'X37620710X', 'Mr.', 'Forrest301', 'Jacobs452', 'NA', 'NA', 'M', 'white', 'hispanic', 'M', 'Wrentham  Massachusetts  US', '722 Ullrich Promenade', 'Everett', 'Massachusetts', 'Middlesex County', '02148', '42.4779060051335', '-71.0204050464474', '733205.81', '2664.8');");
alasql("INSERT INTO patients VALUES ('ab88386a-1c0d-4d1c-89fc-b38f631b3edc', '1990-01-25', 'NA', '999-85-3833', 'S99935526', 'X74358200X', 'Mrs.', 'Oda116', 'Willms744', 'NA', 'Dietrich576', 'M', 'white', 'nonhispanic', 'F', 'Acushnet  Massachusetts  US', '158 Rempel Drive', 'Wareham', 'Massachusetts', 'Plymouth County', 'NA', '41.7864240325723', '-70.7434572830845', '753274.93', '4847.99');");
alasql("INSERT INTO patients VALUES ('b1d50391-79c5-403c-919f-3ded66c9d77a', '1959-09-01', 'NA', '999-96-8597', 'S99987915', 'X27141234X', 'Mrs.', 'Gertie348', 'Runolfsson901', 'NA', 'Nolan344', 'M', 'black', 'hispanic', 'F', 'Westborough  Massachusetts  US', '361 Haag Boulevard Unit 0', 'Springfield', 'Massachusetts', 'Hampden County', 'NA', '42.134943625397', '-72.601106133145', '1308480.38', '13897.55');");
alasql("INSERT INTO patients VALUES ('ca24f616-30cc-4351-aca9-1b49297de076', '1942-05-23', '2001-02-10', '999-61-4406', 'S99934749', 'X55713048X', 'Mr.', 'Filiberto722', 'Adams676', 'NA', 'NA', 'M', 'native', 'nonhispanic', 'M', 'Boston  Massachusetts  US', '673 Pagac Esplanade Apt 20', 'Chatham', 'Massachusetts', 'Barnstable County', '02633', '41.6887565172739', '-69.9407634414895', '198943.29', '51847.26');");
alasql("INSERT INTO patients VALUES ('cafc2141-2307-4f62-abd1-2d6e5486d7a5', '1942-05-23', '2011-12-14', '999-68-4539', 'S99979088', 'X14233432X', 'Mr.', 'Alonso270', 'Gerhold939', 'NA', 'NA', 'M', 'native', 'nonhispanic', 'M', 'West Springfield  Massachusetts  US', '260 Effertz Hollow', 'Chatham', 'Massachusetts', 'Barnstable County', '02633', '41.6313534346182', '-70.0176252634712', '236803.89', '34294.4');");
alasql("INSERT INTO patients VALUES ('d286528e-a39a-4c04-8545-5e648f781052', '1974-04-25', 'NA', '999-72-6418', 'S99924001', 'X17879337X', 'Mrs.', 'Scottie437', 'Koss676', 'NA', 'Witting912', 'M', 'black', 'nonhispanic', 'F', 'Worcester  Massachusetts  US', '474 Hettinger Arcade', 'Hamilton', 'Massachusetts', 'Essex County', 'NA', '42.605565952088', '-70.8917039273168', '890218.58', '7506.68');");
alasql("INSERT INTO patients VALUES ('dcda9f18-59eb-402e-985b-f13c15c2131c', '2012-12-19', 'NA', '999-10-6031', 'NA', 'NA', 'NA', 'Colby655', 'Gleichner915', 'NA', 'NA', 'NA', 'white', 'nonhispanic', 'M', 'Peabody  Massachusetts  US', '408 Dicki Corner Unit 82', 'Everett', 'Massachusetts', 'Middlesex County', '02148', '42.4043223426552', '-71.0735281194192', '197008.18', '2066.56');");
alasql("INSERT INTO patients VALUES ('e175908a-09db-4730-a311-4e57ba73438b', '2009-05-07', 'NA', '999-19-6600', 'NA', 'NA', 'NA', 'Eveline832', 'Wintheiser220', 'NA', 'NA', 'NA', 'black', 'hispanic', 'F', 'Sandwich  Massachusetts  US', '895 MacGyver Skyway', 'Chicopee', 'Massachusetts', 'Hampden County', '01020', '42.1834548010167', '-72.5016471115102', '26070.08', '645.8');");
alasql("INSERT INTO patients VALUES ('e974e5c3-9b22-41f2-b3a3-c12848f29a73', '1922-02-14', '2016-04-17', '999-40-9174', 'S99950579', 'X27596354X', 'Mrs.', 'Ramona980', 'Alcaraz418', 'NA', 'Vázquez552', 'M', 'asian', 'hispanic', 'F', 'Port-au-Prince  Haiti  HT', '932 Hoppe Camp Unit 1', 'Cambridge', 'Massachusetts', 'Middlesex County', '02140', '42.32956821377', '-71.0655750714097', '1399151.49', '28678.46');");
alasql("INSERT INTO patients VALUES ('ed6fb8d6-c14d-4e34-a029-2dab33855ddd', '1973-06-10', 'NA', '999-41-4345', 'S99931849', 'X85490024X', 'Mrs.', 'Sara501', 'Arreola736', 'NA', 'Medina536', 'M', 'native', 'hispanic', 'F', 'Caguas  Puerto Rico  PR', '313 Gulgowski Plaza Unit 81', 'Peabody', 'Massachusetts', 'Essex County', 'NA', '42.5629355117525', '-71.017704116768', '155686.2', '20059.08');");
alasql("INSERT INTO patients VALUES ('fcc61454-1b07-4e49-a25b-29e5064e0063', '1966-07-06', 'NA', '999-87-1534', 'S99948423', 'X7514421X', 'Mr.', 'Patrick786', 'Farrell962', 'NA', 'NA', 'M', 'asian', 'nonhispanic', 'M', 'Hanoi  Hà Đông  VN', '341 Homenick Trailer Suite 77', 'Marlborough', 'Massachusetts', 'Middlesex County', '01752', '42.3590769360988', '-71.5160843735423', '1392358.66', '5569.53');");
</script>
@end

@AlaSQL.buildTable_allergies
<script>
    alasql("DROP TABLE IF EXISTS allergies;");
    alasql("create table allergies (start date,stop date,patient text,encounter text,description text);");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Shellfish allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('2002-01-24',null,'bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('2014-12-04',null,'e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1998-07-19','2014-03-20','e061409e-4b85-4ec1-b1f7-02677d51f763','022ad487-e41c-43ba-90f3-eb2d6711f4d3','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1998-07-19','2014-03-20','e061409e-4b85-4ec1-b1f7-02677d51f763','022ad487-e41c-43ba-90f3-eb2d6711f4d3','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1998-07-19',null,'e061409e-4b85-4ec1-b1f7-02677d51f763','022ad487-e41c-43ba-90f3-eb2d6711f4d3','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1998-07-19',null,'e061409e-4b85-4ec1-b1f7-02677d51f763','022ad487-e41c-43ba-90f3-eb2d6711f4d3','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1974-05-17',null,'71e13815-55fb-4734-bcac-6079160d82a0','9607667e-4c98-4087-9c59-0fd5b6331078','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1974-05-17',null,'71e13815-55fb-4734-bcac-6079160d82a0','9607667e-4c98-4087-9c59-0fd5b6331078','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('1974-05-17',null,'71e13815-55fb-4734-bcac-6079160d82a0','9607667e-4c98-4087-9c59-0fd5b6331078','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03','2019-12-30','ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to dairy product');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to nut');");
    alasql("INSERT INTO allergies VALUES ('2004-07-03',null,'ca3330c5-bbbc-47e7-addb-302f2e069986','d8f2b92b-5971-455f-a0b9-99da66d03899','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1978-11-04',null,'24bca5cf-ba55-457f-8e80-49690202443c','1d475126-f3c0-41c9-a9ed-f4a0c9a955c4','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1978-11-04',null,'24bca5cf-ba55-457f-8e80-49690202443c','1d475126-f3c0-41c9-a9ed-f4a0c9a955c4','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1978-11-04',null,'24bca5cf-ba55-457f-8e80-49690202443c','1d475126-f3c0-41c9-a9ed-f4a0c9a955c4','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('1978-11-04',null,'24bca5cf-ba55-457f-8e80-49690202443c','1d475126-f3c0-41c9-a9ed-f4a0c9a955c4','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Shellfish allergy');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Allergy to nut');");
    alasql("INSERT INTO allergies VALUES ('2018-03-20',null,'841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1951-04-21',null,'ee7f6c74-a8ed-4147-b8e2-4879c8657b0f','0b7d2e65-a9df-4b74-84ed-25feffc23f62','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1951-04-21',null,'ee7f6c74-a8ed-4147-b8e2-4879c8657b0f','0b7d2e65-a9df-4b74-84ed-25feffc23f62','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1971-03-07',null,'ab6a2662-f6d1-4da6-b3ce-3929d68650d7','603a0692-9302-459a-84b4-af631dc3aee8','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1971-03-07',null,'ab6a2662-f6d1-4da6-b3ce-3929d68650d7','603a0692-9302-459a-84b4-af631dc3aee8','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('1971-03-07',null,'ab6a2662-f6d1-4da6-b3ce-3929d68650d7','603a0692-9302-459a-84b4-af631dc3aee8','Allergy to nut');");
    alasql("INSERT INTO allergies VALUES ('1971-03-07',null,'ab6a2662-f6d1-4da6-b3ce-3929d68650d7','603a0692-9302-459a-84b4-af631dc3aee8','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31','2020-03-21','4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to eggs');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31','2020-03-21','4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('2002-05-31',null,'4440ff11-69ec-440b-a2bd-dc1c14105e8e','38de2a79-6bea-438e-963f-804823c1e32d','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1994-05-12','2011-02-03','1aa71b23-790e-4d22-92da-c689682c8993','228c992b-3877-454c-920d-fa629bb8c5d9','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('1994-05-12',null,'1aa71b23-790e-4d22-92da-c689682c8993','228c992b-3877-454c-920d-fa629bb8c5d9','Allergy to nut');");
    alasql("INSERT INTO allergies VALUES ('1994-05-12',null,'1aa71b23-790e-4d22-92da-c689682c8993','228c992b-3877-454c-920d-fa629bb8c5d9','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','Allergy to soya');");
    alasql("INSERT INTO allergies VALUES ('1950-01-07',null,'848e0227-5d5d-4bdf-8603-207cdea72e2a','77427b07-f03b-49bc-9556-d69b4feed7ef','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2004-12-06',null,'eafd1fd3-3778-423a-ba79-4584bd310eb4','36279aee-15ff-48ad-a4a6-8ba334466278','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1952-03-10',null,'0288abb6-633c-40c3-ba0c-66c7d957727e','a64c55df-b288-4f78-9996-d2ecf0b65c9d','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1952-03-10',null,'0288abb6-633c-40c3-ba0c-66c7d957727e','a64c55df-b288-4f78-9996-d2ecf0b65c9d','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1952-03-10',null,'0288abb6-633c-40c3-ba0c-66c7d957727e','a64c55df-b288-4f78-9996-d2ecf0b65c9d','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1952-03-10',null,'0288abb6-633c-40c3-ba0c-66c7d957727e','a64c55df-b288-4f78-9996-d2ecf0b65c9d','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1952-03-10',null,'0288abb6-633c-40c3-ba0c-66c7d957727e','a64c55df-b288-4f78-9996-d2ecf0b65c9d','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26','2019-12-25','097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to dairy product');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to soya');");
    alasql("INSERT INTO allergies VALUES ('2004-04-26',null,'097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','9c3c633f-c33c-426c-b771-b6117ba7d6fc','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07','2011-03-09','78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Allergy to dairy product');");
    alasql("INSERT INTO allergies VALUES ('1994-06-07',null,'78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to eggs');");
    alasql("INSERT INTO allergies VALUES ('2011-10-24',null,'c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('2009-01-22',null,'e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','5e4a49f2-47e7-4b76-9120-276a79f1766f','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13','2018-09-08','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13','2018-09-08','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13','2018-09-08','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13',null,'8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13',null,'8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13','2019-05-02','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to eggs');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13','2019-05-02','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('2003-06-13',null,'8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','e75460f0-5f5c-4aa2-ab0b-200310a96c63','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1981-01-29',null,'df7c1d66-eac2-49bd-9d12-ee17e8758f68','a232db22-565f-4559-bb56-edf9021b74b2','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1981-01-29',null,'df7c1d66-eac2-49bd-9d12-ee17e8758f68','a232db22-565f-4559-bb56-edf9021b74b2','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1981-01-29',null,'df7c1d66-eac2-49bd-9d12-ee17e8758f68','a232db22-565f-4559-bb56-edf9021b74b2','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1981-01-29',null,'df7c1d66-eac2-49bd-9d12-ee17e8758f68','a232db22-565f-4559-bb56-edf9021b74b2','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1981-01-29',null,'df7c1d66-eac2-49bd-9d12-ee17e8758f68','a232db22-565f-4559-bb56-edf9021b74b2','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1978-07-20',null,'68878f91-5962-4ef2-83e7-43b8298c1708','95099931-0042-4524-b808-dd6b6447fc0e','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Shellfish allergy');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to fish');");
    alasql("INSERT INTO allergies VALUES ('1963-07-23',null,'1c2aa038-9366-4c7d-9a3e-52cb753a670f','c90b2536-b388-479c-aa7e-3406fe4c2211','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Allergy to bee venom');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Allergy to nut');");
    alasql("INSERT INTO allergies VALUES ('1987-11-30',null,'8d202c65-427d-4190-8c28-3aa27e1a9f4c','16bc6376-a1cc-4d63-8307-c5d7479dc021','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Allergy to wheat');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Shellfish allergy');");
    alasql("INSERT INTO allergies VALUES ('1965-09-23',null,'2a6d1e58-88eb-4be0-b6b4-59a471257c2e','f7ff5032-50cc-480e-90ca-848c85d6d014','Allergy to peanuts');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03','2016-06-25','e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Latex allergy');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Allergy to mould');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','House dust mite allergy');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Dander (animal) allergy');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Allergy to grass pollen');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Allergy to tree pollen');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Allergy to eggs');");
    alasql("INSERT INTO allergies VALUES ('2000-01-03',null,'e6ff4bf9-09c2-4976-aa84-cca142207cf8','6c760807-a6b7-4af4-8d50-f32325803448','Allergy to peanuts');");
</script>
@end

@AlaSQL.buildTable_observations
<script>
    alasql("DROP TABLE IF EXISTS observations;");
    alasql("create table observations (observed date,patient text,encounter text,description text,observation_value text,units text,type text);");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','American house dust mite IgE Ab in Serum','26.0','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Cat dander IgE Ab in Serum','92.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Cladosporium herbarum IgE Ab in Serum','56.9','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Codfish IgE Ab in Serum','70.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Common Ragweed IgE Ab in Serum','93.7','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Cow milk IgE Ab in Serum','0.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Egg white IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Honey bee IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Latex IgE Ab in Serum','6.0','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Peanut IgE Ab in Serum','26.6','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Shrimp IgE Ab in Serum','0.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Soybean IgE Ab in Serum','0.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Walnut IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','Wheat IgE Ab in Serum','75.4','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2014-12-04T23:28:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','469fbd8a-ec48-4da9-9165-027144ccf9a0','White oak IgE Ab in Serum','10.4','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','American house dust mite IgE Ab in Serum','63.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Cat dander IgE Ab in Serum','83.5','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Cladosporium herbarum IgE Ab in Serum','3.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Codfish IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Common Ragweed IgE Ab in Serum','58.7','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Cow milk IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Egg white IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Honey bee IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Latex IgE Ab in Serum','0.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Peanut IgE Ab in Serum','37.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Shrimp IgE Ab in Serum','85.0','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Soybean IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Walnut IgE Ab in Serum','89.9','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','Wheat IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2018-03-20T11:48:11Z','841095eb-d29f-4492-8f0e-08011321e85d','32622f63-734e-4433-8628-942ce1585e6a','White oak IgE Ab in Serum','56.4','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','American house dust mite IgE Ab in Serum','42.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Cat dander IgE Ab in Serum','37.0','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Cladosporium herbarum IgE Ab in Serum','58.7','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Codfish IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Common Ragweed IgE Ab in Serum','42.0','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Cow milk IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Egg white IgE Ab in Serum','60.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Honey bee IgE Ab in Serum','61.8','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Latex IgE Ab in Serum','2.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Peanut IgE Ab in Serum','12.1','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Shrimp IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Soybean IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Walnut IgE Ab in Serum','0.3','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','Wheat IgE Ab in Serum','0.2','kU/L','numeric');");
    alasql("INSERT INTO observations VALUES ('2011-10-24T09:24:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','White oak IgE Ab in Serum','60.7','kU/L','numeric');");
</script>
@end


-->

# SQL, Intermediate Level

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Some experience writing basic SQL code (SELECT, FROM, WHERE) is expected in this module.  If you would like a code-free overview to SQL we recommend our module [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md).  If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).

**Learning Objectives**

@learning_objectives

</div>


## SQL: A Brief Refresher

**SQL** (**S**tructured **Q**uery **L**anguage) is a language that for more than four decades has been used to interact with **relational databases**.  You can pronounce it as "sequel" or just say the letters S-Q-L.

A relational database is a data storage solution that stores data tables, which are comprised of columns (also called 'fields') and rows.

<div class = "important">

Sometimes we'll use the word "column" and sometimes we'll use the word "field".  These refer to the same thing!

</div>

SQL is great at working with rectangular data, data that is stored in tables with rows and columns / fields.  Its powerful SELECT - FROM - WHERE syntax makes SQL an ideal tool for isolating just the data you care about, whether that's specifying the columns you're interested in or limiting your data to just those rows that meet certain conditions.  However, it's not great for fine-tuned statistical, linguistic, or data visualization purposes.  SQL is therefore a tool that is often partnered with other tools like R or Python, which are better suited for work like statistical analysis.

If you want to review SQL at a high level, consider our [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md) module.

Most users of SQL do a lot of their work in one of many SQL **clients**.  A SQL client is a piece of software that has lots of functions, like allowing you to connect to various databases you have access to, giving you a place to type queries and submit them, and diagramming capability to help you understand the relationships in your database.  Here's a screenshot from a popular SQL client, DBeaver.  This screenshot is one they share [on their website](https://dbeaver.io/screenshots/).

![Complex application screen with a long SQL query, connection information for a PostgreSQL database, and more](media/dbeaver_screenshot.png)<!-- style = "max-width: 800px; border: 1px solid rgb(var(--color-highlight));" -->

However, in our module, we won't ask you to download a heavy-duty SQL client.  Rather, you'll work with code in a simple code box like this one.  Go ahead and hit the play button below the code box to run the code below.

```sql
SELECT
  birthdate
  ,sex
FROM patients
LIMIT 10;
```
@AlaSQL.eval("#dataTable2a")

<table id="dataTable2a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

<div class = "important">

Don't worry -- the data here, although it **looks** like human subject or patient data, is completely fabricated.  We used sample data from the open source project [Synthea](https://synthetichealth.github.io/synthea).  There are other clues that this data isn't real: for example, names include a numerical suffix, and SSN values are clearly fake.

</div>

### Style

Whether you adopt our preferred style or not, it's a good idea to have some sort of convention in your way of writing SQL, so that your code is consistent and reader-friendly.  We propose the following as a basic style guide.  To read more about this, reference our [longer treatment of style](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md#5) in our SQL Basics module.

1) **Put keywords in CAPITAL LETTERS so they stand out.**  Examples of keywords are SELECT, LIKE, AS, WHERE, JOIN, DISTINCT, MEAN, ORDER BY, and many more.  While most code editors and SQL clients (software that lets you query a database) do a good job of color-coding these special words, you might end up seeing a SQL query in monochrome, and having keywords stand out helps you figure out where each part of your query is.  

2) **Put members of a list on separate lines.**  This usually means the list of fields you're requesting.  Putting each item on its own line is easier on the eyes and allows for much easier cut-and-paste to rearrange things.  It also means you have space after each item of the list to add a comment if necessary.

3) **Use indentation to clarify the various sections of your query.**  Indenting the list of columns below a SELECT statement is a way of subordinating those lines to the SELECT, subtly indicating that those lines are a continuation of the SELECT statement.  A new line that isn't indented (say, a FROM statement) shows that the SELECT part of the query is over.

4) **Use "dot notation"**, which we'll talk about in the next section.  Dot notation means adding more information about your data, for example, by including the table name the column comes from.  This practice will prepare you for using multiple data sources in your queries.

5) **Use a comma-first style.**  This one can be a little jarring at first, but it does have real advantages, especially if you end up doing SQL for more than a few hours a week.  In a list of length n, don't put the comma **after** items 1 through n-1.  Rather, put the comma **before** items 2 through n.  


## CASE Statement

The `CASE` statement is used to produce conditional row-level output based on columns/rows provided as input.  It's like an "if" statement in other languages, but with multiple possibilities, or "cases", that are considered.  A `CASE` statement will have several lines (possibly many lines), but for any row of data, SQL will give only **one** value back per `CASE` statement.

Often when working with data, you will come across the need to define your own "custom categories/groupings" given some raw row data as input (for example, "normal" versus "borderline" vs "abnormal" hematocrit levels). This is where the `CASE` statement can come in handy!

The `CASE` statement has 4 main components (shown below).


```sql
CASE                --COMPONENT 1: start tag of the case statement.
  WHEN (…) THEN (…) --COMPONENT 2: conditional when "some input" then "some output" logic.
  …                 --             additional "when / then" possibilities continue,
                    --             as many as you need.
  ELSE (…)          --COMPONENT 3: declaration of default value to be returned if
                    --             none of the when/then conditions are met.
END                 --COMPONENT 4: end tag of case statement with optional
                    --             field name (for instance, `AS patient_category`)
```

It's important to note that the `CASE`, `ELSE`, and `END` components can only be listed once for a given `CASE` statement.  Additionally, the `CASE` and `END` components **must** be included).

However, you can list as many occurrences of the `WHEN` / `THEN` component as you would like.

<div class = "important">

When multiple `WHEN` / `THEN` components are listed, SQL will walk through each of them in the order they are listed and will return output for the first `WHEN` condition to be evaluated as TRUE.  This is very important to remember, because sometimes multiple conditions might be true, if you don't write them carefully, but only **one** result will be returned -- the one corresponding to the first matching condition.

</div>

Finally, if no `ELSE` clause is explicitly specified SQL imposes a condition of `ELSE NULL` by default.  We strongly encourage you to always include an `ELSE` clause even if you like the default value of `ELSE NULL`, to make your code more explicit.

The example below looks at "Peanut IgE Ab in Serum" observations (i.e. labs) and uses a `CASE` statement to create a column called `interpretation`, which categorizes (or you might hear "bins", "lumps", or "buckets") the results of the `observations.observation_value` field for each record into one of five distinct categories, or, if none of the criteria is met, makes the value of `interpretation` NULL.

```sql
SELECT
	observations.*
	,CASE
        WHEN observations.observation_value >= 17.5 THEN 'Strongly Positive'
        WHEN observations.observation_value >= .7 THEN 'Positive'
        WHEN observations.observation_value >= 0.35 THEN 'Equivocal'
        WHEN observations.observation_value >= 0.10 THEN 'Borderline'
        WHEN observations.observation_value < 0.10 THEN 'Negative'
        ELSE NULL
	END AS interpretation
FROM alasql.observations
WHERE
	observations.description = 'Peanut IgE Ab in Serum';
```
@AlaSQL.eval("#dataTable4a")

<table id="dataTable4a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_observations

</div>

## LIKE Operator

The `LIKE` operator can be used to filter on row values that contain a simple pattern of text in a column of interest (this action is known as "text/pattern matching").

For the purpose of "pattern matching", the `LIKE` operator is able to utilize the 2 distinct **wildcard characters** listed below:

| Wildcard Characters | Description |
| --- | --- |
| `%` | "Wildcard" for 0 or more characters. |
| `_` | "Wildcard" for exactly 1 characters. |

The code block shown below uses the `LIKE` operator, in the `WHERE` clause, to filter on records from the `allergies` table where the `allergies.description` contains the two letters "nu" or the two letters "fi" (listed one right after the other).

```sql
SELECT DISTINCT allergies.description
FROM alasql.allergies
WHERE
	LOWER(allergies.description) LIKE LOWER('%nu%')
	or LOWER(allergies.description) LIKE LOWER('%fi%')

```
@AlaSQL.eval("#dataTable5a")

<table id="dataTable5a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_allergies

</div>

<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>

Why are we using `LOWER` in the query above? This is a handy trick to make sure that the things we're comparing are in a single case.  You could do the same thing by setting everything to `UPPER`, if you prefer.

If we're not certain if texts are in upper, lower, or mixed case, we can set both sides of a comparison to the same case, assuming that case doesn't matter to us (e.g. *Apples*, *APPLES* and *apples* should be considered equal).  Otherwise, because SQL is **case-sensitive**, the same text in a different case will not be considered equal: *Apples*, *APPLES*, and *apples* are, according to SQL, three different things that are unequal to one another.

But, you might point out, `nu` and `fi` are already in lower case!  Why are we adding an unneeded `LOWER` to the right side of our `LIKE` operator?

Good eye!  You indeed **don't** need that second `LOWER`, but we want you to get in the habit of doing the same thing on both sides of a text comparison, so we overdid it and added `LOWER` to both sides even though only one side really needs it.

</div>

### REGEXP_LIKE and Regular Expressions

**Regular expression functions** are a class of function that utilize [regular expressions](https://en.wikipedia.org/wiki/Regular_expression), including [metacharacters](https://en.wikipedia.org/wiki/Regular_expression#POSIX_basic_and_extended), to perform some kind of pattern matching on text data.  

A regular expression (or "regex", which you can pronounce either with "reg" rhyming with "beg" or "reg" rhyming with "wedge") is a coded description of a pattern, such as the pattern for a phone number in the United States.  

You might describe what an American phone number looks like written out by describing it as follows:

* Maybe a '+1' for the country code, then 
* Optionally a space or some other separator like a dash or period or open parenthesis, then 
* Three digits for the area code, 
* Another optional space or separator (but this time it could be a closed parenthesis, not an open one), 
* Three more digits, 
* Another optional space or separator, and then 
* The last four digits.  

In a regular expression, we could write that like this:

```
(?:\+1)?[\s\(\-\.]?\d{3}[\s\)\-\.]?\d{3}[\s\-\.]?\d{4}
```

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Regular expressions can look intimidating, but learning regex can be a powerful way to find text needles in a haystack, helping you pull out useful text from clinical notes, Python code you've written, a pile of social media posts compiled for research, or other text.  If you'd like to learn regex, we suggest checking out our modules [Demystifying Regular Expressions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_regular_expressions/demystifying_regular_expressions.md#1) or [Regular Expressions Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/regular_expressions_basics/regular_expressions_basics.md#1) to get started!

You don't need to memorize the information we share here about regular exprssions.  In our regex quiz question, we provide you with the regular expression you need!  Our goal is to let you see and work with these powerful tools in a supported way, so they're less scary when you run across them later.

</div>

Regex can be thought of as a supercharged version of the the `LIKE` operator's "wildcard" characters.

The most common set of regular expression metacharacters are listed below.

|Metacharacter|Description|
|:---|:---|
|^|Matches the starting position within the string.|
|\$|Matches the ending position within the string.|
|.|Matches any single character (similar to the `_` wildcard in a `LIKE` statement).|
|*|Matches 0 or more occurrences of the preceding character.|
|\||This character (known as the "choice operator") can be used to delimit multiple match patterns, and will provide a match on either the expression before or the expression after it is listed in your search string.|

To experiment with regular expressions and learn more about them, we recommend using a regular expression tester or checker online, like [regular expressions 101](https://regex101.com).   A website like that will give you a lot of instant feedback and practice to help you understand regex.  We teach more about regular expression checkers in our [Demystifying Regular Expressions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_regular_expressions/demystifying_regular_expressions.md#1) module.

In the SQL `REGEXP_LIKE()` function, you have to give two arguments or parameters.  The first argument is the string SQL should look at (normally, a SQL column), and the second argument is the pattern it should look for, to see if there's a match (this is what's written in regex code). The example below uses the `REGEXP_LIKE()` function to filter on records where the `allergies.description` field contains either the string "nu" or "fi".  

```sql
SELECT DISTINCT allergies.description
FROM alasql.allergies
WHERE
  REGEXP_LIKE(LOWER(allergies.description), LOWER("nu|fi"))
```
@AlaSQL.eval("#dataTable6a")

<table id="dataTable6a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_allergies

</div>

As you can see from even just this simple example, regular expression functions can be much more useful & dynamic than the `LIKE` operator for filtering on complex text based data.

### Quiz: CASE, LIKE, and REGEXP_LIKE

In this quiz, we have some scenarios for you to consider as a researcher.  If you create the correct SQL query, you'll get the corresponding quiz answer (which appears below the code box) easily!  There is one question each for `CASE`, `LIKE`, and `REGEXP_LIKE`.

You're studying attitudes about smoking and will issue a survey in phases.  Phase 1 will go out to residents of Plymouth County, Phase 2 will go out to residents of Essex County and Phase 3 will go out to Barnstable County.  Finish the following query such that you get the patient name, county, and a new column called `phase`.  Then scroll down to answer a simple question.  Stuck?  No worries -- scroll ahead to where the question appears, and if you click the "check mark" button after the question, you'll see the code that we used to answer the question.

```sql
SELECT
  patients.first
  ,patients.last
  ,patients.county
  ,CASE
    WHEN      THEN "Phase 1"
    WHEN      THEN "Phase 2"
    WHEN      THEN "Phase 3"
    ELSE NULL
  END
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable7a")

<table id="dataTable7a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

How many patients are in the third phase of surveys?

[[ ]] 0
[[ ]] 1
[[X]] 2
[[ ]] 3
***************

<div class = "answer" style = "width: 100%">

This is the query we used to get the answer:

```sql
SELECT
  patients.first
  ,patients.last
  ,patients.county
  ,CASE
    WHEN patients.county = "Plymouth County" THEN "Phase 1"
    WHEN patients.county = "Essex County" THEN "Phase 2"
    WHEN patients.county = "Barnstable County" THEN "Phase 3"
    ELSE NULL
  END AS phase
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable7b")

<table id="dataTable7b" border="1"></table><br>

</div>

*********

You'd like to research patients born in the 1970s (so any year starting 197_ would work).  Use a `LIKE` statement to enrich the query below and find the patient set you care about.  Below the code box, there's a question.  Stuck?  No worries -- scroll ahead to where the question appears, and if you click the "check mark" button after the question, you'll see the code that we used to answer the question.

```sql
SELECT
  patients.id
  ,patients.birthdate
FROM alasql.patients;
```
@AlaSQL.eval("#dataTable7c")

<table id="dataTable7c" border="1"></table><br>

Which of these years are represented in your query results?

[[ ]] 1970
[[X]] 1971
[[ ]] 1972
[[X]] 1973
[[X]] 1974
[[ ]] 1975
***************

<div class = "answer" style = "width: 100%">

This is the query we used to get the answer:

```
SELECT
  patients.id
  ,patients.birthdate
FROM alasql.patients
WHERE patients.birthdate LIKE "197%"
```
@AlaSQL.eval("#dataTable7d")

<table id="dataTable7d" border="1"></table><br>


</div>

**************

You're doing research involving patients who live in multi-tenant housing like apartment buildings or long term hotels.  You know that sometimes people use "apartment", other times "apt", sometimes "unit", or "suite", or "room", so to search for all of these might be tough.  What you want to try is looking for addresses where there's some number listed **after** the part of the string that's composed only of letters and spaces.  So, "123 Apple Street" wouldn't match, but "123 Apple Street, Apt. 10" would.

In regex, "one or more lower case letters or spaces, in any combination" is written `[a-z\s]+`, and "one or more digits" is written `\d+`.  Use that information to complete the following code, to pull out patient information you might be interested in.  

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

We know this is a tricky question, because regular expressions are hard.  Click on the light bulb after the answer choices to ask for a hint if you need it!

As in the previous cases, if you get stuck, just scroll down and hit the "check mark" button after the question.

</div>

```sql
SELECT
  patients.id
  ,patients.birthdate
  ,patients.address
FROM alasql.patients
WHERE REGEXP_LIKE();
```
@AlaSQL.eval("#dataTable7e")

<table id="dataTable7e" border="1"></table><br>

Which of the following is an address that appears in the output of your query?  Select all that apply! 

[[ ]] 119 Apple Valley Road Unit 7
[[X]] 958 Robel Run Unit 83
[[X]] 604 Sipes Divide Unit 0
[[ ]] 82 Marriott Way Room 1153
[[?]] Hint: The regular expression for the address pattern is `[a-z\s]+\d+`.  You'll want to put that in quotes within your `REGEXP_LIKE` clause!
***************

<div class = "answer" style = "width: 100%">

This is the query we used to get the answer:

```
SELECT
  patients.id
  ,patients.birthdate
  ,patients.address
FROM alasql.patients
WHERE REGEXP_LIKE(LOWER(patients.address), "[a-z\s]+\d+");
```
@AlaSQL.eval("#dataTable7f")

<table id="dataTable7f" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

</div>

**************

## Aggregate Functions

**Aggregate functions** can be used to get a single value related the values for multiple rows of data in some meaningful way.  This aggregation could be a numerical statistic, like the sum or standard deviation of a number of rows, or it could pull out a special value, like the minimum or maximum value (this works as well for strings, in which case it would be the first or last value in alphabetical order). There are many other possibilities as well, like giving a count of rows or pulling a value at random from the rows.

See the table below for a list of the most commonly used aggregate functions:

|Function|Description|
|:---|:---|
|`COUNT()`|Returns the count of the number of non-null values among the column(s)/rows provided as input.|
|`SUM()`|Returns the summation of all values from a column provided as input.|
|`MIN()`|Returns the minimum value from a column provided as input.|
|`MAX()`|Returns the maximum value from a column provided as input.|
|`AVG()`|Returns the numerical mean of all values from a column provided as input.|

<div class = "important">
If you just want to count how many rows there are, use `COUNT(*)`.  You can use a specific column, instead, if you wish, like `COUNT(birthdate)`, but if you do that, a missing birthdate will mean the count is lower than the number of rows.
</div>

The below table utilizes each of these aggregate functions to analyze the last name (`last`) column from the `patient` table:

```sql
SELECT
    COUNT(patients.last) AS lon_count
    ,MIN(patients.last) AS min_lon
    ,MAX(patients.last) AS max_lon
FROM alasql.patients
```
@AlaSQL.eval("#dataTable8a")

<table id="dataTable8a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

Aggregation by itself is somewhat limited, so we often use aggregation in partnership with `GROUP BY`, which we'll look at next.

### GROUP BY Clause

Often, you are interested in statistics by group, such as the average BMI for men and for women, or the standard deviation of reading test scores in teens with ADHD, depression, neither condition, or both conditions.

The `GROUP BY` clause is used to group column results into only the unique/distinct values among them, and is used in combination with aggregate functions to generate summary statistics about the larger dataset that was "grouped" (i.e. "collapsed") by `GROUP BY`.

The code block below shows an example of using the `GROUP BY` clause to summarize some simple information from the `patients` table.


```sql
SELECT
    patients.sex
    ,COUNT(*) AS pat_count
    ,MIN(birthdate) AS earliest_birthdate
    ,MAX(birthdate) AS latest_birthdate
FROM alasql.patients
GROUP BY
    patients.sex
```
@AlaSQL.eval("#dataTable9a")

<table id="dataTable9a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

`GROUP BY` aggregations like the one above can be confusing and frustrating for new SQL users, because you have to remember that an aggregation returns **one and only one** value for the entire group of rows.  This means you **cannot** ask for something in your `SELECT` clause that could give more than one value for the  group.  You can include aggregate functions (they by definition give you one and only one value for the group) and you can include what you grouped by (because each member of the group is guaranteed to have the same value), but you can't add anything else.  For example, we couldn't add `race` in the `SELECT` statement above without also adding it to the GROUP BY clause, because each group in the existing GROUP BY (i.e. the group `sex` = 'F' and the group `sex` = 'M') could potentially have more than one value for `race` in the data.

```sql
SELECT
    patients.sex
    ,patients.race
    ,COUNT(*) AS pat_count
    ,MIN(birthdate) AS earliest_birthdate
    ,MAX(birthdate) AS latest_birthdate
FROM alasql.patients
GROUP BY
    patients.sex
```
@AlaSQL.eval("#dataTable9b")

<table id="dataTable9b" border="1"></table><br>

<div class = "warning">
While AlaSQL gives up and just gives you empty data for `race` in the example above, the SQL dialects you'll use in the real world will probably give you an error that is something like `Error: Column is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.`  Remember, when you're aggregating, you can **only** add things to your `SELECT` statement that are **guaranteed** to have **one and only one value** per group of rows.  That means (when using a `GROUP BY` in your query) you can only use items in your `SELECT` statement that are either: 1) columns that are also referenced in your `GROUP BY`, or 2) functions that are aggregate functions, like `COUNT()`.

</div>

### HAVING Clause

The `HAVING` clause can be used to filter your result set on the value of an aggregate function.  It works similarly to a `WHERE` clause, but the two are not interchangable.  This is another common error people who are new to SQL often encounter -- mixing up `WHERE` and `HAVING`.

In terms of placement in your query, the `HAVING` clause can be placed directly after your `GROUP BY` statement, and before your `ORDER BY` statement (if applicable).

The example below summarizes patients by grouping them by `race` and giving the earliest and latest birthdate per group.  Then it uses the `HAVING` clause to only return the race groups with more than 5 members, and then returns a results sorted in order by `earliest_birthdate`.

Try commenting out (use `--` at the start of the line) the `ORDER BY` clause to see what changes in the results.  Then do the same for the `HAVING` clause.

```sql
SELECT
    patients.race
    ,COUNT(*) AS pat_count
    ,MIN(birthdate) AS earliest_birthdate
    ,MAX(birthdate) AS latest_birthdate
FROM alasql.patients
GROUP BY
    patients.race
HAVING COUNT(*) >= 5
ORDER BY earliest_birthdate;
```
@AlaSQL.eval("#dataTable10a")

<table id="dataTable10a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

<div class = "warning">

SQL can be a bit tricky, because even though you've added an alias to `COUNT(*)` (you're calling it `pat_count` in the query above), that alias isn't available to SQL at the time it's parsing the `HAVING` clause.  To see what we mean, try replacing the `HAVING` clause above with `HAVING pat_count >= 5`.  

But `ORDER BY` is the last thing done by SQL, after it has already applied aliases, so you **can** use the `earliest_birthdate` alias in your `ORDER BY` clause.  Tricky, we know!

</div>

 The `HAVING` clause is also a great tool to use for determining which columns in your tables are potential **primary keys**. Primary keys are columns that have a unique value for each row of data, with no repeating values.

Try running the query below, which checks to see if there are any repeated patient ids:

```sql
SELECT
    patients.id
    ,COUNT(*) AS pat_count
FROM alasql.patients
GROUP BY
    patients.id
HAVING COUNT(*) > 1;
```
@AlaSQL.eval("#dataTable10b")

<table id="dataTable10b" border="1"></table><br>

### Quiz: Aggregate functions, GROUP BY, and HAVING

In this quiz, we're going to challenge you to create a query from scratch using aggregate functions, and then quiz you about the results of that query.

Please create a query below that queries `alasql.patients` and gives the patient population of each city (`patients.city`) which has more than one patient living there.  Give the results in an alphabetized list.  Your results should start like the table below.  Stuck?  No worries -- scroll ahead to where the question appears, and if you click the "check mark" button after the question, you'll see the code that we used to answer the question.

<!-- data-type="none" -->
| city | patient_population |
| ---- | ---- |
| Boston | 2 |
| ...    | ... |


```sql
-- Enter your query here!
```
@AlaSQL.eval("#dataTable11a")

<table id="dataTable11a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

What's the third row of results?

[[X]] Everett, with a `patient_population` of 2
[[ ]] Greenbrier, with a `patient_population` of 3
[[ ]] Falls Bridge, with a `patient_population` of 2
[[ ]] Maryknoll, with a `patient_population` of 4
***************

<div class = "answer" style = "width: 100%;">

This is the query we used to get the answer:

```sql
SELECT
    patients.city
    ,COUNT(*) AS patient_population
FROM alasql.patients
GROUP BY
    patients.city
HAVING COUNT(*) > 1
ORDER BY city;
```
@AlaSQL.eval("#dataTable11b")

<table id="dataTable11b" border="1"></table><br>

</div>

**************

## Sub Queries

A **sub query** (or subquery or sub-query) is essentially a nested SQL query that is referenced inside of a larger SQL query.

Sub queries can appear in the `FROM` section of your `SELECT` statement where you'd ordinarily give a table name.  The sub query is enclosed by parentheses, followed by an alias name that you would like to use to reference it later on in your query.  

Let's say we wanted to consider a subset of patients, Latina women (in this dataset, "hispanic" `ethnicity` and "F" `sex`) and wanted to get their ids and race and classify their `birth_status` as either born in Massachusetts, not born in Massachusetts, or with a birth place that was not listed (based on the contents of the `birthplace` field).  Instead of tackling all this at once, we could use a subquery to make the tasks a bit more separate and easy to understand.

For instance, we could start with just a simple query:

```sql
SELECT *
FROM alasql.patients
WHERE sex = 'F' AND ethnicity = 'hispanic'
```
@AlaSQL.eval("#dataTable12a")

<table id="dataTable12a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

Then we could use that as a sub query, and do our `birthplace` query just on that set of results.  Note that we're going to give our sub query a name (`latina_pop`) and our main query has to use that name to refer to that subset of results it's querying on!

```sql
SELECT
  latina_pop.id  -- referencing the name we will give to the sub query
  ,latina_pop.race
  ,CASE
     WHEN LOWER(latina_pop.birthplace) LIKE '%massachusetts%' THEN 'Born in MA'
     WHEN latina_pop.birthplace IS NULL THEN 'Birthplace Unknown'
     ELSE 'Not born in MA'
   END AS birth_status
FROM
(SELECT *
FROM alasql.patients
WHERE
  sex = 'F' AND
  ethnicity = 'hispanic') AS latina_pop -- note that we've named this!
```
@AlaSQL.eval("#dataTable12b")

<table id="dataTable12b" border="1"></table><br>


### WITH Statement

The `WITH` statement can be used to create a sort of "detached" sub query (you might hear people say "temporary table" as well) that will be created **before** your primary `SELECT` statement runs.

Let's revise the previous example using a `WITH` statement:

```sql
WITH latina_pop AS
(SELECT *
FROM alasql.patients
WHERE
  sex = 'F' AND
  ethnicity = 'hispanic')

SELECT
  latina_pop.id
  ,latina_pop.race
  ,CASE
     WHEN LOWER(latina_pop.birthplace) LIKE '%massachusetts%' THEN 'Born in MA'
     WHEN latina_pop.birthplace IS NULL THEN 'Birthplace Unknown'
     ELSE 'Not born in MA'
   END AS birth_status
FROM latina_pop
```
@AlaSQL.eval("#dataTable13a")

<table id="dataTable13a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

This approach, using `WITH` to move the sub query to before the main query, is often used to increase code readability, but can also be used to increase query performance in certain situations.

### Quiz: Sub Queries

There are three problems with the SQL code below.  Correct all three and run the code successfully and you should be able to answer the quiz question.  Below the code box, there's a question.  If you can't find all the errors, scroll ahead to where the question appears, and if you click the "check mark" button after the question, you'll see the code that we used!

```sql
WITH generations (
SELECT
  patients.id
  ,patients.sex
  ,patients.race
  ,CASE
    WHEN patients.birthdate LIKE "194%" THEN "boomer"
    WHEN patients.birthdate LIKE "195%" THEN "boomer"
    WHEN patients.birthdate LIKE "198%" THEN "millenial"
    WHEN patients.birthdate LIKE "199%" THEN "millenial"
    ELSE "other"
   END AS age_group
FROM alasql.generations)

SELECT *
FROM generation
```
@AlaSQL.eval("#dataTable14a")

<table id="dataTable14a" border="1"></table><br>

<div style = "display:none;">

@AlaSQL.buildTable_patients

</div>

What are the sex, race, and age group of the patient with id 03963166-b49f-4440-a80d-30abb90b4a78?

[[ ]] F, black, millenial
[[ ]] M, other, other
[[X]] M, white, other
[[ ]] F, white, boomer
***************

<div class = "answer" style = "width: 100%;">

This is the query we used to get the answer:

```sql
WITH generations AS (
SELECT
  patients.id
  ,patients.sex
  ,patients.race
  ,CASE
    WHEN patients.birthdate LIKE "194%" THEN "boomer"
    WHEN patients.birthdate LIKE "195%" THEN "boomer"
    WHEN patients.birthdate LIKE "198%" THEN "millenial"
    WHEN patients.birthdate LIKE "199%" THEN "millenial"
    ELSE "other"
   END AS age_group
FROM alasql.patients)

SELECT *
FROM generations;
```
@AlaSQL.eval("#dataTable14b")

<table id="dataTable14b" border="1"></table><br>

</div>

**************



## Additional Resources

* Khan Academy's [Introduction to SQL](https://www.khanacademy.org/computing/computer-programming/sql) is high quality and easy to learn from.  There's a section called "More advanced SQL queries" you might find useful.

* [regular expressions 101](https://regex101.com/) is extremely helpful in practicing regex skills, whether that's for use in SQL or elsewhere.

* To read more about the basic types of **operators** available for use in a SQL query, check out [tutorialspoint.com](https://www.tutorialspoint.com/sql/sql-operators.htm) for some helpful documentation.


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22SQL+Intermediate%22&version=1.0.3)!
