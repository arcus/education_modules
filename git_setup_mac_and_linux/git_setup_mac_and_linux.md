<!--

author:   Rose Hartman
email:    hartmanr1@chop.edu
version:  1.0.3
module_template_version: 2.0.0
language: en
narrator: UK English Female
title: Setting Up Git on Mac and Linux

comment: This module provides recommendations and examples to help new users configure git on their computer for the first time on a Mac or Linux computer.

long_description: If you're ready to start using the Git version control system, this lesson will walk you through how to get set up. This lesson should be a good fit for people who already have an idea of what version control is (although may not have any experience using it yet), and know how to open the command line interface (CLI) on their computer. No previous experience with Git is expected.

estimated_time: 15 min

@learning_objectives  

After completion of this module, learners will be able to:

- Configure `git` the first time it is used on a computer
- Understand the meaning of the `--global` configuration flag

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/styles.css

script: https://kit.fontawesome.com/83b2343bd4.js

-->

# Setting Up Git on Mac and Linux

<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** @estimated_time

**Pre-requisites**

- Have used the command line interface (CLI) on your computer before
- Have Git installed on your computer (note that it is probably installed already even if you've never used it)
- Have an account on github.com (you can [sign up now](https://github.com/signup) if you haven't yet --- it's free)


**Learning Objectives**

@learning_objectives

</div>

## Lesson Preparation

<div class = "important">
Note that this module is written specifically for people working on Mac or Linux computers. If you are using a Windows machine, you should reference [Git Setup for Windows](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_setup_windows/git_setup_windows.md) instead.
</div>

All of the commands for this lesson should be run in the command line interface (CLI) of your computer.
You don't need to navigate to a particular directory or open anything else;
you should be able to just open the CLI and run all of the commands in this lesson as they are written.

Chances are very good that Git is already installed on your computer, even if you've never used it before.
To check, run the following command:

```bash
git --version
```

You should get some brief message giving the version number of Git installed on your machine (e.g. `git version 2.24.3 (Apple Git-128)` or something similar).
If you get an error message instead, you may need to [install Git](https://carpentries.github.io/workshop-template/#git) before continuing with the lesson.  

<div class = "important">
If you don't have Git installed already, go ahead and try downloading it using the links above, but if you have problems talk to your own institution's tech support. Especially if your computer was issued by your employer, they might have put up very high barriers to downloading and installing things.
</div>

## Global configurations

When we use Git on a new computer for the first time, we need to configure a few things.
Below are a few examples of configurations we will set as we get started with Git:

*   our name and email address,
*   what our preferred text editor is,
*   and that we want to use these settings globally (i.e. for every project).

<div class = "important">
We will use `git config` with the `--global` option to configure a user name, email address, editor, and other preferences. This only needs to be done once per machine.
</div>

### Setting up your username and email

On a command line, Git commands are written as `git verb options`,
where `verb` is what we actually want to do and `options` is additional optional information which may be needed for the `verb`. So here is how
Dracula sets up his new laptop:

```bash
$ git config --global user.name "Vlad Dracula"
$ git config --global user.email "vlad@tran.sylvan.ia"
```
<div class = "warning">
Please use your own name and email address instead of Dracula's.
</div>

This user name and email will be associated with your subsequent Git activity,
which means that any changes pushed to
[GitHub](https://github.com/),
[BitBucket](https://bitbucket.org/),
[GitLab](https://gitlab.com/) or
another Git host server
after this lesson will include this information.

For this lesson, we will be interacting with [GitHub](https://github.com/) and so the email address used should be the same as the one used when setting up your GitHub account.

<div class = "options">
If you are concerned about privacy, please review [GitHub's instructions for keeping your email address private](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address).
</div>

If you elect to use a private email address with GitHub, then use that same email address for the `user.email` value, e.g. `username@users.noreply.github.com` replacing `username` with your GitHub one.

### Handling line endings

As with other keys, when you hit `Enter` or `↵` or on Macs, `Return` on your keyboard,
your computer encodes this input as a character.
Different operating systems use different character(s) to represent the end of a line.
(You may also hear these referred to as newlines or line breaks.)
Because Git uses these characters to compare files,
it may cause unexpected issues when editing a file on different machines.

<div class = "learnmore">
Though it is beyond the scope of this lesson, you can read more about this issue
[in the Pro Git book](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_core_autocrlf).
</div>

You can change the way Git recognizes and encodes line endings using the `core.autocrlf` command to `git config`.
The following setting is recommended:

```bash
$ git config --global core.autocrlf input
```

### Setting your text editor

Dracula also has to set his favorite text editor, following this table:

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| Atom | `$ git config --global core.editor "atom --wait"`|
| nano               | `$ git config --global core.editor "nano -w"`    |
| BBEdit (Mac, with command line tools) | `$ git config --global core.editor "bbedit -w"`    |
| Sublime Text (Mac) | `$ git config --global core.editor "/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl -n -w"` |
| Kate (Linux)       | `$ git config --global core.editor "kate"`       |
| Gedit (Linux)      | `$ git config --global core.editor "gedit --wait --new-window"`   |
| Scratch (Linux)       | `$ git config --global core.editor "scratch-text-editor"`  |
| Emacs              | `$ git config --global core.editor "emacs"`   |
| Vim                | `$ git config --global core.editor "vim"`   |
| VS Code                | `$ git config --global core.editor "code --wait"`   |

It is possible to reconfigure the text editor for Git whenever you want to change it.


<div class = "help">
**Exiting Vim**

Note that Vim is the default editor for many programs. If you haven't used Vim before and wish to exit a session without saving your changes, press `Esc` then type `:q!` and hit `Enter` or `↵` or on Macs, `Return`.
If you want to save your changes and quit, press `Esc` then type `:wq` and hit `Enter` or `↵` or on Macs, `Return`.

This is [a common problem that has frustrated many a new Git user](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)! You are not alone.
</div>

### Default branch naming

Git (2.28+) allows configuration of the name of the branch created when you initialize any new repository.  Dracula decides to use that feature to set it to `main` so
it matches GitHub, which is the cloud service he will eventually use.

```bash
$ git config --global init.defaultBranch main
```

Source file changes are associated with a "branch."
For new learners in this lesson, it's enough to know that branches exist, and this lesson uses one branch.
The primary branch of some projects, particularly older projects, is called `master` instead of `main`. GitHub has joined the programming community in a concerted effort to [replace programming terms associated with slavery](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/). However Git has not yet made the same change.  As a result, local repositories must be manually configured have the same main branch name as most cloud services.

### Check your global configurations

The commands we just ran in the sections above only need to be run once: the flag `--global` tells Git to use the settings for every project, in your user account, on this computer.

You can check your settings at any time:

```bash
$ git config --list
```

You can change your configuration as many times as you want: use the same commands to choose another editor or update your email address.

<div class = "help">
**Proxy**

In some networks you need to use a
[proxy](https://en.wikipedia.org/wiki/Proxy_server). If this is the case, you may also need to tell Git about the proxy:

```bash
$ git config --global http.proxy proxy-url
$ git config --global https.proxy proxy-url
```

To disable the proxy, use

```bash
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```

Not sure whether or not your network uses a proxy? You should be able to check for a proxy by looking at the settings in your browser. For example, [here's what the proxy settings look like for the FireFox browser](https://support.mozilla.org/en-US/kb/connection-settings-firefox). You can search online to find more examples of proxy settings in different browsers, or just open the Settings for whatever browser you're using and poke around to see if you can find proxy information.

**Note**: If your network does use a proxy, or if you can't determine whether there's a proxy or not, you may need to contact your own institution's tech support team for help. In some cases, proxy settings can be complex; you may not be able to find good information relevant to your specific situation without talking to the team that manages your network.
</div>

## Git Help and Manual

Always remember that if you forget the subcommands or options of a `git` command, you can access the relevant list of options typing `git <command> -h` or access the corresponding Git manual by typing
`git <command> --help`, e.g.:

```bash
$ git config -h
$ git config --help
```

<div class = "important">
While viewing the manual, remember the `:` is a prompt waiting for commands and you can press `Q` to exit the manual.
</div>

More generally, you can get the list of available `git` commands and further resources of the Git manual typing:

```bash
$ git help
```

## Quiz

Without looking it up, what can you say about the following command? `git config --global alias.ci commit` Select all that apply.

[[X]] It will change something in the global settings, meaning it will apply to all the projects in your user account on this computer
[[ ]] You'll need to run this command each time you start a new Git repository if you want it to take effect
[[ ]] It will affect your settings on GitHub.com as well as on your local computer
***
<div class = "answer">

This command begins with `git config --global`, like most of the commands we ran during this lesson. The `--global` flag tells us this setting will be applied for all of the Git projects on this user account on this computer (for a review of this topic, see [Check your global configurations](#check-your-global-configurations)).

Global configurations for Git only need to be run once and then they will continue to apply until you undo them or replace them with new settings.

Importantly, 'global' only refers to within your account on your machine; if you use Git on multiple machines, or when you use it in the cloud (for example, on GitHub.com), your global configuration settings from your personal machine won't apply.

</div>
***

If you wanted to learn more about the command above, which of the following would be good places to start? Select all that apply.

[[ ]] `git config -h`
[[X]] `git config --help`
[[X]] Google it
[[X]] Ask a friend, or post a question in an online community forum
****
<div class = "answer">

Remember that  `-h` will pull up a list of the options for a command, while `--help` will bring up its full help documentation. In this case, knowing the list of options for `git config` won't help much since you need additional information about how the `global` option is working in this particular case, not just the fact that `global` is an option. In general, `-h` is good for when you already know pretty much what a command does but want a reminder of how to use it, whereas `--help` is better for learning about a new command.

In this particular case, the help file for `git config` won't tell you what you want to know about the global settings for aliases, so `git config --help` will turn out to be a dead end. But sometimes the Git help files will have exactly what you need, so it's never a bad idea to check!

Googling it is also never a bad idea. There are tons of great Git resources available online, and for common problems you're likely to find a useable answer quickly. Keep in mind that there are lots of very advanced Git users posting things online as well, though, and if you get unlucky you could end up with search results that are not at all user-friendly for beginners. When that happens, remind yourself that kind of gatekeeping is a failure on the part of the writer, not something wrong with you as a learner, and keep searching to find a good answer to your question somewhere else.

Asking a peer (in person, or via an online community of practice) is probably the best strategy in a lot of situations, especially if the first two strategies don't yield useful results right away. If you feel embarrassed to ask a question, remind yourself that everyone is a beginner at some point and [asking for help is a great skill to practice](https://www.linkedin.com/pulse/20141027152039-95387062-why-you-should-never-feel-embarrassed-to-ask-questions)!

</div>
****

<details>

<summary>**Curious about that `alias` command? Click to learn more.**</summary>

<div class = "learnmore">
This command is an example of [how to set aliases in Git](https://www.atlassian.com/git/tutorials/git-alias), something we didn't cover in this lesson.

Basically, aliases are shortcuts you can write for yourself so you don't have to type out full Git commands every time. We won't be using aliases in the lessons here, but you may like to set some up on your own computer if that sounds attractive to you!
</div>

</details>


## Additional Resources

Although the content here focuses on command line Git, you may prefer to use the GitHub Desktop program instead. See the instructions posted on GitHub.com for how to [install and configure GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop).

## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Setting+up+Git+for+Mac+and+Linux%22)!
