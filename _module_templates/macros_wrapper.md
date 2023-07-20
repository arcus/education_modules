<!--

author:   DART Team
email:    dart@chop.edu
version:  1.0.0
current_version_description: Add current_version_description and version_history metadata
language: en
narrator: UK English Female
title: Wrapper Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history  
@end

@module_structure
1. Part 1
2. Part 2
3. Part 3
@end

@print_list
<h4>@0</h4> 

@1 

<script run-once modify="false" style="display:block">

let checks = [@2, @4, @6];

let list = ""

const data = ['<b>Expert Authors / Well-Vetted: </b>'+`@3`, '<b>Maintained: </b>'+`@5`, '<b>Stable Support: </b>'+`@7`]

for (let i = 0; i < data.length; i++) {
  
  if(checks[i]){
      list += '<li><span class="fa-li"><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i></span>' + data[i] + '</li>'
    } else {
      list += '<li><span class="fa-li"><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i></span>' + data[i] + '</li>'
    }
};

"HTML: <ul class='fa-ul'>" + list + "</ul>"
</script>
<b>Known issues with accessibility and/or inclusion:</b> @8
@end

print_resource1: @print_list(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)

print_resource2: @print_list(@resource2_name,@resource2_description,@resource2_wellvetted,@resource2_wellvetted_text,@resource2_maintained,@resource2_maintained_text,@resource2_stablesupport,@resource2_stablesupport_text,@resource2_a11y_issues,@uid)

print_resource3: @print_list(@resource3_name,@resource3_description,@resource3_wellvetted,@resource3_wellvetted_text,@resource3_maintained,@resource3_maintained_text,@resource3_stablesupport,@resource3_stablesupport_text,@resource3_a11y_issues,@uid)

@lesson_prep_wrapper

<h3>This module will direct you to external educational content.</h3>

Many topics have great content already available online! For this module, here's what to expect:

@module_structure

<h3>More information about the resources we link to</h3>

We only link to external resources that we think do an excellent job of teaching the content. 
We also evaluate each resource based on how well it meets our criteria.

@end

-->

# Wrapper Module Macros

@lesson_prep_wrapper

@print_resource1

@print_resource2

@print_resource3

