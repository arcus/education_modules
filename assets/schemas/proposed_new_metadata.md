### Proposed metadata:

#### Already exist, to be included in front matter:
- [ ] `pre_reqs` : currently stored only on the overview page of each module.


#### New module metadata:

- [ ] `coding_required` : required metadata, True/False based on whether acheiving the module's learning objectives requires coding. If this is True: 
  - [ ] `coding_language` : required if coding_required is True
    - `r`
    - `sql`
    - `python`
    - `bash`
    - `git`
    - multiple languages: A module teaching regex, for example, is not specific to a particular language, but does require the learner to code.
  - [ ] `coding_level`: required if coding_required is True
    - getting started: These modules are primarily about getting a platform set up
    - basics: These modules require little or no previous exposure to coding
    - intermediate: These modules require some previous coding exposure
    - advanced: These modules focus on particularly difficult or specialized tasks.
    - practice exercise: These modules do not introduce new content.
- [ ] `data_type `: optional metadata for modules that focus on a particular type of data, either as the topic of the module or as the main type of examples.
  - omics
  - geospatial
  - ehr
- [ ] `data_task`: optional metadata. What type of task/action/skill does this module teach?
  - data_visualization
  - data_management
  - data_cleaning
  - data_transformation
  - data_analysis
 
