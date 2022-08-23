# viewhtmlmail
Simple utility to easily view HTML mail from mutt in your default (graphical) browser

## Installation:

* clone this repository
* `pipenv install`
* link `viewhtmlmail` from your virtualenv PATH somewhere in to your main PATH
* configure mutt

For example, put
```
macro index,pager H     "<pipe-message>viewhtmlmail<enter>" "render html mail using viewhtmlmail"
```
in your `muttrc`-file.
