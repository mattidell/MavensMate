# [MavensMate](http://mavensmate.com)

MavensMate is a powerful open source tool for building Force.com IDEs. Develop Force.com applications in your favorite text editors, like Sublime Text. MavensMate is created and maintained by [Joe Ferraro](http://twitter.com/joeferraro).

To get started, check out [http://mavensmate.com](http://mavensmate.com)!

## Contributing

MavensMate is currently comprised of two open source projects: the underlying API (called `mm`) and the plugin for Sublime Text.

### mm

`mm` is the command line tool (written in Python, "compiled" with PyInstaller) that's responsible for interacting with the file system and various Force.com IDEs. Its goal is to make it simple to create IDEs for Force.com by abstracting many of the complicated aspects like indexing, file system interaction, REST/SOAP calls, etc.

[To the code...][mmgithub]

### MavensMate for Sublime Text

MavensMate for Sublime Text is a Sublime Text plugin that uses the `mm` command line tool to provide a rich IDE experience in the editor. The bulk of the MM for ST codebase is used focused on integration with the Sublime Text APIs. The interaction with the Force.com APIs are still handled by `mm`.

[MavensMate for Sublime Text][stp]

## Bugs and feature requests

Have a bug or a feature request? [Please open a new issue](https://github.com/joeferraro/mavensmate/issues). Before opening any issue, please search for existing issues.

**Always include your MavensMate version number(s) (for example, MavensMate.app v0.35.1 and MavensMate for Sublime Text 3.0.8) AND plugin client version number (for example, Sublime Text 3 build 3051) when submitting issues.**

## Documentation

MavensMate's documentation is built with [Daux.io](http://daux.io) and publicly available on [http://mavensmate.com][docs].

## Plugins

If you're looking for the Sublime Text plugin, head here > [Sublime Text Plugin][stp]

<img src="http://cdn.mavensconsulting.com/mavensmate/img/mm-bg.jpg"/>

[mmcom]: http://mavensmate.com/?utm_source=github&utm_medium=mavensmate&utm_campaign=api
[docs]: http://mavensmate.com/Getting_Started/Developers
[stp]: https://github.com/joeferraro/MavensMate-SublimeText
[mmgithub]: https://github.com/joeferraro/mm
