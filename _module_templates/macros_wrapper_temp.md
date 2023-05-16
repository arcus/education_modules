<!--

author:   DART Team
email:    dart@chop.edu
version:  0.0.0
module_type: wrapper
language: en
narrator: UK English Female
title: Wrapper Module Macros
comment:  This is placeholder module to save macros used in other modules.


resource1_name: Docker Tutorial
resource1_description: A tutorial on using Docker
resource1_wellvetted: true
resource1_wellvetted_text: This is a well-known thing.
resource1_maintained: true
resource1_maintained_text: Maintained by Docker.
resource1_stablesupport: false
resource1_stablesupport_text: Not stable?
resource1_a11y_issues: No known issues with accessibility.

resource2_name: Regexone Website
resource2_description: An interactive website for learning regex
resource2_wellvetted: false
resource2_wellvetted_text: No idea.
resource2_maintained: true
resource2_maintained_text: Yeah
resource2_stablesupport: true
resource2_stablesupport_text: Yep
resource2_a11y_issues: Good question...


@module_structure
1. Part 1
2. Part 2
3. Part 3
@end


@if_print_testing

<script>
  
  if(`@0`.includes("@")){ 
    send.html("doesn't exist")
  } else {
    send.liascript(`@print_list(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)`)
  }
</script>

<script>
  
  if(`@1`.includes("@")){ 
    send.html("doesn't exist")
  } else {
    send.liascript(`@print_resource2`)
  }
</script>

<script>
  
  if(`@2`.includes("@")){ 
    send.html("doesn't exist")
  } else {
    send.liascript(`@print_resource3`)
  }
</script>

@end


@if_print
<script>

if(`@0`.includes("@")){ 
  send.clear()
    } else { send.html(`
    <h4>@0</h4> 
    <p>@1</p>

    <ul class="fa-ul" id="id_@9"></ul>
    <script>
      let checks = [@2, @4, @6];
      let data = ['<b>Expert Authors / Well-Vetted: </b>@3', '<b>Maintained: </b>', '<b>Stable Support: </b>'];
      
      let list = document.getElementById("id_@9");
      var fragList = document.createDocumentFragment();

      for (let i = 0; i < data.length; i++) {
        var li = document.createElement('li');
        if(checks[i]){
          li.innerHTML = '<span class="fa-li"><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i></span>'+data[i]
        } else {
          li.innerHTML = '<span class="fa-li"><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i></span>'+data[i]
        }
        fragList.appendChild(li);
      }
      list.appendChild(fragList);
    </script>

    <b>Known issues with accessibility and/or inclusion:</b> @8

  We do our best to list potential problems here, but we might have missed something! If you encounter an issue, please let us know.`)
}
</script>
@end


@print_list
<h4>@0</h4> 

@1 

<ul class="fa-ul" id="id_@9"></ul>
<script>
  let checks = [@2, @4, @6];
  let data = ['<b>Expert Authors / Well-Vetted: </b>'+`@3`, '<b>Maintained: </b>'+`@5`, '<b>Stable Support: </b>'+`@7`];
  
  let list = document.getElementById("id_@9");
  var fragList = document.createDocumentFragment();

  for (let i = 0; i < data.length; i++) {
    var li = document.createElement('li');
    if(checks[i]){
      li.innerHTML = '<span class="fa-li"><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i></span>'+data[i]
    } else {
      li.innerHTML = '<span class="fa-li"><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i></span>'+data[i]
    }
    fragList.appendChild(li);
  }
  list.appendChild(fragList);
</script>
<b>Known issues with accessibility and/or inclusion:</b> @8

We do our best to list potential problems here, but we might have missed something! If you encounter an issue, please let us know in @make_survey_url('@title', '@version', '@module_type').
@end

print_resource1: @print_list(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)

print_resource2: @print_list(@resource2_name,@resource2_description,@resource2_wellvetted,@resource2_wellvetted_text,@resource2_maintained,@resource2_maintained_text,@resource2_stablesupport,@resource2_stablesupport_text,@resource2_a11y_issues,@uid)

print_resource3: @print_list(@resource3_name,@resource3_description,@resource3_wellvetted,@resource3_wellvetted_text,@resource3_maintained,@resource3_maintained_text,@resource3_stablesupport,@resource3_stablesupport_text,@resource3_a11y_issues,@uid)

@lesson_prep_wrapper

<h3>This module will direct you to external educational content.</h3>

Many topics have great content written by others! We chose this content for you based on how well it meets our criteria.

Not all selected materials will meet all of these criteria, but selected materials should meet as many as possible.
Write a short sentence about how this material meets, or does not meet, each criterion.

@end

@test_printing

<script>
  
  if(`@0`.includes("@")){ 
    send.html("doesn't exist")
  } else {
    send.html("here's the list")
  }
</script>

@end


import: https://raw.githubusercontent.com/arcus/education_modules/templates_update/_module_templates/macros.md
-->

# Wrapper Module Macros

if print testing 

@if_print_testing(@resource1_name,@resource2_name,@resource3_name)

print 1

@print_list(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)

print 2 

@print_list(@resource2_name,@resource2_description,@resource2_wellvetted,@resource2_wellvetted_text,@resource2_maintained,@resource2_maintained_text,@resource2_stablesupport,@resource2_stablesupport_text,@resource2_a11y_issues,@uid)


## testing

@if_print(@resource2_name, @resource2_description)

@if_print(@resource3, @resource3_name)

@if_print(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)

