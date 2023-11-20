# Education Modules

## Easier Interface

If you're a learner or educator and you don't want to read the technical details, but want to jump right into training materials, please visit our [learner and educator facing site](https://arcus.github.io/education_modules).  Otherwise, read on to get more details about this repository.

## Intention

This repository holds publicly available instructional modules aimed at teaching data science and related skills to researchers, as part of an NIH emphasis on improving research reproducibility, transparency, and rigor.

These materials have been created for the purpose of sharing them widely with the research community.  Support for this effort includes NIH funding via an R25 grant mechanism.

## About These Materials

The training materials here are built in [markdown](https://www.markdownguide.org/), and you can use the Liascript markdown renderer to make them into attractive, configurable training modules.  To use Liascript, go to https://liascript.github.io and enter the url of any markdown file.  

This project is grateful for the generosity of Liascript's creators and sustainers, André Dietrich and Sebastian Zug, for sharing their work (and advice!) freely.

## Remixing Our Materials

This work is [licensed](LICENSE) with Creative Commons Attribution-ShareAlike 4.0.  There is also a helpful [summary](https://creativecommons.org/licenses/by-sa/4.0/) of the full [license](LICENSE) that describes what we permit in brief terms.  You are free to share and adapt these materials as long as you give appropriate credit and apply the same license to your version of these materials.  Some uses we foresee include:

* [Forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository and changing some elements to be more contextualized to your audience (such as translating materials or changing sample data), and sharing the remixed contents with your audience
* [Forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository and adding or removing courses that best meet the needs of your audience
* Sharing links to this repository or its contents with communities of learners
* Suggesting changes to our materials (especially where doing so would improve generalizability and accessibility) by [adding an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-repository) or [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) with proposed changes
* Creating free community learning events like user groups or hackathons that use these materials
* Using our published guidelines and methods for curriculum creation, with attribution, in your own projects

If you do use these materials, we would love to hear from you!  Please [let us know about your experience](mailto:dart@chop.edu) so we can continue to improve.


## For Contributors

If you would like to create a module for inclusion here, please review our documentation on [how to write a module](_for_authors/write_a_module.md).
## A Few Notes and Caveats

If you use .css or .js scripts, it's important to know that you can't supply these scripts directly from GitHub.  GitHub does not provide the appropriate metadata to indicate that the content of the files is of the correct type, which means that browsers won't include them.

One solution is to use a CDN that re-packages GitHub contents for use in a web page.  For example, [Liascript itself suggests using a CDN](https://github.com/liaScript/custom-style/) to provide a CSS script from GitHub.

Since CDNs generally have a refresh rate that doesn't meet the "let's try this really quickly" pace of development in GitHub, another option is to host your script in another publicly accessible location.  In our case, we've made use of the AWS S3 service to host a custom css file.  This means updating the S3 version of the file as well as the version hosted here, in this GitHub, but the extra headache is worth it.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
