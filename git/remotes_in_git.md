<!--

author:   Julianna Pakstis
email:    pakstisj@chop.edu
version:  0.0.1
language: en
narrator: UK English Female
title: Remotes in GitHub
comment:  Learn how to share changes with others on the web. 
long_description: Learn how to share changes to and gather changes from remote repositories in GitHub on the web. This module teaches how to share your work between repositories and how to pull the work of others into your repository. It reveals the power of git and Github for collaboration. 

@learning_objectives  

After completion of this module, learners will be able to:

- Explain what remote repositories are and why they are useful 
- Push to or pull from a remote repository

@end

link:  https://chop-dbhi-arcus-education-website-assets.s3.amazonaws.com/css/modules.css

-->

# Remotes in GitHub


<div class = "overview">

## Overview
@comment

**Is this module right for me?** @long_description

**Estimated time to completion:** 45 minutes-1 hour

**Pre-requisites**

List any skills and knowledge needed to do this module here. When available, include links to resources, especially other modules we've made (to show learners where this falls within our catalog).

* A [GitHub](https://github.com/) account
* (Preferred) Completion of git modules 1-6

**Learning Objectives**

@learning_objectives


</div>

## Lesson Preparation

Open a web browser, like Chrome or Firefox 

## Create a remote repository

Log in to [GitHub](github.com), then click on the icon in the top right corner to create a new repository called planets:

![github-create-repo-01](./assets/media/remotes_step_01_images/github-create-repo-01.png)

Name your repository “planets” and then click “Create Repository”.

Note: Since this repository will be connected to a local repository, it needs to be empty. Leave “Initialize this repository with a README” unchecked, and keep “None” as options for both “Add .gitignore” and “Add a license.” See the “GitHub License and README files” exercise below for a full explanation of why the repository needs to be empty.


![github-create-repo-02](./assets/media/remotes_step_01_images/github-create-repo-02.png)


As soon as the repository is created, GitHub displays a page with a URL and some information on how to configure your local repository:

![github-create-repo-03](./assets/media/remotes_step_01_images/github-create-repo-03.png)

This effectively does the following on GitHub’s servers:

```console
$ mkdir planets
$ cd planets
$ git init
```

If you remember back to the earlier episode where we added and committed our earlier work on mars.txt, we had a diagram of the local repository which looked like this:

![git-staging-area-04](./assets/media/remotes_step_01_images/git-staging-area-04.svg)

Now that we have two repositories, we need a diagram like this:

![git-freshly-made-github-repo-05](./assets/media/remotes_step_01_images/git-freshly-made-github-repo-05.svg)

Note that our local repository still contains our earlier work on mars.txt, but the remote repository on GitHub appears empty as it doesn’t contain any files yet.

## Connect local to remote repository

Now we connect the two repositories. We do this by making the GitHub repository a remote for the local repository. The home page of the repository on GitHub includes the URL string we need to identify it:

![github-find-repo-string-01](./assets/media/remotes_step_02_images/github-find-repo-string-01.png)

Click on the ‘SSH’ link to change the protocol from HTTPS to SSH.

![github-change-repo-string-02](./assets/media/remotes_step_02_images/github-change-repo-string-02.png)

Copy that URL from the browser, go into the local planets repository, and run this command:


```console
$ git remote add origin git@github.com:vlad/planets.git
```

Make sure to use the URL for your repository rather than Vlad’s: the only difference should be your username instead of `vlad`.

`origin` is a local name used to refer to the remote repository. It could be called anything, but `origin` is a convention that is often used by default in git and GitHub, so it’s helpful to stick with this unless there’s a reason not to.

We can check that the command has worked by running `git remote -v`:

```console
$ git remote -v
```

```output
origin   git@github.com:vlad/planets.git (fetch)
origin   git@github.com:vlad/planets.git (push)
```

We’ll discuss remotes in more detail in the next episode, while talking about how they might be used for collaboration.


## Push local changes to a remote

Now that authentication is setup, we can return to the remote. This command will push the changes from our local repository to the repository on GitHub:

```console
$ git push origin main
```

Since Dracula set up a passphrase, it will prompt him for it. If you completed advanced settings for your authentication, it will not prompt for a passphrase.


```output
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 8 threads.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (16/16), 1.45 KiB | 372.00 KiB/s, done.
Total 16 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/vlad/planets.git
 * [new branch]      main -> main
```


<div class = 'help'>
### Proxy
  
If the network you are connected to uses a proxy, there is a chance that your last command failed with “Could not resolve hostname” as the error message. To solve this issue, you need to tell Git about the proxy:
 
```console
$ git config --global http.proxy http://user:password@proxy.url
$ git config --global https.proxy https://user:password@proxy.url
```

When you connect to another network that doesn’t use a proxy, you will need to tell Git to disable the proxy using:
  
    ```console
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```
  
</div>

<div class = 'care'>
**Password Managers**
  
If your operating system has a password manager configured, git push will try to use it when it needs your username and password. For example, this is the default behavior for Git Bash on Windows. If you want to type your username and password at the terminal instead of using a password manager, type:
 
  ```console
$ unset SSH_ASKPASS
```

in the terminal, before you run `git push`. Despite the name, Git uses SSH_ASKPASS for all credential entry, so you may want to unset `SSH_ASKPASS` whether you are using Git via SSH or https.

You may also want to add `unset SSH_ASKPASS` at the end of your `~/.bashrc` to make Git default to using the terminal for usernames and passwords.
  
</div>


Our local and remote repositories are now in this state:

![github-repo-after-first-push_01](./assets/media/remotes_step_03_images/github-repo-after-first-push_01.svg)

<div class = 'care'>
**the -u flag**

You may see a -u option used with git push in some documentation. This option is synonymous with the --set-upstream-to option for the git branch command, and is used to associate the current branch with a remote branch so that the git pull command can be used without any arguments. To do this, simply use git push -u origin main once the remote has been set up.
  
</div>  

We can pull changes from the remote repository to the local one as well:

  ```console
$ git pull origin main
```

  ```output
From https://github.com/vlad/planets
 * branch            main     -> FETCH_HEAD
Already up-to-date.
```

Pulling has no effect in this case because the two repositories are already synchronized. If someone else had pushed some changes to the repository on GitHub, though, this command would download them to our local repository.

### Quiz: GitHub GUI

Browse to your `planets` repository on GitHub. Under the Code tab, find and click on the text that says “XX commits” (where “XX” is some number). Hover over, and click on, the three buttons to the right of each commit. What information can you gather/explore from these buttons? How would you get that same information in the shell?

[[GitHub GUI]]
***
<div class = "answer">
The left-most button (with the picture of a clipboard) copies the full identifier of the commit to the clipboard. In the shell, `git log` will show you the full commit identifier for each commit.

When you click on the middle button, you’ll see all of the changes that were made in that particular commit. Green shaded lines indicate additions and red ones removals. In the shell we can do the same thing with `git diff`. In particular, `git diff ID1..ID2` where ID1 and ID2 are commit identifiers (e.g. `git diff a3bf1e5..041e637`) will show the differences between those two commits.

The right-most button lets you view all of the files in the repository at the time of that commit. To do this in the shell, we’d need to checkout the repository at that particular time. We can do this with git checkout ID where ID is the identifier of the commit we want to look at. If we do this, we need to remember to put the repository back to the right state afterwards!
</div>
***

<div class = 'care'>
**Uploading files directly in GitHub browser**
  
Github also allows you to skip the command line and upload files directly to your repository without having to leave the browser. There are two options. First you can click the “Upload files” button in the toolbar at the top of the file tree. Or, you can drag and drop files from your desktop onto the file tree. You can read more about this on [this GitHub page](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
  
</div>

### Quiz: GitHub Timestamp

Create a remote repository on GitHub. Push the contents of your local repository to the remote. Make changes to your local repository and push these changes. Go to the repo you just created on GitHub and check the timestamps of the files. How does GitHub record times, and why?

[[GitHub Timestamp]]
***
<div class = "answer">
GitHub displays timestamps in a human readable relative format (i.e. “22 hours ago” or “three weeks ago”). However, if you hover over the timestamp, you can see the exact time at which the last change to the file occurred.
</div>
***

### Quiz: Push vs. Commit

In this module, we introduced the “git push” command. How is “git push” different from “git commit”?

[[Push vs. Commit]]
***
<div class = "answer">
When we push changes, we’re interacting with a remote repository to update it with the changes we’ve made locally (often this corresponds to sharing the changes we’ve made with others). Commit only updates your local repository.
</div>
***


### Quiz: GitHub license and README files

In this module, we learned about creating a remote repository on GitHub, but when you initialized your GitHub repo, you didn’t add a README.md or a license file. If you had, what do you think would have happened when you tried to link your local and remote repositories?

[[GitHub license and README files]]
***
<div class = "answer">
In this case, we’d see a merge conflict due to unrelated histories. When GitHub creates a README.md file, it performs a commit in the remote repository. When you try to pull the remote repository to your local repository, Git detects that they have histories that do not share a common origin and refuses to merge.

   ```console
$ git pull origin main
```
  
     ```output
warning: no common commits
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/vlad/planets
 * branch            main     -> FETCH_HEAD
 * [new branch]      main     -> origin/main
fatal: refusing to merge unrelated histories
```
  
</div>
***

## Wrap-Up 
- A local Git repository can be connected to one or more remote repositories.
- Use the SSH protocol to connect to remote repositories.
- `git push` copies changes from a local repository to a remote repository.
- `git pull` copies changes from a remote repository to a local repository.



## Additional Resources

To learn more about SSH and its setup, refer to the Software carpentries episode [here](https://swcarpentry.github.io/git-novice/07-github/index.html#3-ssh-background-and-setup).


## Feedback

In the beginning, we stated some goals.

**Learning Objectives:**

@learning_objectives

We ask you to fill out a brief (5 minutes or less) survey to let us know:

* If we achieved the learning objectives
* If the module difficulty was appropriate
* If we gave you the experience you expected

We gather this information in order to iteratively improve our work.  Thank you in advance for filling out [our brief survey](https://redcap.chop.edu/surveys/?s=KHTXCXJJ93&module_name=%22Module+Template%22)!

Remember to change the redcap link so that the module name is correct for this module!
