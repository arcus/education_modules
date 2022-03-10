# Versioning Guidelines
In order to keep track of the many moving pieces of this project, we've instituted version numbers for three things:
1. Module content
2. Sample module template
3. QA Process template checklist

This document provides guidance to ensure that we are all using version numbering in the same way.

**Versioning Basics:**
* Each time one part of the version number is increased, all numbers of the right of it are reset to zero.
* Every digit matters -- don't treat version numbers like decimals
  * Version 1.2.1 ≠ 1.2.10 (this is _nine_ versions newer).
  * Version 1.2.5 is older than 1.2.36

We are using semantic versioning, which is a 3-part version number (x.y.z) where each part corresponds to a different kind of update: major.minor.revision

Because our use case is different than the traditional use for semantic versioning (software development), below is some more granular definition of how we're interpreting those terms.

### Major.x.x
This number gets incremented for each major content update, with version 1.0.0 being the first public version of the module/first version of the template ever utilized.

**Modules:** </br>
Examples: entirely new content is added; sections are majorly reworked; the scope of the module is widened or narrowed; significant content is removed.

A good mental framework might be that an update is major if the module has changed significantly enough that a learner who took previous versions would not be familiar with all of this version's content or may encounter new knowledge by retaking it.
On the other hand, an update would also be major if a learner who takes the new version would walk away with less knowledge than a learner who previously took it, as would be the case if the scope was narrowed.

**Templates:** </br>
Examples: entirely new elements are added; elements are removed; elements are expanded upon or reworded in a way that is significant enough to potentially impact how the template was previously interpreted and applied

A good mental framework here might be that an update is major if the template has changed enough that things created using earlier versions of the template will need to be updated to ensure that they are in line with the new standards.

### x.Minor.x
These updates still affect the module or template content but are not as wide-reaching as major updates.

**Modules:** </br>
Examples: rewording parts of the content to increase clarity without adding new information; adding more informative feedback to incorrect answers in formative assessments; providing links to additional resources; restructuring the order in which content is presented

A good mental framework might be that an update is minor if the module is updated in a way that hopefully improved the learning experience for future learners but is not so substantially different that previous learners would be expected to gain much by retaking the new version.

**Templates:** </br>
Examples: elements are reworded to improve clarity; ordering or presentation of elements of template is changed; sections are combined or further split apart

A good mental framework might be that an update is minor if the template has changed in a way that probably shouldn't significantly alter the standards of the thing being templated, however it may be worthwhile to look over things created with previous versions of the template to ensure that everything is consistent.


### x.x.Revision

These updates are small, inconsequential changes.

Examples: fixing typos, updating broken links

A good mental framework might be that these changes are generally so small that it would be very difficult if not impossible to quickly spot what changed when looking at the old and new versions side-by-side
