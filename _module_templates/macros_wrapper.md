<!--

author:   DART Team
email:    dart@chop.edu
version:  0.0.0
language: en
narrator: UK English Female
title: Module Macros
comment:  This is placeholder module to save macros used in other modules.


@check_list_item
<script>
if (@0) {
    send.html(`  <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> ${@1} : ${@2}</li>`);
  } else {
    send.html(`  <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> ${@1} : ${@2}</li>`);
  }
</script>
@end

@format_list
<script>
send.html(`<ul style="list-style-type: none">`)

@check_list_item(@0,"Well-Vetted",@2)
@check_list_item(@1,"Maintained",@2)
@check_list_item(@0,"Stable Support",@2)

send.html(`</ul>`)
</script>
@end

@make_survey_url
<script>
function makeURL(title, version_number, module_type) {
  let url = new URL('https://redcap.chop.edu/surveys');
  url.searchParams.set('s', 'KHTXCXJJ93');
  url.searchParams.set('module_name', title);
  url.searchParams.set('version_number', version_number);
  url.searchParams.set('module_type', module_type);
  return url;
}
var surveyURL = makeURL(@0, @1, @2);

send.html(`<a href="${surveyURL}")">our brief survey</a>`)
</script>
@end

@external_resources_javascript
<script>
var external_resources = [
   {
      resource1: {
        name:"Java-101",
        description:"Introduction to Java",
        expert_author_check: true,
        expert_author_text: "This is written by a total expert."
        
      },
      resource2: {
        name:"Java-102",
        description:"Introduction to More Java",
        expert_author_check: false,
        expert_author_text: "This is an anonymous post."
      },     
   }
]

external_resources.map((resource_list)=>{
   if (typeof resource_list.resource1 != 'undefined')
   send.html(`<b "${resource_list.resource1.name}"</b>)"\n${resource_list.resource1.description}"`)
   if (typeof resource_list.resource2 != 'undefined')
   send.html(`<b "${resource_list.resource2.name}"</b>)"\n${resource_list.resource2.description}"`)   
})
</script>
@end

@lesson_prep_wrapper

This module will direct you to external educational content.
---

Many topics have great content written by others! We chose this content for you based on how well it meets our criteria.

Not all selected materials will meet all of these criteria, but selected materials should meet as many as possible.
Write a short sentence about how this material meets, or does not meet, each criterion.

**Resource 1 Name**

Short optional summary sentence about resource 1.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
</ul>

**Known issues with accessibility and inclusive design:** Explain any known problems related to accessibility and inclusive design here. If there are none, you can write "No known issues, but we may have missed something. If you encounter an issue, please [let us know in our feedback form](#feedback)!"

**Resource 2 Name**

Short optional summary sentence about resource 2.

<ul style="list-style-type: none">
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Expert Authors / Well-Vetted: _who are the expert authors? or what institutional authority guarantees accuracy?_</li>
   <li><i class="fa-solid fa-circle-minus" style="color: #f0bc00;" title="Unchecked"></i> Maintained: _who is in charge of implementing regular updates to this material, important in fast-changing fields._</li>
   <li><i class="fa-solid fa-circle-check" style="color: #158d0c;" title="Checked"></i> Stable Support: _who hosts this material so it won't disappear? If it does, please let us know in a feedback form ASAP!_</li>
</ul>

**Known issues with accessibility and inclusive design:** Explain any known problems related to accessibility and inclusive design here. If there are none, you can write "No known issues, but we may have missed something. If you encounter an issue, please [let us know in our feedback form](#feedback)!"

@end


link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js
script:  https://code.jquery.com/jquery-3.6.0.slim.min.js

-->

# Module Macros

@format_list(true, false, "Description here.")
