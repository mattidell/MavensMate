#MavensMate v2.0

##Background

###Version 0.x
The first version of MavensMate was a TextMate 1.5+ plugin, written mostly in Ruby, that enabled the creation of Salesforce.com-connected projects and the manipulation & deployment of certain elements of metadata.

###Version 1.x (current)
The delayed release of TextMate 2.0 along with the momentum of Sublime Text became the impetus for re-focusing development efforts away from TextMate. The Sublime Text plugin represents a major leap forward from a UX perspective and is currently in regular use by many developers (4,000+ downloads).

###Version 2.x
MavensMate v2.0 represents a fundamental shift in the way the tool is delivered & utilized. The grand vision is to deliver a cross-platform executable that is called directly by client "plugins" (e.g. a native Notepad++ plugin that executes commands like "compile file" "delete file" "deploy package", etc). The good news is that the first plugin is essentially already written (MavensMate-Sublime Text).

##Testing
We'll use the out of box testing framework for Python: http://docs.python.org/2/library/unittest.html

###Salesforce.com credentials to use for testing
username: mm@force.com
password: force

##Some Notes
- We need to explore how to effectively deliver our application
  * Do we need a mavensmate process to be running at all times?
  * If not, what is the performance impact of calling mavensmate from the terminal?
- Is a local HTTP server the most effective way to deliver communication between MavensMate UIs (new/edit project, deploy to server, etc)?
- We're using pyinstaller to build a platform independent binary (more to come)