# Project 1 : Essay

### Link to Project 1 Scores https://github.com/aditikilledar/csc-510-se/blob/main/Project1_Scores.md

---
# Essay 

As part of our Project 1, we reviewed five projects: Auto-anki, DollarBot, CheapBuy, GITS, and Teacher’s Pet Bot. Getting each of them to run came with their difficulties. Some lacked adequate developer and user documentation, some lacked clarity, and some documentation was too short. Our team of 4 consists of 2 MacOS and 2 Windows users, so one of our main challenges was getting the software to work on both OS. 

The first project we ran was GITS - a tool to make working with Git a lot simpler. We tried getting it to work on MacOS and Windows. Still, we faced a few issues: One, since MacOS no longer uses bash, following the “bash”-oriented installation documentation was difficult. This issue could have been avoided by spelling out specific installation instructions for the different OS supported by the package. Two, the documentation misses a short tutorial for running the ‘gits’ commands and instead delivers a paragraph about what it’s supposed to do. User experience could be elevated by including a few GIFs or code examples showing it working. 

We got the second project, Auto-anki, to work on Windows systems; however, it posed a more significant challenge on MacOS. The biggest problem was that the requirements.txt file could not correctly install most required libraries. It was a painstaking process, installing specific versions of missing libraries individually. Improving this situation would require attention to crafting the requirements.txt. 
Even on Windows, installation wasn’t straightforward. The auto-anki repo does not contain a video explaining how to run the software and its use cases. The video on the repo only advertises the new features developed over the previous version but does not show us how one would run it. There are no sample files available to test if the software works. We have to generate our files. Since a new user of the software would not know what the expected output will be, one can only guess. To run the auto-anki software, we had to go through the repo docs on top of which auto-anki was built/extended—the older repository contained instructions on how to run their software version. We needed to intuitively understand how that would translate to the project built upon it with significant changes. To resolve this, it would help to add a “user manual” or a video tutorial explaining how to use the software. 

The third project, CheapBuy, has beautiful documentation, engaging storytelling, and a table of contents. However, we were not able to run and use CheapBuy. The requirements.txt has no versions for the libraries specified and installs a different version of some libraries, which gives rise to errors. The software only uses the driver managers for the Chrome browser. Moreover, the documentation does not provide any help for common issues that users could face, such as updating web drivers. It was challenging to get started with CheapBuy with ease as a user.

The fourth project, Teacher’s Pet, is a Discord Bot that streamlines Discord servers for teachers and students with features like the automatic creation of graphs, email configuration, and grading of quizzes. The repository of the project is well-formatted and easy to read. Going over the project’s readme gives an excellent idea about the tool. It has a detailed explanation of how to install and run the project and the specifications of all the commands that can be run on it. 

It was challenging to run the project as it had missing .dll files because the libraries are old and have not been updated. Determining missing files or which libraries have updated files will take a lot of effort. This could have been avoided if the project was always up to date with its current dependency versions.  

Finally, DollarBot is supported cross-platform, and the installation and running instructions were almost perfect. However, it requires a shell script execution, but no information is provided to get it running on Windows systems or its workarounds. We used Cygwin to run the scripts, but since Git converts EOL based on the system, we have to make sure that EOL follows unix conventions to run on Cygwin. The software also has a lot of bugs, and some edge cases are not considered, causing it to crash. Following the repo instructions, the telegram bot runs with the API key hardcoded into the .properties file. Pushing private API keys into a public repository is a terrible practice and can be misused.

Although this software has its issues, we chose it as our intended project for project two because it is OS agnostic and has potential for improvement.
We have planned some preliminary changes in our iteration of dollarBot:
- Introducing platform-specific running instructions to alleviate a user’s trouble while getting started. 
- Introduce a file for environment variables so sensitive information such as private API keys are not pushed into the repo.
- Making a walkthrough video demonstrating the software’s functionality to help users know how to try it out. 
- To include documentation of common issues a new user might encounter due to their environment or system configurations. (Of couse, we aim to build software that does not pose any problems in the first place.)
- Edge case coverage. A project that can be successfully built and run is not our only goal. Ensuring all edge cases are taken care of, and the software functions as expected without crashing is also essential in guaranteeing user satisfaction.
- Publishing some common workflows that simulate user stories and real-world use cases.

After reviewing and understanding the pain points of installing and working with the projects we were assigned, we now realize the importance of having clear, concise documentation: not just the what but also the how and why. We also have a new appreciation for tracked bugs, well-documented issues, clear installation instructions, and high code quality. We will use our learnings and ensure nobody using our version of DollarBot has to face the problems we had while using it.
