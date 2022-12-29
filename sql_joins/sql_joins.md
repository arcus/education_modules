<!--
author:   Peter Camacho
email:    camachop@chop.edu
version:  1.0.1
module_template_version: 2.0.0
language: en
narrator: US English Male
title: SQL Joins
comment: Learn to extract data from more than one SQL table using JOIN commands in SQL.
long_description: Usually, data in a SQL database is "normalized", which means reorganized into separate tables that reduce data duplication.  This means you will often have to bring data together from two or more tables into a single dataset.  To do this, you need to learn how JOIN commands work and how to avoid common pitfalls in SQL JOINs.  This module will help you do just that.
estimated_time: 1 hour

@learning_objectives  
After completion of this module, learners will be able to:

- Explain why SQL data is organized into multiple tables instead of including all pertinent data in a single table
- Describe the various "shapes" of SQL JOIN: left, right, inner, outer, and full
- Write SQL code to correctly specify a JOIN
- Explain what a "Cartesian" JOIN is and why it's problematic
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


-->

# SQL Joins

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**  A moderate level of experience writing basic SQL code (SELECT, FROM, WHERE) and intermediate SQL code (CASE, LIKE, GROUP BY, WITH, etc.) on single tables is expected in this module. If you need to develop basic SQL fluency we recommend our module [SQL Basics](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_basics/sql_basics.md).  For more intermediate topics, we suggest our module [SQL Intermediate](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/sql_intermediate/sql_intermediate.md).

**Learning Objectives**

@learning_objectives

</div>

## SQL Joins

Most SQL queries require something more complex than referencing data from a single table. This is where SQL JOIN functionality comes into play.

SQL JOINs are used to combine rows from 2 (or more) tables, based on some set of columns they have in common.  For example, consider the case where you have data about a multi-site study's research subjects. One table holds depression scores for patients and a different table holds patient addresses.  Your hypothesis is that people who live in certain zip codes have higher rates of depression.

To see if your hypothesis has evidence to back it, you need to combine data, taking the patient ID and depression score from one table, and the patient ID and zip code from another table, and combining them.  

Maybe your source tables look something like the tables below:

**Table 1: `depression_scale`**

<div style = "font-size: 0.7em;">
<!-- data-type="none" -->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |
</div>

**Table 2: `subject_address`**

<div style = "font-size: 0.7em;">
<!-- data-type="none" -->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 11234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | NULL    |
| 11234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 93452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | NULL   |
</div>

What you end up with after your successful JOIN will be a single table of results that might just have three columns: `subj_id`, `dep_total`, and `zip`.  That way you can look at any relationship between depression inventory scale and zip code.

You may be asking yourself, "Why not just put all the information together in one table to start with?". After all, getting one row per subject is how we usually prepare to apply statistical tests. If we could just **start** with one row per subject in SQL, we'd be ready to jump into the science and not have so much data preparation work. 

The reason why this usually doesn't happen in a SQL database, and you instead see lots of different tables that you have to join together is because of a concept known as **normalization**.  To explain normalization, we'll first explain **one-to-many** data relationships.

## One-to-many

Data often has one-to-many relationships. What does ***one-to-many*** mean? Consider two use cases, a hospital and a retail website.  Each organization has one-to-many data relationships:

**Hospital one-to-many examples**

* One patient has multiple encounters on different dates
* One encounter may include multiple orders for different procedures and medications
* One medication order can give rise to multiple medication administrations

**Retail website one-to-many examples**

* One customer may have several associated addresses for shipping, billing, or both
* One customer will probably have multiple orders 
* Each order will have one or many associated items

One-to-many data relationships (one X is related to more than one Y) can be very hard to accommodate in a single table with all the data.  Imagine having a table of order information from an online website, in which a single row contained every item included in that order. 

It would be impossible to know ahead of time how many columns would be needed.  What if we provided enough columns for 100 items in an order to start?  Then, maybe someone orders 110 items.  What do we do?  Also, most orders are much smaller, which means we have many empty cells with no data in them.  It's not an efficient way to store data.  

It also means that if we have to update an item name (maybe there's a spelling error), we'd have to look in many rows to make that correction.  That kind of "find and replace" is time consuming and error-prone.  

That brings us to the idea of ***normalization***, or organizing data to reduce duplication and break down complex data into multiple tables.

## Normalization

When data is normalized, we separate data into tables representing different concepts, like "address", "order", "procedure", "medication", "item", etc., and give each of these concept an id number to identify it.  To show why this is helpful, let's use an example.

Which of the following is more efficient to correct, if we want to change "orane juice" to "orange juice"? Is it easier to correct with the data stored in one table, or with the data in two tables, where items are given an id number?

**One Table Option**

<div style = "max-width: 100%">
**`order_and_items`**

<!-- data-type="none" -->
| order_num   | item_1   | item_2  | ...  | item_50  |
| :--------- | :--------- | :--------- | :--------- | :--------- |
| 23125    | orane juice     | pistachios     | ...    | NULL    |
| 41320    | peanut butter    | plain bagels     | ...    | orane juice    |
| ... hundreds more rows ... | ... | ... | ...| ... |
| 53011    | napkins    | distilled water     | ...    | NULL    |
| 14123    | pistachios    | orane juice     | ...    | peanut butter    |
</div>

**Two Table Option**

**`items`**
<!-- data-type="none" -->
| item_id   | item_name  |
| :--------- | :--------- |
| 15 | distilled water |
| 178 | napkins |
| 210 | orane juice |
| 97 | peanut butter |
| 108 | pistachios  |
| 233 | plain bagels  |
| ...| ... additional items ...|

**`orders`**
<!-- data-type="none" -->
| order_id   | item_id |
| :--------- | :--------- |
| 23125 | 210 |
| 23125 | 108 |
| 41320 | 97 |
| 41320 | 233 |
| 41320 | 210  |
| 53011 | 178 |
| 53011 | 15 |
| 14123 | 108 |
| 14123 | 210 |
| 14123 | 97 |
| ...| ... additional order - item pairs |


Therefore, data in SQL databases are fragmented in a process called **normalization**, to help reduce needless repetition and improve performance.

Let's consider the data we looked at in the last section, the two tables related to a mental health research study.  To remind you, this is what that data looked like: 

**Table 1: depression_scale**

<!-- data-type="none" -->
| subj_id  | date  | dep_q1  | dep_q2   | dep_q3  | dep_q4  | dep_total   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 01234   | 2021-05-15   | 3    | 3  | 2    | 4    | 12    |
| 86234   | 2021-06-01   | 4    | 4  | 3    | 4    | 15    |
| 32660   | 2021-06-10   | 1    | 1  | 2    | 1    | 5   |
| 86234   | 2022-01-13   | 2    | 2  | 1    | 3    | 8    |
| 41356   | 2022-02-10   | 1    | 3  | 2    | 3    | 10   |

**Table 2: pat_address**

<!-- data-type="none" -->
| subj_id  | street_address  | city  | state   | zip  | date_start  | date_end   |
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| 01234   | 123 Main Street   | Smithtown    | PA  | 19000    | 2022-01-01   | NULL    |
| 01234   | 123 Oak Lane   | Old Towne    | PA  | 18000   | 2000-01-01    | 2021-12-31    |
| 03452   | 123 Green Blvd  | Kirby    | TN  | 37000    | 2020-05-01    | NULL   |

Notice the one-to-many aspects of this data.  The subject with id 86234 has two different administrations of the depression inventory, on different dates.  The subject with id 01234 has two different addresses for two different date ranges.

Imagining how to consolidate this data into one single table with one row per subject is challenging.  Would we provide two sets of columns for addresses?  Maybe the column names would be `street_address_1`, `city_1`, etc., and `street_address_2`, `city_2`, and so on.  But this is a longitudinal study and people might move 3, 5, even 10 times!  The same problem emerges with multiple administrations of the depression inventory.  And it gets worse, because we also have other data about subjects that we'd need to include, like their demographic information (date of birth, sex, race, etc.).  

## Quiz: Why is SQL Data Fragmented?

Why is data normalized (carefully fragmented to reduce repetition and inefficiency) in SQL?  Select all the correct answers.

[[ ]] SQL has a limit on number of columns permitted in a table, and must break up data in order to keep tables smaller
[[X]] Because data is often one-to-many, storing data in a single table is inefficient
[[X]] Normalizing data makes correcting or changing data simpler and less prone to error
[[ ]] Normalization is a holdover from when most databases were business-related, but it not necessary in biomedical research
[[?]] There are multiple correct answers!
*********

<div class = "answer">

The reason for normalization isn't that SQL lacks the capacity for very wide tables with lots of columns.  Rather, the kind of rich data that is stored in SQL databases simply isn't right for storage in a single table.  There are many one-to-many relationships in data, and this means that using multiple tables, one for each kind of concept (like "address" or "order" or "encounter") makes sense.  There are also lots of repetition in data -- multiple patients might live at the same address, or receive the same medication.  Multiple orders each contain the same product.  This repetition means that it's much easier to correct or change data when a normalized model is used.  Instead of correcting a product name 9,241 times, once for each order that product appears on, we correct it once, in the "product" table.

</div>

***********


## Learning to Ask the Right Question

But you want the data in a flattened format, just one row per subject. You mention this, and there’s a bit of difficulty in getting you exactly what you want. Why is this the case?

Let’s recall, first, that human-centric data in particular is very messy. People have varying vital signs measured at different times, may have completed questionnaires more than once, take anywhere from one to dozens of medications, etc. It’s hard to come up with a perfect schema (set of columns / shape of dataset) that fits all cases. That’s why data professionals will often give you raw data in various datasets, instead of combining them into one. The choice of how to combine the data is really up to the subject matter expert (you!), and there’s no single right way to do it.

For example, let’s take the case of combining surgical patients and their antibiotic use (note, I’m not a clinician, forgive my terrible prescribing practices).

We have a (very simplified) surgical procedure table that starts like this:

PT	PROC_DATE
1	2016-03-04
2	2017-08-17
3	2015-12-12
4	2018-01-30
5	2016-10-25
And an antibiotic use table (again, very simplified) like this:

PT	ABX_ACTION_DATE	ABX_NAME
1	2016-03-04	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
1	2016-03-05	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
1	2016-03-06	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
2	2017-08-18	AMPICILLIN-SULBACTAM 30 MG AMP/ML (NSS) INJECTION CUSTOM
2	2017-08-18	AZITHROMYCIN 250 MG OR TABS
4	2018-03-21	METRONIDAZOLE 250 MG OR TABS
What do we notice? First of all, it seems that the surgical procedure table has one row per patient. But is that really true? Is it possible that patients appear twice because of different procedures on different dates? Or because of multiple procedures on the same date? Or because a procedure spanned midnight? We have to check our assumptions (which you can do easily in a statistical programming environment like R).

What else do we notice? The antibiotic use table has multiple rows for some patients, missing rows for others, and single row for one patient. One patient received a single antibiotic over several days, another patient had two different antibiotics on the same day, and a third patient had an antibiotic prescribed well past the date of surgery – is this relevant?

Generally, when we combine data from multiple tables, linking by some common field (like the PT column), we get a Cartesian product, such that each combination of tables grows the number of rows, geometrically (i.e. by multiplication). So since PT 1 has one row in the surgical procedure table and 3 rows in the antibiotics table, PT 1 would have 1 X 3, or 3, rows in the result table. This is what that looks like:

PT	PROC_DATE	ABX_ACTION_DATE	ABX_NAME
1	2016-03-04	2016-03-04	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
1	2016-03-04	2016-03-05	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
1	2016-03-04	2016-03-06	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
2	2017-08-17	2017-08-18	AMPICILLIN-SULBACTAM 30 MG AMP/ML (NSS) INJECTION CUSTOM
2	2017-08-17	2017-08-18	AZITHROMYCIN 250 MG OR TABS
3	2015-12-12	 	 
4	2018-01-30	2018-03-21	METRONIDAZOLE 250 MG OR TABS
5	2016-10-25	 	 
Often that combinatorial approach may be exactly what you want (say, if you were predicting how long after surgery various antibiotics tended to be prescribed). But in this case, let’s assume it’s not.

If you said to your data wrangler, “can you flatten this”, how could they cram all of that multi-row data related to antibiotics into a single row per patient?

One way would be to make each repetition in the antibiotics table its own set of columns:

PT	PROC_DATE	ABX_ACTION_DATE_1	ABX_NAME_1	ABX_ACTION_DATE_2	ABX_NAME_2	ABX_ACTION_DATE_3	ABX_NAME_3
1	2016-03-04	2016-03-04	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS	2016-03-05	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS	2016-03-06	DOXYCYCLINE MONOHYDRATE 100 MG OR TABS
2	2017-08-17	2017-08-18	AMPICILLIN-SULBACTAM 30 MG AMP/ML (NSS) INJECTION CUSTOM	2017-08-18	AZITHROMYCIN 250 MG OR TABS	 	 
3	2015-12-12	 	 	 	 	 	 
4	2018-01-30	2018-03-21	METRONIDAZOLE 250 MG OR TABS	 	 	 	 
5	2016-10-25	 	 	 	 	 	 
The evident problem with this is that it:

causes huge growth in the number of columns (imagine if there were more details in the antibiotics table, and one patient had 17 separate antibiotics administrations!)
may make statistical analysis difficult because of sparsity, aka missingness (most patients only have 1-2 administrations, but the most highly-medicated patient has 17, so that means everyone has to have 17 sets of antibiotics data, most of which are empty)
So what other options are there?

I always suggest to researchers that they hone their criteria and data definitions. So, instead of:

“Can you give me a list of orthopedic surgical patients and the dates of their surgeries for the past three years?”
You might want to consider:

“Can you give me a list of orthopedic surgical patients for the past three years who have had only one orthopedic surgery, and the date that surgery ended?” (Handles repeats and surgeries spanning 2 calendar days)
Instead of saying:

“I want the antibiotics they were prescribed post-surgery.”
You might want to ask, instead:

“Please also give me any antibiotics prescribed to the patient within 2 weeks of the date of the end of surgery.”
When you’re thinking about integrating the procedure table and the antibiotics table, don’t just say “I want antibiotics in columns, too”. Instead, you might say one or more of the following (to yourself, or to your data analyst):

“I want to see the various possible classes of antibiotics as columns, with 0/1 coding for each patient, indicating whether they received this class in the two weeks post-surgery.” (benefit: sets the max number of columns to the number of antibiotic classes)
“I want to see the total days of post-surgical antibiotic treatment as a column.” (benefit: will be one column only)
“I want to see the number of distinct antibiotics used post-surgically as a column.” (benefit: will be one column only)
“I want to see the number of days elapsed between surgery and first antibiotic rx as a column.” (benefit: will be one column only)
Think about what will help you in statistical modeling (or whatever your goal is) – what seems predictive? What data is needed to support or refute your hypothesis? If missing data will be a problem, how will you design your dataset so that you reduce or eliminate missing data?

Note that it’s much easier to do things like counts and classifications (we could call this kind of combination of multiple rows of data “aggregation”) on the raw data. This is why when data is extracted for you, it’s generally given to you without combining with other datasets, so that you can make the decisions on how to do that, based on your specific questions.


## Additional Resources


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22SQL+Joins%22)!
