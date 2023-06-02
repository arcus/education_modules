<!--

author:   Your Name
email:    email@chop.edu
version:  0.0.0
current_version_description: Brief description of why this version exists
module_type: wrapper
docs_version: 1.1.0
language: en
narrator: UK English Female
mode: Textbook

title: Module Title

comment:  This is a short, focused description of the module.

long_description: This is a longer description, which should be understandable for a lay audience.

estimated_time_in_minutes: 

@pre_reqs
List any skills or knowledge needed to complete this module here.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- identify key elements
- create a product
- do a task
- articulate the rationale for something
@end

@version_history 

Previous versions: 

- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
- [x.x.x](link): that version's current version description
@end

resource1_name: Thing
resource1_description: Great stuff
resource1_wellvetted: true
resource1_wellvetted_text: So good
resource1_maintained: false
resource1_maintained_text: Iffy at best
resource1_stablesupport: true
resource1_stablesupport_text: Very solid
resource1_a11y_issues: Doesn't exist, so heads up if that's a deal breaker for you.


@module_structure
1. Part 1
2. Part 2
3. Part 3
@end



@print_list
<h4>@0</h4> 

@1 

<ul class="fa-ul" id="id_@9"></ul>
<script modify="false">
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
@end

print_resource1: @print_list(@resource1_name,@resource1_description,@resource1_wellvetted,@resource1_wellvetted_text,@resource1_maintained,@resource1_maintained_text,@resource1_stablesupport,@resource1_stablesupport_text,@resource1_a11y_issues,@uid)



import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/wrapper_macro_fix/_module_templates/macros_wrapper.md
-->

# Module Title

## Lesson Preparation


@print_resource1


## Additional Resources


