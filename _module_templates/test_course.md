<!--

@listmacro

<ul id="mylist"></ul>

<script>
// example from https://developer.mozilla.org/en-US/docs/Web/API/Document/createDocumentFragment#javascript

const element = document.getElementById("mylist"); 
const fragment = document.createDocumentFragment();
const browsers = ["Firefox", "Chrome", "Opera", "Safari"];

browsers.forEach((browser) => {
  const li = document.createElement("li");
  li.textContent = browser;
  fragment.appendChild(li);
});

element.appendChild(fragment);

</script>

@end

-->

# Test course

@listmacro

