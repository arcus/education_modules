<!--

author:   DART Team
email:    dart@chop.edu
version:  1.1.0
current_version_description: Add current_version_description and version_history metadata, remove @overview
language: en
narrator: UK English Female
title: Module Macros for SQL
comment:  This is placeholder module to save macros used in other modules.

@version_history 

Previous versions: 

- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/e983922162e6fbf971c03dc96052f68713cc72af/_module_templates/macros_sql.md#1): Initial version
@end

@lesson_prep_sql

**SQL** (**S**tructured **Q**uery **L**anguage) is a language that for more than four decades has been used to interact with **relational databases**.  You can pronounce it as "sequel" or just say the letters S-Q-L.

A relational database is a data storage solution that stores data tables, which are comprised of columns (also called 'fields') and rows.

<div class = "important">

Sometimes we'll use the word "column" and sometimes we'll use the word "field".  These refer to the same thing!

</div>

SQL is great at working with rectangular data, data that is stored in tables with rows and columns / fields.  Its powerful SELECT - FROM - WHERE syntax makes SQL an ideal tool for isolating just the data you care about, whether that's specifying the columns you're interested in or limiting your data to just those rows that meet certain conditions.  However, it's not great for fine-tuned statistical, linguistic, or data visualization purposes.  SQL is therefore a tool that is often partnered with other tools like R or Python, which are better suited for work like statistical analysis.

If you want to review SQL at a high level, consider our [Demystifying SQL](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_sql/demystifying_sql.md) module.

Most users of SQL do a lot of their work in one of many SQL **clients**.  A SQL client is a piece of software that has lots of functions, like allowing you to connect to various databases you have access to, giving you a place to type queries and submit them, and diagramming capability to help you understand the relationships in your database.  

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
@end

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
-->

# Module Macros

## Lesson Preparation: SQL

@lesson_prep_sql

## Feedback
@feedback
