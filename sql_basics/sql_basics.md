<!--
author:   Peter Camacho
email:    camachop@chop.edu
version:  1.0.0
module_template_version: 2.0.0
language: en
narrator: US English Male
title: SQL Basics
comment:  SQL is a relational database solution that has been around for decades.  Learn how to do basic SQL queries on single tables, hands on!
long_description: Do you want to learn basic SQL either to understand concepts or prepare for access to a real database?  This module will give you hands on experience with simple queries using keywords including SELECT, WHERE, FROM, DISTINCT, and AS.  This module is appropriate for people who have little or no experience in SQL and are ready to practice with real queries.
estimated_time: 40 minutes

@learning_objectives  

After completion of this module, learners will be able to:

- Use SELECT, FROM, and WHERE to do a basic query on a SQL table
- Explain the use of DISTINCT and how it can be useful
- Use ORDER BY to change how query results appear


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
      row$.append($('<td/>').html(cellValue));
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
    myinput=myinput.replace(/;$/, ""); // remove trailing semi-colon
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
    alasql("create table patients (id text,birthdate date,deathdate date,ssn text,drivers text,passport text,prefix text,first text,last text,suffix text,maiden text,marital text,race text,ethnicity text,sex text,birthplace text,address text,city text,state text,county text,zip integer,lat real,lon real);");
    alasql("INSERT INTO patients VALUES ('bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','2000-11-21',null,'999-87-8860','S99917788',null,'Ms.','Cecila','Feil',null,null,null,'white','nonhispanic','F','Nahant  Massachusetts  US','873 Mueller Arcade Unit 96','Ashland','Massachusetts','Middlesex County',null,42.2138985577807,-71.503695110333);");
    alasql("INSERT INTO patients VALUES ('e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','2013-07-02',null,'999-82-6451',null,null,null,'Lorrie','Leannon',null,null,null,'white','nonhispanic','F','Winthrop  Massachusetts  US','813 Casper Street','Peabody','Massachusetts','Essex County',1940,42.4951616189433,-71.0071749067398);");
    alasql("INSERT INTO patients VALUES ('e061409e-4b85-4ec1-b1f7-02677d51f763','1997-09-11',null,'999-32-2366','S99995098','X50396137X','Ms.','Tabetha','OHara',null,null,null,'white','nonhispanic','F','Auburn  Massachusetts  US','1080 Sawayn Gateway Suite 9','Framingham','Massachusetts','Middlesex County',1701,42.3224819015944,-71.4003256055831);");
    alasql("INSERT INTO patients VALUES ('71e13815-55fb-4734-bcac-6079160d82a0','1973-06-02',null,'999-94-8759','S99996780','X23275205X','Mrs.','Laticia','Flatley',null,'Rempel203','M','white','nonhispanic','F','Boston  Massachusetts  US','469 Gerhold Bay Unit 34','Waltham','Massachusetts','Middlesex County',2451,42.4312144913848,-71.2680783842969);");
    alasql("INSERT INTO patients VALUES ('ca3330c5-bbbc-47e7-addb-302f2e069986','2003-06-23',null,'999-44-5854','S99912993',null,null,'Golden','Pollich',null,null,null,'white','nonhispanic','F','Carlisle  Massachusetts  US','792 OKon Byway','Springfield','Massachusetts','Hampden County',1105,42.0930726815877,-72.5803988374441);");
    alasql("INSERT INTO patients VALUES ('24bca5cf-ba55-457f-8e80-49690202443c','1977-06-28',null,'999-31-8026','S99975475','X46617643X','Mr.','Lionel','Fadel',null,null,'M','white','nonhispanic','M','Dighton  Massachusetts  US','1015 Parisian Divide Unit 26','Fairhaven','Massachusetts','Bristol County',null,41.6529893063487,-70.8948756027136);");
    alasql("INSERT INTO patients VALUES ('841095eb-d29f-4492-8f0e-08011321e85d','2017-04-08',null,'999-81-1909',null,null,null,'Carlton','Leffler',null,null,null,'asian','nonhispanic','M','Ipswich  Massachusetts  US','344 Feest Camp Suite 73','Wakefield','Massachusetts','Middlesex County',1880,42.4780284069299,-71.0892699664186);");
    alasql("INSERT INTO patients VALUES ('ee7f6c74-a8ed-4147-b8e2-4879c8657b0f','1950-04-11',null,'999-24-8407','S99984370','X70737069X','Mr.','Kelvin','Powlowski',null,null,'M','white','nonhispanic','M','Fall River  Massachusetts  US','623 Runolfsson Annex Suite 88','Revere','Massachusetts','Suffolk County',2151,42.4674386785624,-71.0070987954362);");
    alasql("INSERT INTO patients VALUES ('ab6a2662-f6d1-4da6-b3ce-3929d68650d7','1971-01-16',null,'999-76-3317','S99978505','X28929072X','Mrs.','Miesha','Wyman',null,'Jacobs452','M','white','nonhispanic','F','Harvard  Massachusetts  US','850 Thiel Road Unit 0','Westfield','Massachusetts','Hampden County',1086,42.0904434489837,-72.7927566478986);");
    alasql("INSERT INTO patients VALUES ('4440ff11-69ec-440b-a2bd-dc1c14105e8e','2001-11-20',null,'999-68-1710','S99968894',null,'Ms.','Ona','Dooley',null,null,null,'white','hispanic','F','Athol  Massachusetts  US','1048 Weimann Throughway','Northborough','Massachusetts','Worcester County',null,42.3661545339449,-71.6515505734496);");
    alasql("INSERT INTO patients VALUES ('1aa71b23-790e-4d22-92da-c689682c8993','1993-05-03',null,'999-84-7590','S99922416','X45217366X','Ms.','Jeannie','VonRueden',null,null,null,'white','nonhispanic','F','Ashburnham  Massachusetts  US','711 Williamson Dale','Ayer','Massachusetts','Middlesex County',null,42.5198988512541,-71.6009012317879);");
    alasql("INSERT INTO patients VALUES ('848e0227-5d5d-4bdf-8603-207cdea72e2a','1949-03-27',null,'999-87-5716','S99971093','X51980015X','Mrs.','Alda','Kris',null,'Satterfield305','M','white','nonhispanic','F','Mansfield  Massachusetts  US','1090 Wiegand Union','Attleboro','Massachusetts','Bristol County',null,41.9326094578451,-71.3272454816091);");
    alasql("INSERT INTO patients VALUES ('eafd1fd3-3778-423a-ba79-4584bd310eb4','2003-07-05',null,'999-39-2345','S99942603',null,null,'Buford','Lynch',null,null,null,'white','nonhispanic','M','Walpole  Massachusetts  US','332 Witting Mission','Malden','Massachusetts','Middlesex County',null,42.4569197038897,-71.0641138577902);");
    alasql("INSERT INTO patients VALUES ('0288abb6-633c-40c3-ba0c-66c7d957727e','1950-11-28',null,'999-18-7195','S99953954','X15598453X','Mrs.','Keva','Shanahan',null,'Reichel38','M','white','nonhispanic','F','Winchendon  Massachusetts  US','169 Witting Orchard Unit 98','Williamstown','Massachusetts','Berkshire County',null,42.7353013466036,-73.1923384461437);");
    alasql("INSERT INTO patients VALUES ('097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','2003-06-18',null,'999-43-8940','S99945945',null,null,'Maribeth','DAmore',null,null,null,'white','hispanic','F','Fall River  Massachusetts  US','238 Mills Hollow','Holyoke','Massachusetts','Hampden County',1040,42.1738356843755,-72.6457553208547);");
    alasql("INSERT INTO patients VALUES ('78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','1993-05-01',null,'999-75-7372','S99974220','X59022582X','Mr.','James','Wyman',null,null,null,'white','nonhispanic','M','Stoughton  Massachusetts  US','702 Stoltenberg Course Apt 16','Attleboro','Massachusetts','Bristol County',2703,41.9406317547512,-71.311136544988);");
    alasql("INSERT INTO patients VALUES ('c05478a7-a4df-4fd3-8d68-60b9452d4781','2010-10-14',null,'999-96-3194',null,null,null,'Brandon','Hagenes',null,null,null,'white','nonhispanic','M','Natick  Massachusetts  US','519 Thiel Annex Apt 55','Pittsfield','Massachusetts','Berkshire County',null,42.4079671056193,-73.3177862656724);");
    alasql("INSERT INTO patients VALUES ('e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','2008-07-16',null,'999-93-5743',null,null,null,'Frances','Schumm',null,null,null,'white','nonhispanic','M','Chelsea  Massachusetts  US','826 Hammes Mission Apt 1','Natick','Massachusetts','Middlesex County',null,42.2584672080661,-71.3444415391516);");
    alasql("INSERT INTO patients VALUES ('8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','2002-03-02',null,'999-93-1045','S99931036',null,'Ms.','Essie','Kutch',null,null,null,'white','nonhispanic','F','Cambridge  Massachusetts  US','219 Gorczany Gateway Unit 71','Chelmsford','Massachusetts','Middlesex County',null,42.5642627698721,-71.3448142130082);");
    alasql("INSERT INTO patients VALUES ('df7c1d66-eac2-49bd-9d12-ee17e8758f68','1979-11-19',null,'999-19-4886','S99963281','X82905419X','Mrs.','Iraida','Oberbrunner',null,'Sporer811','M','white','nonhispanic','F','Hanson  Massachusetts  US','903 Spencer Gate Suite 97','Springfield','Massachusetts','Hampden County',null,42.018977154431,-72.5783835627201);");
    alasql("INSERT INTO patients VALUES ('68878f91-5962-4ef2-83e7-43b8298c1708','1977-11-07',null,'999-40-6743','S99988503','X59484000X','Mr.','Ali','Maggio',null,null,'S','asian','nonhispanic','M','Taunton  Massachusetts  US','448 Rath Glen','Boston','Massachusetts','Suffolk County',2118,42.3425177110989,-71.1548454376564);");
    alasql("INSERT INTO patients VALUES ('1c2aa038-9366-4c7d-9a3e-52cb753a670f','1962-09-13',null,'999-19-8817','S99966954','X83180931X','Mr.','Homero','Carrillo',null,null,'M','white','hispanic','M','Gaudalajara  Jalisco  MX','627 Weissnat Fork','Boston','Massachusetts','Suffolk County',2128,42.3109346386431,-71.0700902117231);");
    alasql("INSERT INTO patients VALUES ('8d202c65-427d-4190-8c28-3aa27e1a9f4c','1986-10-24',null,'999-82-4546','S99932840','X66208297X','Mrs.','Mariam','Bogisich',null,'Hermann103','M','white','nonhispanic','F','Milton  Massachusetts  US','1032 McClure Extension Unit 88','Framingham','Massachusetts','Middlesex County',1701,42.3029088307893,-71.4025310847364);");
    alasql("INSERT INTO patients VALUES ('2a6d1e58-88eb-4be0-b6b4-59a471257c2e','1964-10-10',null,'999-22-8704','S99976805','X66668021X','Ms.','Nikia','Herzog',null,null,'S','white','nonhispanic','F','Wareham  Massachusetts  US','679 Robel Junction Apt 36','Quincy','Massachusetts','Norfolk County',2169,42.2640821758816,-71.0518467413496);");
    alasql("INSERT INTO patients VALUES ('e6ff4bf9-09c2-4976-aa84-cca142207cf8','1998-12-23',null,'999-91-5603','S99952608','X23816401X','Ms.','Corie','Howe',null,null,null,'white','nonhispanic','F','West Boylston  Massachusetts  US','580 Hickle Dam','Brookline','Massachusetts','Norfolk County',2215,42.3312937592791,-71.1672225619312);");
    JSON.stringify(@0);
</script>
@end

@AlaSQL.buildTable_encounters
<script>
    alasql("DROP TABLE IF EXISTS encounters;");
    alasql("create table encounters (id text,start date,stop date,patient text,organization text,provider text,encounterclass text,description text,reasondescription text);");
    alasql("INSERT INTO encounters VALUES ('a61f97fa-70c3-4366-90e1-7c6fdcba5cbb','2002-01-24T20:46:46Z','2002-01-24T21:31:46Z','bf35e4fa-ea4f-40a4-8fe6-1f2f26e0aa45','24cb4eab-6166-3530-bddc-a5a8a14a4fc1','7bd4e666-a82d-3ad1-bc7c-b49eb726577b','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('469fbd8a-ec48-4da9-9165-027144ccf9a0','2014-12-04T23:28:40Z','2014-12-05T00:08:40Z','e3af2463-f4c9-4dbb-a8d2-d6a08c5b1460','d692e283-0833-3201-8e55-4f868a9c0736','f4eb93d1-9187-3cfb-83a4-6d9cd77f7df6','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('022ad487-e41c-43ba-90f3-eb2d6711f4d3','1998-07-19T12:55:35Z','1998-07-19T13:38:35Z','e061409e-4b85-4ec1-b1f7-02677d51f763','465de31f-3098-365c-af70-48a071e1f5aa','0a8a9359-7b33-3256-a068-b5a7d18ebe4b','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('9607667e-4c98-4087-9c59-0fd5b6331078','1974-05-17T10:52:30Z','1974-05-17T11:07:30Z','71e13815-55fb-4734-bcac-6079160d82a0','6f122869-a856-3d65-8db9-099bf4f5bbb8','3180b739-e823-37a0-b307-52a6d67db4a5','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('d8f2b92b-5971-455f-a0b9-99da66d03899','2004-07-03T22:12:27Z','2004-07-03T22:57:27Z','ca3330c5-bbbc-47e7-addb-302f2e069986','60457c13-adb2-3415-82c5-86ab5dab5f93','47cb5349-d261-324a-9109-c888f4a0e966','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('1d475126-f3c0-41c9-a9ed-f4a0c9a955c4','1978-11-04T06:05:02Z','1978-11-04T06:51:02Z','24bca5cf-ba55-457f-8e80-49690202443c','ef6ab57c-ed94-3dbe-9861-812d515918b3','77a7881d-6dd5-32e1-9e18-521a59749572','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('32622f63-734e-4433-8628-942ce1585e6a','2018-03-20T11:48:11Z','2018-03-20T12:36:11Z','841095eb-d29f-4492-8f0e-08011321e85d','d692e283-0833-3201-8e55-4f868a9c0736','f4eb93d1-9187-3cfb-83a4-6d9cd77f7df6','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('0b7d2e65-a9df-4b74-84ed-25feffc23f62','1951-04-21T08:40:57Z','1951-04-21T08:55:57Z','ee7f6c74-a8ed-4147-b8e2-4879c8657b0f','d692e283-0833-3201-8e55-4f868a9c0736','f4eb93d1-9187-3cfb-83a4-6d9cd77f7df6','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('603a0692-9302-459a-84b4-af631dc3aee8','1971-03-07T16:13:43Z','1971-03-07T16:28:43Z','ab6a2662-f6d1-4da6-b3ce-3929d68650d7','ebc3f5c4-6700-34af-8323-85621c313726','eabb2bff-3216-34da-9f29-824dbca901c3','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('38de2a79-6bea-438e-963f-804823c1e32d','2002-05-31T06:08:11Z','2002-05-31T07:01:11Z','4440ff11-69ec-440b-a2bd-dc1c14105e8e','331f4c11-d298-308b-aaa1-d7825b29b57f','8ee28b4a-9018-3065-9f6b-0c9b69de7080','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('228c992b-3877-454c-920d-fa629bb8c5d9','1994-05-12T20:03:59Z','1994-05-12T20:47:59Z','1aa71b23-790e-4d22-92da-c689682c8993','ac8356a5-78f8-3a63-8a1e-59e832fd54e7','f6065151-bf86-330b-a526-ac86b53b440b','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('77427b07-f03b-49bc-9556-d69b4feed7ef','1950-01-07T13:40:23Z','1950-01-07T13:55:23Z','848e0227-5d5d-4bdf-8603-207cdea72e2a','5e765f2b-e908-3888-9fc7-df2cb87beb58','0359f968-d1a6-30eb-b1cc-e6cc0b4d3513','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('36279aee-15ff-48ad-a4a6-8ba334466278','2004-12-06T09:48:16Z','2004-12-06T10:36:16Z','eafd1fd3-3778-423a-ba79-4584bd310eb4','d692e283-0833-3201-8e55-4f868a9c0736','f4eb93d1-9187-3cfb-83a4-6d9cd77f7df6','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('a64c55df-b288-4f78-9996-d2ecf0b65c9d','1952-03-11T04:07:36Z','1952-03-11T04:22:36Z','0288abb6-633c-40c3-ba0c-66c7d957727e','4f3a530e-a2f7-3de0-9a09-c0a70a9ab894','3f15c687-0cfe-3bf2-9e62-34f3c85ff3cb','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('9c3c633f-c33c-426c-b771-b6117ba7d6fc','2004-04-26T14:03:38Z','2004-04-26T14:42:38Z','097079b1-ff8f-4ee0-8ce3-0ea744ecfa21','5d4b9df1-93ae-3bc9-b680-03249990e558','af01a385-31d3-3c77-8fdb-2867fe88df2f','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('7c0482a4-04fc-4cdc-9c2b-ff1f28f704db','1994-06-07T13:13:50Z','1994-06-07T13:57:50Z','78a9a8d6-b3b2-47dc-b4a0-867abec7c78f','5e765f2b-e908-3888-9fc7-df2cb87beb58','0359f968-d1a6-30eb-b1cc-e6cc0b4d3513','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('6dbce8d2-3bb0-4ff9-8e9b-7152ff03cc0c','2011-10-24T09:24:08Z','2011-10-24T10:01:08Z','c05478a7-a4df-4fd3-8d68-60b9452d4781','4f3a530e-a2f7-3de0-9a09-c0a70a9ab894','3f15c687-0cfe-3bf2-9e62-34f3c85ff3cb','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('5e4a49f2-47e7-4b76-9120-276a79f1766f','2009-01-22T22:23:00Z','2009-01-22T23:15:00Z','e188fafe-c1bb-45dc-9627-4ff4e4bc0ec0','465de31f-3098-365c-af70-48a071e1f5aa','0a8a9359-7b33-3256-a068-b5a7d18ebe4b','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('e75460f0-5f5c-4aa2-ab0b-200310a96c63','2003-06-13T09:58:22Z','2003-06-13T10:35:22Z','8db0d104-4c3f-40d3-bcf5-f5eb81b7308f','b0e04623-b02c-3f8b-92ea-943fc4db60da','58b66cc1-2b86-377f-ad77-ad8164388e50','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('a232db22-565f-4559-bb56-edf9021b74b2','1981-01-29T12:47:12Z','1981-01-29T13:33:12Z','df7c1d66-eac2-49bd-9d12-ee17e8758f68','fd328395-ab1d-35c6-a2d0-d05a9a79cf11','1530e81b-106c-32d5-95d5-42a710c92068','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('95099931-0042-4524-b808-dd6b6447fc0e','1978-07-20T13:40:53Z','1978-07-20T14:17:53Z','68878f91-5962-4ef2-83e7-43b8298c1708','69176529-fd1f-3b3f-abce-a0a3626769eb','c9b3c857-2e24-320c-a79a-87b8a60de63c','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('c90b2536-b388-479c-aa7e-3406fe4c2211','1963-07-23T15:56:00Z','1963-07-23T16:11:00Z','1c2aa038-9366-4c7d-9a3e-52cb753a670f','ff9863d3-3fa3-3861-900e-f00148f5d9c2','e49edc61-6ba6-324c-bef7-b65f0e10799f','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('16bc6376-a1cc-4d63-8307-c5d7479dc021','1987-11-30T13:51:47Z','1987-11-30T14:41:47Z','8d202c65-427d-4190-8c28-3aa27e1a9f4c','465de31f-3098-365c-af70-48a071e1f5aa','0a8a9359-7b33-3256-a068-b5a7d18ebe4b','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('f7ff5032-50cc-480e-90ca-848c85d6d014','1965-09-23T13:40:01Z','1965-09-23T13:55:01Z','2a6d1e58-88eb-4be0-b6b4-59a471257c2e','12c9daf5-a29c-36c9-ac55-28972463e566','aa89beb2-7bc6-35fa-83f7-4b32039e84eb','ambulatory','Encounter for problem',null);");
    alasql("INSERT INTO encounters VALUES ('6c760807-a6b7-4af4-8d50-f32325803448','2000-01-03T07:32:25Z','2000-01-03T08:22:25Z','e6ff4bf9-09c2-4976-aa84-cca142207cf8','3d10019f-c88e-3de5-9916-6107b9c0263d','4b04cd2f-3f27-35bc-8069-f4ca6339529f','ambulatory','Encounter for problem',null);");
    JSON.stringify(@0);
</script>
@end

@AlaSQL.buildTable_providers
<script>
    alasql("DROP TABLE IF EXISTS providers;");
    alasql("create table providers (id text,name text,gender text,speciality text,address text,city text,state text,zip text,lat real,lon real);");
    alasql("INSERT INTO providers VALUES ('7bd4e666-a82d-3ad1-bc7c-b49eb726577b','Lonna Dietrich','F','GENERAL PRACTICE','14 PROSPECT STREET','MILFORD','MA','01757',42.158692,-71.521419);");
    alasql("INSERT INTO providers VALUES ('f4eb93d1-9187-3cfb-83a4-6d9cd77f7df6','Vern Powlowski','M','GENERAL PRACTICE','585 LEBANON STREET','MELROSE','MA','02176',42.455723,-71.059019);");
    alasql("INSERT INTO providers VALUES ('0a8a9359-7b33-3256-a068-b5a7d18ebe4b','Keri Schmidt','F','GENERAL PRACTICE','115 LINCOLN STREET','FRAMINGHAM','MA','01701',42.307905,-71.436196);");
    alasql("INSERT INTO providers VALUES ('3180b739-e823-37a0-b307-52a6d67db4a5','Zana Considine','F','GENERAL PRACTICE','41 & 45 MALL ROAD','BURLINGTON','MA','01803',42.503227,-71.201713);");
    alasql("INSERT INTO providers VALUES ('47cb5349-d261-324a-9109-c888f4a0e966','Mohammed Parisian','M','GENERAL PRACTICE','759 CHESTNUT STREET','SPRINGFIELD','MA','01199',42.115454,-72.539978);");
    alasql("INSERT INTO providers VALUES ('77a7881d-6dd5-32e1-9e18-521a59749572','Phillip McCullough','M','GENERAL PRACTICE','88 LEWIS BAY ROAD','HYANNIS','MA','02601',41.748854,-70.740536);");
    alasql("INSERT INTO providers VALUES ('eabb2bff-3216-34da-9f29-824dbca901c3','Oscar Mateo','M','GENERAL PRACTICE','115 WEST SILVER STREET','WESTFIELD','MA','01085',42.138838,-72.755911);");
    alasql("INSERT INTO providers VALUES ('8ee28b4a-9018-3065-9f6b-0c9b69de7080','Malinda Cassin','F','GENERAL PRACTICE','201 HIGHLAND STREET','CLINTON','MA','01510',42.411887,-71.690005);");
    alasql("INSERT INTO providers VALUES ('f6065151-bf86-330b-a526-ac86b53b440b','Tressa Kovacek','F','GENERAL PRACTICE','200 GROTON ROAD','AYER','MA','01432',42.562221,-71.584844);");
    alasql("INSERT INTO providers VALUES ('0359f968-d1a6-30eb-b1cc-e6cc0b4d3513','Gaynell Streich','F','GENERAL PRACTICE','211 PARK STREET','ATTLEBORO','MA','02703',41.931653,-71.294503);");
    alasql("INSERT INTO providers VALUES ('3f15c687-0cfe-3bf2-9e62-34f3c85ff3cb','Jesús Quiroz','M','GENERAL PRACTICE','725 NORTH STREET','PITTSFIELD','MA','01201',42.452045,-73.26054);");
    alasql("INSERT INTO providers VALUES ('af01a385-31d3-3c77-8fdb-2867fe88df2f','Garth Wyman','M','GENERAL PRACTICE','575 BEECH STREET','HOLYOKE','MA','01040',42.211656,-72.642448);");
    alasql("INSERT INTO providers VALUES ('58b66cc1-2b86-377f-ad77-ad8164388e50','Veda Pfeffer','F','GENERAL PRACTICE','295 VARNUM AVENUE','LOWELL','MA','01854',42.638893,-71.322107);");
    alasql("INSERT INTO providers VALUES ('1530e81b-106c-32d5-95d5-42a710c92068','Wayne Mertz','M','GENERAL PRACTICE','271 CAREW STREET','SPRINGFIELD','MA','01104',42.115454,-72.539978);");
    alasql("INSERT INTO providers VALUES ('c9b3c857-2e24-320c-a79a-87b8a60de63c','Suzette Monahan','F','GENERAL PRACTICE','330 MOUNT AUBURN STREET','CAMBRIDGE','MA','02138',42.375967,-71.118275);");
    alasql("INSERT INTO providers VALUES ('e49edc61-6ba6-324c-bef7-b65f0e10799f','Carolyne Howell','F','GENERAL PRACTICE','51 BLOSSOM STREET','BOSTON','MA','02114',42.33196,-71.020173);");
    alasql("INSERT INTO providers VALUES ('aa89beb2-7bc6-35fa-83f7-4b32039e84eb','Sanford Gottlieb','M','GENERAL PRACTICE','199 REEDSDALE ROAD','MILTON','MA','02186',42.241589,-71.082651);");
    alasql("INSERT INTO providers VALUES ('4b04cd2f-3f27-35bc-8069-f4ca6339529f','Maile Frami','F','GENERAL PRACTICE','2014 WASHINGTON STREET','NEWTON','MA','02462',42.331876,-71.208402);");
    JSON.stringify(@0);
</script>

@AlaSQL.buildTable_organizations
<script>
    alasql("DROP TABLE IF EXISTS organizations;");
    alasql("create table organizations (id text,name text,address text,city text,state text,zip text,lat real,lon real,phone text);");
    alasql("INSERT INTO organizations VALUES ('24cb4eab-6166-3530-bddc-a5a8a14a4fc1','MILFORD REGIONAL MEDICAL CENTER','14 PROSPECT STREET','MILFORD','MA','01757',42.158692,-71.521419,'5084731190');");
    alasql("INSERT INTO organizations VALUES ('d692e283-0833-3201-8e55-4f868a9c0736','HALLMARK HEALTH SYSTEM','585 LEBANON STREET','MELROSE','MA','02176',42.455723,-71.059019,'7819793000');");
    alasql("INSERT INTO organizations VALUES ('465de31f-3098-365c-af70-48a071e1f5aa','METROWEST MEDICAL CENTER','115 LINCOLN STREET','FRAMINGHAM','MA','01701',42.307905,-71.436196,'5083831000');");
    alasql("INSERT INTO organizations VALUES ('6f122869-a856-3d65-8db9-099bf4f5bbb8','LAHEY HOSPITAL & MEDICAL CENTER  BURLINGTON','41 & 45 MALL ROAD','BURLINGTON','MA','01803',42.503227,-71.201713,'7817445100');");
    alasql("INSERT INTO organizations VALUES ('60457c13-adb2-3415-82c5-86ab5dab5f93','BAYSTATE MEDICAL CENTER','759 CHESTNUT STREET','SPRINGFIELD','MA','01199',42.115454,-72.539978,'4137940000');");
    alasql("INSERT INTO organizations VALUES ('ef6ab57c-ed94-3dbe-9861-812d515918b3','CAPE COD HOSPITAL','88 LEWIS BAY ROAD','HYANNIS','MA','02601',41.748854,-70.740536,'5087711800');");
    alasql("INSERT INTO organizations VALUES ('ebc3f5c4-6700-34af-8323-85621c313726','NOBLE HOSPITAL','115 WEST SILVER STREET','WESTFIELD','MA','01085',42.138838,-72.755911,'4135682811');");
    alasql("INSERT INTO organizations VALUES ('331f4c11-d298-308b-aaa1-d7825b29b57f','CLINTON HOSPITAL ASSOCIATION','201 HIGHLAND STREET','CLINTON','MA','01510',42.411887,-71.690005,'9783683000');");
    alasql("INSERT INTO organizations VALUES ('ac8356a5-78f8-3a63-8a1e-59e832fd54e7','NASHOBA VALLEY MEDICAL CENTER','200 GROTON ROAD','AYER','MA','01432',42.562221,-71.584844,'9787849000');");
    alasql("INSERT INTO organizations VALUES ('5e765f2b-e908-3888-9fc7-df2cb87beb58','STURDY MEMORIAL HOSPITAL','211 PARK STREET','ATTLEBORO','MA','02703',41.931653,-71.294503,'5082225200');");
    alasql("INSERT INTO organizations VALUES ('4f3a530e-a2f7-3de0-9a09-c0a70a9ab894','BERKSHIRE MEDICAL CENTER INC - 1','725 NORTH STREET','PITTSFIELD','MA','01201',42.452045,-73.26054,'4134472000');");
    alasql("INSERT INTO organizations VALUES ('5d4b9df1-93ae-3bc9-b680-03249990e558','HOLYOKE MEDICAL CENTER','575 BEECH STREET','HOLYOKE','MA','01040',42.211656,-72.642448,'4135342500');");
    alasql("INSERT INTO organizations VALUES ('b0e04623-b02c-3f8b-92ea-943fc4db60da','LOWELL GENERAL HOSPITAL','295 VARNUM AVENUE','LOWELL','MA','01854',42.638893,-71.322107,'9789376000');");
    alasql("INSERT INTO organizations VALUES ('fd328395-ab1d-35c6-a2d0-d05a9a79cf11','MERCY MEDICAL CTR','271 CAREW STREET','SPRINGFIELD','MA','01104',42.115454,-72.539978,'4137489000');");
    alasql("INSERT INTO organizations VALUES ('69176529-fd1f-3b3f-abce-a0a3626769eb','MOUNT AUBURN HOSPITAL','330 MOUNT AUBURN STREET','CAMBRIDGE','MA','02138',42.375967,-71.118275,'6174923500');");
    alasql("INSERT INTO organizations VALUES ('ff9863d3-3fa3-3861-900e-f00148f5d9c2','SHRINERS HOSPITAL FOR CHILDREN - BOSTON  THE','51 BLOSSOM STREET','BOSTON','MA','02114',42.33196,-71.020173,'6177223000');");
    alasql("INSERT INTO organizations VALUES ('12c9daf5-a29c-36c9-ac55-28972463e566','BETH ISRAEL DEACONESS HOSPITAL-MILTON INC','199 REEDSDALE ROAD','MILTON','MA','02186',42.241589,-71.082651,'6176964600');");
    alasql("INSERT INTO organizations VALUES ('3d10019f-c88e-3de5-9916-6107b9c0263d','NEWTON-WELLESLEY HOSPITAL','2014 WASHINGTON STREET','NEWTON','MA','02462',42.331876,-71.208402,'6172436000');");
    JSON.stringify(@0);
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
    JSON.stringify(@0);
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
    JSON.stringify(@0);
</script>
@end
-->

# SQL Basics

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

Experience working with rectangular data (data in rows and columns) is required, as is some exposure to the idea of SQL and its use of tables with rows and columns.  No experience writing SQL code is expected or required for this module.  If you would like a code-free overview to SQL we recommend our module [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md)

**Learning Objectives**

@learning_objectives

</div>


## SQL: A Brief Refresher

**SQL** (**S**tructured **Q**uery **L**anguage) is a language that for more than four decades has been used to interact with "**Relational Databases**".  You can pronounce it as "sequel" or just say the letters S-Q-L.

A relational database is a data storage solution that stores data tables, which are comprised of columns (sometimes called 'fields') and rows.

SQL is great at working with rectangular data, data that is stored in tables with rows and columns.  Its powerful SELECT / FROM / WHERE syntax makes SQL an ideal tool for isolating just the data you care about, whether that's specifying the columns you're interested in or limiting your data to just those rows that meet certain conditions.  However, it's not great for fine-tuned statistical, linguistic, or data visualization purposes.  SQL is therefore a tool that is often partnered with other tools like R or Python, which are better suited for work like statistical analysis.

If you want to review SQL at a high level, consider our [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md) module.

### SQL Implementations

Although all SQL implementations have a similar structure, and the same basic syntax, each different SQL database product often has its own minor variations in dialect.

Colloquially people often refer to the different SQL dialects as different "flavors" of SQL.

Some popular "flavors" of SQL:

* [**MySQL**](https://www.mysql.com/) (open source)
* [**SQLite**](https://www.sqlite.org) (open source)
* [**PostgreSQL**](https://www.postgresql.org/) (open source)
* [**Oracle**](https://www.oracle.com/database/technologies/appdev/sql.html) (proprietary)
* [**BigQuery**](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) (proprietary)

The most common difference between different SQL "flavors" are the availability of different functions that users can use for data manipulation, as well as the types of error messages that will be returned to the user when running code with syntax issues.

That said, knowing the specific "flavor" of SQL your database uses is especially useful when first getting started writing queries and troubleshooting errors.  

In the hands-on portion of this module, we'll be using a form of SQL that actually runs in your web browser as you look at these pages.  This lightweight SQL engine is called "AlaSQL".  We pre-populated some tables for you to experiment with in this module.  These tables are filled with fabricated data meant to look a little like an electronic health record (EHR).

## SQL Queries

A SQL **query** is essentially a question or request for data, written in a specific structure.  Let's take a closer look at how to compose a SQL query!

At a high level, we generally provide three pieces of information when constructing SQL "**queries**":

 1. The name of the **table(s)** where the data is stored.
 2. The **column name(s)** you want to look at from the table(s) you specified.  Want all the columns?  You can use an asterisk!
 3. Any **filtering condition(s)** you want to apply to your data pull.  This part is optional but is often used.

You put these basic pieces of information together using the syntax shown below to create a SQL query:

```sql
SELECT _2_ FROM _1_ WHERE _3_;
```

For example, here are some sample queries, each of which take place on just a single table.  

```sql
SELECT price FROM products WHERE product_type = "FRUIT";

SELECT mpg, transmission_type FROM cars;

SELECT * FROM patients WHERE age < 20;
```

Please note that while we write these queries all on a single line to show you a few examples in just a little space, that's the last time you'll see that kind of SQL in this module.  We have some strong opinions about SQL style here that we'll share in the next section.

### An Aside About Style

Style is how we choose to write SQL or other languages, within the confines of syntax.  All of the following queries are valid and would work.  What distinguishes them?  Style.  

```sql
select price, best_by_date, sale_pct, quantity from products where product_type = "FRUIT";
```

```sql
SELECT price, best_by_date, sale_pct,
quantity from products WHERE
product_type = "FRUIT";
```

```sql
SELECT
  price
  ,best_by_date
  ,sale_pct
  ,quantity
FROM products
WHERE product_type = "FRUIT";
```

You may be working with a group that has an established SQL style guide, either in written form or as oral tradition.  If so, great!  Ignore what we tell you and do what they suggest.  Style is nothing more than a convention to help humans read code more easily, and it's a good idea to go along with what is already broadly understood within your team.  Everyone agreeing on conventions like when to start a new line and how and where to comment means it's easier for other people to help you with your code or for you to copy / paste from existing examples your peers share with you.

But if you don't have anyone to guide you in style, we'll do our best to instill some basic principles. It might seem silly to start talking about style now with very short queries, but we encourage you to develop good habits now.  We are going to advocate for some style conventions that not everyone will share.  As they say, there's no accounting for taste, and if you depart from our suggestions, that's fine -- but do start to develop your own standards for style, because it will help you immensely once your SQL queries get to be 5, 10, or 100 lines long and the number of queries you write increases.

Here are our (opinionated but not necessarily "right" style suggestions).  These might not make sense right now, but once you see them in actual queries, we think you'll understand them more intuitively.

1) Put keywords in CAPITAL LETTERS so they stand out.  Examples of keywords are SELECT, LIKE, AS, WHERE, JOIN, DISTINCT, MEAN, ORDER BY, and many more.  While most code editors do a good job of color-coding these special words, you might end up seeing a SQL query in monochrome, and having keywords stand out helps you figure out where each part of your query is.  

2) Put members of a list on separate lines.  This usually means the list of fields you're requesting.  Putting each item on its own line is easier on the eyes and allows for much easier cut-and-paste to rearrange things.  It also means you have space after each item of the list to add a comment if necessary.

3) Use indentation to clarify the various sections of your query.  Indenting the list of columns below a SELECT statement is a way of subordinating those lines to the SELECT, subtly indicating that those lines are a continuation of the SELECT statement.  A new line that isn't indented (say, a FROM statement) shows that the SELECT part of the query is over.

4) Use "dot notation", which we'll talk about in the next section.  Dot notation means adding more information about your data, for example, by including the table name the column comes from.  This practice will prepare you for using multiple data sources in your queries.

5) Use a comma-first style.  This one can be a little jarring at first, but it does have real advantages, especially if you end up doing SQL for more than a few hours a week.  In a list of length n, don't put the comma *after* items 1 through n-1.  Rather, put the comma *before* items 2 through n.  

<div class = 'options'>

As long as you put a comma between the columns you are requesting (but not after the last column), your syntax is valid.  However, we propose a "comma-first" syntax.  To explain what comma-first syntax looks like, here are two shopping lists.  One is in comma-first style, where the first item is lacking a comma, and the other is comma-last, where the last item is missing a comma:


| comma-first (or leading comma) | comma-last (or trailing comma) |
| --- | ---- |
| apples | apples, |
| ,oranges | oranges, |
| ,lettuce | lettuce, |
| ,olives  | olives |


A comma-first stance is not uncontroversial, and some people find this style distracting or hard to understand.  If you hate it, you don't have to use it.  But first, allow us to share our rationale. Our thinking behind proposing a "comma-first" notation is based in ease of editing and improving your code as you go:

* **Commas line up.** In the comma-first example, it's easy to spot if you've left a comma out, because they all line up on the same character.  Not so in the comma-last version.  A missing comma will cause your SQL to not execute, and that's annoying and costs you extra time to track down which is the offending line.
* **It's easy to rearrange columns 2-n.** In SQL we often try a short query with just a few fields, then add a few more, then maybe rearrange their order, and finally delete the columns we don't need.  Usually, the first item in a list of columns is something of central importance, while the others in the list have a higher likelihood to be ones you may decide you don't need, or will change the order of.  Because you rarely touch the first item in a list but more frequently change the last item, it's less likely that you'll introduce a missing (or extra) comma using a comma-first paradigm as compared to the comma-last style.
* **You won't accidentally add a comma after your last item.** The reasoning is the same as above.  Anyone who's done SQL for very long has accidentally added a comma after the last item and spent a few minutes scratching their head trying to figure out what the error is.

</div>

Now that we've got you thinking about style, let's move on to the substance of SQL and work with SELECT and FROM.

### SELECT and FROM

A **SELECT statement** is used to specify which columns (or fields, we use both terms interchangeably here) you would like to have returned as output from your SQL query.

The basic components of a select statement are the `SELECT` and `FROM` keywords. The `FROM` keyword is used to specify the table or tables that hold the data you're interested in, and the `SELECT` keyword is used to provide a list of columns within those table(s) that you would like returned as output.  

**Select All Columns**

If you would like to return **all** of the fields from the table(s) specified in your SQL query, you can use the `*` wild card character as shown in the example below.  You'll notice that we put a line break between the asterisk and the `FROM` keyword.  Spaces and line breaks (together, called **whitespace**) don't really matter for SQL.  You can run your code together on a single line, or (as we strongly suggest) use styled whitepsace such as predictable line breaks and indentation.

Notice that the `FROM` line of this query is followed by 2 words separated by a period. This format is known as "**dot notation**".  Dot notation is usually something like `dataset_name.table_name.column_name`.  Some dialects of SQL might require some special notation, like backticks (`\``) around part of the dot notation, but we don't need that for your hands on work here.

So the first word in the dot notation below is "alasql", which is the name of the **schema** or **catalog** or **dataset** that your data is stored in (terms differ according to the dialect of SQL that you're using), and the second word, "patients", is the name of the specific table you would like to reference as the base of your query.

Ready to run your first SQL query?  Hit the execute button below the SQL code to run this query and you'll see the results appear!

```sql
SELECT *
FROM alasql.patients;
```

@AlaSQL.eval("#dataTable1")

<table id="dataTable1" border="1"></table><br>


**Select Specific Columns**

If you would only like to return a specific set of columns in your select statement you will need to explicitly list out each of those columns after the select keyword, with each separate column reference separated by a comma.  Note that this time, our dot notation is in the form `table_name.column_name` for our columns, and `dataset_name.table_name` for our table.  We do this to be very explicit about which data we mean.  

It may seem obvious that if we're getting data from the `patients` table, that all of our columns come, well, from `patients`... so why do we use dot notation to specify that in the list of columns?  Why say `patients.id` when `id` alone would work just as well?  

This is an example of forming a good habit early.  You will eventually need to do queries that involve multiple tables, which may each have similar or identical column names.  In that case, you **do** have to indicate which table you're referring to, in order to disambiguate which "date" column you mean -- do you mean `date` in `encounters`, or `date` in `medication_administration`?  Rather than learn dot notation later, we want to introduce you to it now, even if it feels unnecessary.

Go ahead and run this code by clicking the execute button.  How are your results different from the `SELECT *` query you ran previously?

```sql
SELECT
  patients.id
  ,patients.sex
  ,patients.race
  ,patients.ethnicity
  ,patients.state
FROM alasql.patients;

```
@AlaSQL.eval("#dataTable2")

<table id="dataTable2" border="1"></table><br>

@AlaSQL.buildTable_patients('')

### DISTINCT

The `DISTINCT` clause in **SQL** can be placed directly after the `SELECT` key word, and can be used to limit your result set down to only the unique row values.  

This can be especially useful when exploring a dataset for the first time and trying to become familiar with the data in each column of a given table.  For example, perhaps you want to see all the possible values for `sex` or `race` in the `patients` table, to understand a bit more about the data collection options.  If you were to use `SELECT` by itself to get just the `race` field from the `patients` table, you'd get the race of every patient, with lots of repeats.  If you used `SELECT DISTINCT` instead, you'd get a much shorter list of every possible value for `race`, each listed just once.  

You can also explore using SELECT DISTINCT on more than one field.  The code block below provides an example of using this syntax to invesitgate the unique combinations of values from the `sex` and `ethnicity` columns from the `patient` table.  As you can see, the `DISTINCT` clause will work on any number of columns.  Go ahead and execute this code to see the results.

```sql
SELECT DISTINCT
  patients.sex
  ,patients.ethnicity
FROM alasql.patients;

```
@AlaSQL.eval("#dataTable3")

<table id="dataTable3" border="1"></table><br>

<div class = "important">

Here's a pro tip!  The `DISTINCT` keyword is especially useful for removing duplicates rows from the result set of your SQL queries.  If you suspect that there may be duplicate data, you can use SELECT DISTINCT to make sure you only get one copy of any identical rows of results.

@AlaSQL.buildTable_patients('')


@AlaSQL.buildTable_patients('patients table queryable from this page!')

### Adding Comments

**Comments** are essentially explanatory or helpful bits of text that you can add to your code as documentation for yourself or other reviewers of your code.  Comments don't actually affect the execution of the SQL code in any way and are simply there for humans.

In **SQL** there are 2 different techniques that can be used for adding comments, **single-line** and **multi-line** comments.

Single-line comments can be created by typing 2 minus signs in a row (i.e. `--`).

Once added to your code, anything that appears to the right of the `--` comment delimiter will be treated as comment text.

Multi-line comments can be started by adding the `/*` characters to your code, and the multi-line comment can be closed by adding the `*/` characters.

Once created, any text that appears between the `/*` and `*/` "tags" will be treated as comment text.

The code block below provides an example of each of these styles of commenting:

```sql
/* This is a simple demographics query*/
SELECT
  patients.id         --unique patient identifier.
  ,patients.sex       --patient sex {'M', 'F'}
  ,patients.race      --patient race
  ,patients.ethnicity --patient ethnicity {'hispanic', 'nonhispanic'}
  ,patients.state     --full name of patients state of residence.
FROM alasql.patients;


/*
    Aren't Comments Great!
*/
```
@AlaSQL.eval("#dataTable11")

<table id="dataTable11" border="1"></table><br>

@AlaSQL.buildTable_patients('')


### WHERE

The **WHERE clause**, using the `WHERE` keyword, is the section of your query used to specify any "filtering logic" that should be applied to your query before returning any output.  It's optional but very useful.

The below example uses `WHERE` to filter output on only the records for a specific state.

```sql
SELECT *
FROM alasql.patients
WHERE
	patients.state='Massachusetts';

```
@AlaSQL.eval("#dataTable4")

<table id="dataTable4" border="1"></table><br>

Although the above example lists only one constraint for the dataset, the WHERE clause can contain any number of filtering arguments needed.

Check out the code block below for an example of a where clause that includes multiple constraints, and makes use of both **comparison** operators like `=` and `<=` and **logical** operators including `AND` and `OR`.  Also take a look at the useful comments!  The queries are getting a bit more complex, so it's worth trying to describe this query to yourself in plain English (or another natural language).

```sql
SELECT *
FROM alasql.patients
WHERE
	patients.state='Massachusetts'
	AND patients.ethnicity='hispanic'
	AND (
		patients.birthdate<='2000-01-01'   --date strings are assumed to be yyyy-mm-dd format.
		OR patients.birthdate>='2010-01-01'--date strings are assumed to be yyyy-mm-dd format.
	)

```
@AlaSQL.eval("#dataTable5")

<table id="dataTable5" border="1"></table><br>


@AlaSQL.buildTable_patients('')

### Dealing with Null Values

Like many programing languages, **SQL** deals with "blank" values in a very specific way.

**SQL** uses the concept of **null** to represent "blank" row values.

If you ever find yourself in a situation where you need to filter on null values you can use the `IS NULL` or `IS NOT NULL` operators as shown below.  Here, we're asking to see rows from the `allergies` table where the `stop` value (the date at which the presumed allergy was considered no longer applicable, resolved, a mistake, or not an allergy) isn't missing.  In other words, the allergy has a date at which it was ruled to not exist.

```sql
SELECT *
FROM alasql.allergies
WHERE
    allergies.stop IS NOT NULL; -- there is some value here, it's not empty

```
@AlaSQL.eval("#dataTable6")

<table id="dataTable6" border="1"></table><br>

Its also worth noting that null values are treated very differently from actual data.  Note that you cannot use operators like `=` to ask if something is null, because null values are inherently unknowable, so we can't know what a null value is equal to.  You can't do math with a null value and you can't compare to a null value.  To illustrate this point, we can look at the example code below.  

Consider three options with regards to the `stop` column of `allergies`.  The `stop` column will meet, for each row, one of the conditions below:

1) A date less than (earlier than) March 1, 2020,
2) A date on or greater than (after) March 1, 2020,
3) No date at all (null)

It's important to realize that the code below includes **only** the first case.  Rows that meet the second condition are in direct violation of the WHERE clause and are not included.  Rows that fall into the third condition (null) cannot be evaluated with a comparison operator, and are left out as well.

```sql
SELECT *
FROM alasql.allergies
WHERE
    allergies.stop < '2020-03-01'

```
@AlaSQL.eval("#dataTable7")

<table id="dataTable7" border="1"></table><br>

In order to make sure that records where the `stop` date is null are also included in our output we will need to add another line to the select statement to explicitly include them, as shown below:

```sql
SELECT *
FROM alasql.allergies
WHERE
    (
        allergies.stop < '2020-03-01'
        OR allergies.stop IS NULL
    )

```
@AlaSQL.eval("#dataTable8")

<table id="dataTable8" border="1"></table><br>

<div class = "warning">

The fact that nulls aren't included in comparisons is a very subtle distinction that can drastically alter the output of your SQL statements.  This can be very important when writing inclusion and exclusion logic and thinking about what cases belong in your data set.  Always keep in mind that you might have missing values, and consider what that might mean for your selection of rows.  

</div>

@AlaSQL.buildTable_allergies('')

### ORDER BY Statement

Another useful piece of SQL syntax for exporing datasets is the `ORDER BY` statement, which (as its name suggests) is used to order your result set by a given set of one or more columns.

When listing columns in the `ORDER BY` statment you can specify that they be sorted in either ascending (`ASC`) or descending (`DESC`) order. If you list more than one column in `ORDER BY`, items will be sorted first by the first column you provide, and then, within "ties", by the second, then third, etc., column.  For instance, the code below first sorts by `sex`, and then within each possible value of `sex` sorts by `ethnicity`.  Run it to see the results!

```sql
SELECT DISTINCT
  patients.sex
  ,patients.ethnicity
FROM alasql.patients
ORDER BY
  patients.sex ASC
  ,patients.ethnicity DESC;

```
@AlaSQL.eval("#dataTable9")

<table id="dataTable9" border="1"></table><br>

<div class = "important">

By default, all items in the `order by` clause will be sorted in `asc` order if no explicit ordering direction is provided.

</div>

@AlaSQL.buildTable_patients('')


### LIMIT

The `LIMIT` clause can be used to limit the result set of your select statement to (at most) a pre-defined number of rows.

To do this all you need to do is add the word `LIMIT` as the last line of your query, followed by the number of rows you would like your result set truncated at. This is a great bit of syntax to use for exporting a quick peek at tables you might be unfamiliar with.  Showing just the first three or five or ten rows of a table can give you a quick intuitive grasp of the contents of the whole table and will come back very quickly.  Without a `LIMIT`, large tables can take a long time to return all their results.

The example below pulls all columns from the `patients` table, and limits the result set to only 3 rows.

```sql
SELECT *
FROM alasql.patients
LIMIT 3

```
@AlaSQL.eval("#dataTable10")

<table id="dataTable10" border="1"></table><br>

@AlaSQL.buildTable_patients('')


### Aliasing with AS

In SQL, it is possible to assigne a custom name (usually a kind of shortened name) to a table or column in your query using a technique called **Aliasing**.

* Aliasing **tables** can be helpful for long or complex queries involving multiple tables because it allows you to avoid typing out the full name of a table each time you refer to it.  For example, in a long query involving the `patients` table, the `encounters` table, and the `diagnosis` table, you might prefer to use the shorthand terms `pt`, `enc`, and `dx` or even `p`, `e`, and `d`.

* Aliasing **columns** can be helpful to by assigning clearer, more comprehensible, names for a given column than the name that might be assigned to it in the database.  For example, the you might want to see the results from the `stop` column in the `allergies` table returned to you not as `stop`, but rather as `ruled_out_date`.

Aliases are assigned by placing the `AS` key word directly after the item (table/column) you would like to alias, followed by the name you would like to assign as its **alias**.

In the example below, we can see aliasing being used to rename the `patient` table to `p`, and renaming the `pat_id` and `state_abbr` columns to `unique_patient_id` (because there are other id fields you're working with elsewhere) and `state_name` (because you want to point out that this isn't the state abbreviation).

```sql
SELECT
  p.id AS unique_patient_id
  ,p.sex
  ,p.race
  ,p.ethnicity
  ,p.state AS state_name
FROM alasql.patients AS p

```
@AlaSQL.eval("#dataTable12")

<table id="dataTable12" border="1"></table><br>

@AlaSQL.buildTable_patients('')


## Recap

In this module, you learned about the language SQL, which is an acronym for "Structured Query Language".  It's a powerful tool for requesting specific subsets of data from a relational database, and has been around since the 1970's because of its efficiency and utility.  

We also introduced you to two important elements of the language:

* The "select" statement, which uses `SELECT` and `FROM`
* The "where" statement, which uses `WHERE`

We also discussed what SQL doesn't provide, like robust language and statistical processing and data visualization.  SQL is a tool that ordinarily is used in concert with other tools, each one used in its area of greater strength.

Finally, you learned about the structure of relational databases: data stored in tables, which are comprised of rows and columns.  Columns may contain identifers that allow data from different tables to be related to one another, and that's why the word "relational" appears.

## Additional Resources

* Khan Academy's [Introduction to SQL](https://www.khanacademy.org/computing/computer-programming/sql) is high quality and easy to learn from.

* [What is SQL?](https://education.arcus.chop.edu/sql-intro/) is a brief introduction to SQL similar to the material in this module.

* If you are interested in the history of technology, [Early History of SQL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6359709) is a comprehensive look into how SQL has evolved.  It's very jargon-dense!



> **Additional Reading**:
>
> To read more about the basic types of "Operators" avaiable for use in a **SQL** query, click [here](https://www.tutorialspoint.com/sql/sql-operators.htm) for some helpful documentation from **tutorialspoint.com**.



## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22SQL+Basics%22)!
