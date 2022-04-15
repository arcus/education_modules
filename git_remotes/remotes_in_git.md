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
- Push to and pull from a remote repository

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


* A [GitHub](https://github.com/) account
* (Preferred) Completion of [Intro to Version Control](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_intro/git_intro.md#1) and [Creating a Git Repository](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/git_creation_and_tracking/git_creation_and_tracking.md#1) modules

**Learning Objectives**

@learning_objectives


</div>

## Lesson Preparation

Open a web browser, like Chrome or Firefox and navigate to github.com.

## Create a remote repository

We will be creating a remote version of the `planets` repository we worked with in the previous lessons. We will then connect our remote version to our local version of the `planets` repository. 

Log in to [GitHub](github.com), then click on the icon in the top right corner to create a new repository:

![github-create-repo-01](./media/remotes_step_01_images/github-create-repo-01.png)

Name your repository “planets” and then click “Create Repository”.

<div class = "warning">
Since this repository will be connected to a local repository, it needs to be empty. Leave “Initialize this repository with a README” unchecked, and keep “None” as options for both “Add .gitignore” and “Add a license.” See the “GitHub License and README files” exercise below for a full explanation of why the repository needs to be empty.
</div>

![github-create-repo-02](./media/remotes_step_01_images/github-create-repo-02.png)


As soon as the repository is created, GitHub displays a page with a URL and some information on how to configure your local repository:

![github-create-repo-03](./media/remotes_step_01_images/github-create-repo-03.png)

This effectively does the following on GitHub’s servers:

```console
$ mkdir planets
$ cd planets
$ git init
```

If you remember back to the earlier episode where we added and committed our earlier work on mars.txt, we had a diagram of the local repository which looked like this:

![git-staging-area-04](./media/remotes_step_01_images/git-staging-area-04.svg)

Now that we have two repositories, we need a diagram like this:

![git-freshly-made-github-repo-05](./media/remotes_step_01_images/git-freshly-made-github-repo-05.svg)

<div class = "important">
Note that our local repository still contains our earlier work on mars.txt, but the remote repository on GitHub appears empty as it doesn’t contain any files yet.
</div>

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

## Connect local to remote repository

Now we connect the two repositories. We do this by making the GitHub repository a remote for the local repository. The home page of the repository on GitHub includes the URL string we need to identify it:

![github-find-repo-string-01](./media/remotes_step_02_images/github-find-repo-string-01.png)

Click on the ‘SSH’ link to change the protocol from HTTPS to SSH.

![github-change-repo-string-02](./media/remotes_step_02_images/github-change-repo-string-02.png)

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

### SSH

Before Dracula can connect to a remote repository, he needs to set up a way for his computer to authenticate with GitHub so it knows it’s him trying to connect to his remote repository. Additionally, we use SSH here because, while it requires some additional configuration, it is a security protocol widely used by many applications.

We are going to set up the method that is commonly used by many different services to authenticate access on the command line. This method is called Secure Shell Protocol (SSH). SSH is a cryptographic network protocol that allows secure communication between computers using an otherwise insecure network.

SSH uses what is called a key pair. This is two keys that work together to validate access. One key is publicly known and called the public key, and the other key called the private key is kept private. Very descriptive names.

You can think of the public key as a padlock, and only you have the key (the private key) to open it. You use the public key where you want a secure method of communication, such as your GitHub account. You give this padlock, or public key, to GitHub and say “lock the communications to my account with this so that only computers that have my private key can unlock communications and send git commands as my GitHub account.”

What we will do now is the minimum required to set up the SSH keys and add the public key to a GitHub account.

<div class = "warning"> 
Github no longer supports password authentication as of August 2021. If you do try to use HTTPS to connect to remote you will encounter the error: 
<code>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/vlad/planets.git/</code>
</div>

### SSH Setup

The first thing we are going to do is check if this has already been done on the computer you’re on. Because generally speaking, this setup only needs to happen once and then you can forget about it.

<div class = "care"> 
**Keeping your keys secure**
You shouldn’t really forget about your SSH keys, since they keep your account secure. It’s good practice to audit your secure shell keys every so often. Especially if you are using multiple computers to access your account.
</div>

We will run the list command to check what key pairs already exist on your computer.

```console 
ls -al ~/.ssh
```
Your output is going to look a little different depending on whether or not SSH has ever been set up on the computer you are using.

Dracula has not set up SSH on his computer, so his output is
```console 
ls: cannot access /c/Users/Vlad Dracula/.ssh: No such file or directory
```

If SSH has been set up on the computer you’re using, the public and private key pairs will be listed. The file names are either `id_ed25519/id_ed25519.pub` or `id_rsa/id_rsa.pub` depending on how the key pairs were set up.


#### Create an SSH key pair 

To create an SSH key pair Vlad uses this command, where the -t option specifies which type of algorithm to use and -C attaches a comment to the key (here, Vlad’s email):

```console 
ssh-keygen -t ed25519 -C "vlad@tran.sylvan.ia"
```
<div class = "help">
If you are using a legacy system that doesn’t support the Ed25519 algorithm, use: `$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
</div>

```output 
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/Vlad Dracula/.ssh/id_ed25519):
```

We want to use the default file, so just press `Enter`.

```output 
Created directory '/c/Users/Vlad Dracula/.ssh'.
Enter passphrase (empty for no passphrase):
```

Now, it is prompting Dracula for a passphrase. Since he is using his lab’s laptop that other people sometimes have access to, he wants to create a passphrase. Be sure to use something memorable or save your passphrase somewhere, as there is no “reset my password” option.
```output 
Enter same passphrase again:
```

After entering the same passphrase a second time, we receive the confirmation

```console
Your identification has been saved in /c/Users/Vlad Dracula/.ssh/id_ed25519
Your public key has been saved in /c/Users/Vlad Dracula/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:SMSPIStNyA00KPxuYu94KpZgRAYjgt9g4BA4kFy3g1o vlad@tran.sylvan.ia
The key's randomart image is:
+--[ED25519 256]--+
|^B== o.          |
|%*=.*.+          |
|+=.E =.+         |
| .=.+.o..        |
|....  . S        |
|.+ o             |
|+ =              |
|.o.o             |
|oo+.             |
+----[SHA256]-----+
```

The “identification” is actually the private key. You should never share it. The public key is appropriately named. The “key fingerprint” is a shorter version of a public key.

Now that we have generated the SSH keys, we will find the SSH files when we check.

```console 
ls -al ~/.ssh
```
```output 
drwxr-xr-x 1 Vlad Dracula 197121   0 Jul 16 14:48 ./
drwxr-xr-x 1 Vlad Dracula 197121   0 Jul 16 14:48 ../
-rw-r--r-- 1 Vlad Dracula 197121 419 Jul 16 14:48 id_ed25519
-rw-r--r-- 1 Vlad Dracula 197121 106 Jul 16 14:48 id_ed25519.pub
```

#### Copy public key to GitHub

Now we have a SSH key pair and we can run this command to check if GitHub can read our authentication.

```console 
ssh -T git@github.com
```
```output 
The authenticity of host 'github.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added 'github.com' (RSA) to the list of known hosts.
git@github.com: Permission denied (publickey).
```

Right, we forgot that we need to give GitHub our public key!

First, we need to copy the public key. Be sure to include the `.pub` at the end, otherwise you’re looking at the private key.

```console 
cat ~/.ssh/id_ed25519.pub
```
```output 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDmRA3d51X0uu9wXek559gfn6UFNF69yZjChyBIU2qKI vlad@tran.sylvan.ia
```

Now, going to GitHub.com, click on your profile icon in the top right corner to get the drop-down menu. Click “Settings,” then on the settings page, click “SSH and GPG keys,” on the left side “Account settings” menu. Click the “New SSH key” button on the right side. Now, you can add the title (Dracula uses the title “Vlad’s Lab Laptop” so he can remember where the original key pair files are located), paste your SSH key into the field, and click the “Add SSH key” to complete the setup.

Now that we’ve set that up, let’s check our authentication again from the command line.

```console 
$ ssh -T git@github.com
```
```output 
Hi Vlad! You've successfully authenticated, but GitHub does not provide shell access.
```

## Push and pull local changes to and from a remote

Pushing and pulling changes are a key part of the Git workflow. 

**Pushing** local changes to a remote repository means you are making your local changes accessible to the remote branch and therefore to anyone with access to that remote repository. 

**Pulling** remote changes into your local repository means you are getting any changes pushed to the remote repository and using the files in that state to perform add your own changes. 

Remebering to push and pull changes is especially important when collaborating with others. Others cannot see or work with your changes if you do not push them. You may be working from an outdated version of your repository if you do not pull changes prior to starting out. Forgetting one or both of these steps may lead to conflicts in Git. 

### Push local changes to a remote

Now that authentication is setup, we can return to the remote. This command will push the changes from our local repository to the repository on GitHub:

```console
git push origin main
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

Our local and remote repositories are now in this state:

![github-repo-after-first-push01](./media/remotes_step_03_images/github-repo-after-first-push_01.svg)

### Pull remote changes to a local

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

### Quiz: Push vs. Commit

In this module, we introduced the “git push” command. How is “git push” different from “git commit”?

[[Push vs. Commit]]
***
<div class = "answer">
When we push changes, we’re interacting with a remote repository to update it with the changes we’ve made locally (often this corresponds to sharing the changes we’ve made with others). Commit only updates your local repository.
</div>
***


## GitHub GUI

The GitHub GUI, or Graphical User Interface, in the browser allows you to perform many tasks you are also able to do on the command line. 

**Uploading files directly in GitHub browser**
<br>
<br>  
Github also allows you to skip the command line and upload files directly to your repository without having to leave the browser. There are two options. First you can click the “Upload files” button in the toolbar at the top of the file tree. Or, you can drag and drop files from your desktop onto the file tree. You can read more about this on [this GitHub page](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

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


### Quiz: GitHub Timestamp

Create a remote repository on GitHub. Push the contents of your local repository to the remote. Make changes to your local repository and push these changes. Go to the repo you just created on GitHub and check the timestamps of the files. How does GitHub record times, and why?

[[GitHub Timestamp]]
***
<div class = "answer">
GitHub displays timestamps in a human readable relative format (i.e. “22 hours ago” or “three weeks ago”). However, if you hover over the timestamp, you can see the exact time at which the last change to the file occurred.
</div>
***

## Wrap-Up 
- A local Git repository can be connected to one or more remote repositories.
- Use the SSH protocol to connect to remote repositories.
- `git push` copies changes from a local repository to a remote repository.
- `git pull` copies changes from a remote repository to a local repository.



## Additional Resources

To learn more about SSH and its setup, refer to the Software carpentries episode [here](https://swcarpentry.github.io/git-novice/07-github/index.html#3-ssh-background-and-setup).


### Proxy
  
If the network you are connected to uses a proxy, there is a chance that your last command failed with “Could not resolve hostname” as the error message. To solve this issue, you need to tell Git about the proxy:
``` console  
$ git config --global http.proxy http://user:password@proxy.url
$ git config --global https.proxy https://user:password@proxy.url<code>Testing hint box
```
  
When you connect to another network that doesn’t use a proxy, you will need to tell Git to disable the proxy using:<br>
``` console  
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```

### Password Managers
  
If your operating system has a password manager configured, git push will try to use it when it needs your username and password. For example, this is the default behavior for Git Bash on Windows. If you want to type your username and password at the terminal instead of using a password manager, type:
 
```console
$ unset SSH_ASKPASS
```

in the terminal, before you run `git push`. Despite the name, Git uses SSH_ASKPASS for all credential entry, so you may want to unset `SSH_ASKPASS` whether you are using Git via SSH or https.

You may also want to add `unset SSH_ASKPASS` at the end of your `~/.bashrc` to make Git default to using the terminal for usernames and passwords. 

### The -u flag

You may see a `-u` option used with git push in some documentation. This option is synonymous with the `--set-upstream-to option` for the git branch command, and is used to associate the current branch with a remote branch so that the git pull command can be used without any arguments. To do this, simply use git push `-u origin main` once the remote has been set up.


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
