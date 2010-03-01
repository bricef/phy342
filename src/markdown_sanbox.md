Various stuff
=========
Note that an html version of this email is available [here](http://phy342.googlecode.com/hg/html/markdown_sandbox.html)

Mercurial
-------------

Ok, the mercurial website is [here](http://mercurial.selenic.com/)

The basics are very well explained on the website. In particular, have a look at the [guide](http://mercurial.selenic.com/guide/) or the [quickstart](http://mercurial.selenic.com/quickstart/)

Simple usage goes something like:

1. Create a new repository from the existing one on googlecode  (a repository, or repo for short, is just a place where mercurial keeps the versions of the files.) To do that, open a command prompt and type

    <code>hg clone https://phy342.googlecode.com/hg/ phy342</code>
    
    You should now have a folder called phy342 in which all the program files are.

2. Make some modification, add some files, remove some files, etc...

3. Now, "commit" your changes to the local repository (committing your changes means that you tell mercurial to save your work as a new revision/version)

    <code>hg addremove </code> This adds/remove files from the repo. For example, if you create a new file for the capacitor, then mercurial will add that file to the repo

    You have to do this because the _repo_ is different from the _local copy_. The repo is where mercurial keeps all the information, the changes, etc, while the local copy is what you work on. The repo is actually in a file called ".hg" that will be created for you.
    
     then, <code>hg commit -m "commit message" </code> This will transfer your changes from the local copy to your repository. You'll need to have a ".hgrc" file somewhere that gives a username. The guide explain what should be in it. I'll help you out with setting up your ".hgrc" if you want. Ring me and I'll pop on msn or something.

4. Now, "push" your changes to the googlecode repo. To do this type:

    <code>hg push https://phy432.googlecode.com/hg/</code>

    This will send your work to the google servers. You'll have to use your username and password, which you'll get from the googlecode website. 

5. If you'd rather not use the command line, have a look at [tortoiseHg](http://tortoisehg.bitbucket.org/), which integrates with explorer directly. It depends on your level of comfort with the windows prompt. 

Markdown
---------------
Markdown is just a mark-up language that does the same as html, but in a form that is readable as plain text, without the unsightly tags. For example, this email is valid markdown and I've added it to the project as "markdown_sanbox.md" so that you can see what it will look like i've pre-compiled it so you can have a look at the final result [here](http://phy342.googlecode.com/hg/html/markdown_sandbox.html). you can find more about it on the [markdown page](http://daringfireball.net/projects/markdown/) or on [wikipedia](http://en.wikipedia.org/wiki/Markdown).

Compiling the website
--------------------------------
Markdown pages are compiled into html using a little utility I wrote in python. you have to run the bat script called "makesite.bat" in the "utils" folder. It's actually only one line, and you could just as easily type <code>python Makefile.py ..\src\ ..\html\ </code> instead. It might or might not work. I haven't tested it on windows. If it doesn't work, or if you don't want to go to the trouble of installing python, markdown, etc... then don't bother generating the html, I'll do that when needed.

Folder structure
-----------------------

    /phy342/
        /src/
        /utils/
        /html/
        /static/
        /resources/

+ "src" contains the markdown files with a ".md" extension. They're just plain text files.
+ "utils" contains the scripts that turn the markdown website into html
+ "html" contains the final html files. they are copies of the markdown files except that they have the .html extension and have been parsed.
+ "static" contains the CSS files and the html template from which the website is build.
+ "resources" contains extra files that are included, such as circuit diagrams, pictures, etc...


Ok, I hope this covers everything. Let me know if I missed something.

See you at uni,

Brice




