Pex
===
Pex manages template directories for your projects.
Think of pex as a glorified cp -R.

Let's say you want to start a new Beamer presentation
for presenting the results of your thesis.
Pex allows you to just say:

    $ pex new beamer-presentation thesis-results

You've just created a directory called `thesis-results`
that contains the skeleton for your presentation!
I'll tell you right away
how you install that template in the first place.

Pex understands that anything can serve as a template for something.
For example, a Zip file:

    $ pex new ~/Download/project-template.zip sales-project

Or even a plain directory:

    $ pex new ~/c-program/ tetris-game

Pex also knows how to get your templates from the web.
You can upload a template for anyone to use it:

    $ pex new http://your.website.com/files/photo-gallery.zip 2009-vacation

Soon you'll get tired of typing such a long URL,
so you'll want to install the template:

    $ pex install http://your.website.com/files/photo-gallery.zip gallery
    $ pex new gallery 2010-roadtrip

Pex makes it convenient for you to host your templates on Github:

    $ pex new gh:rbonvall/simple-website 

Disclaimer
----------
Whenever I say «pex does X»,
what I really mean is «it will when X gets implemented».
It's not lazyness, it's [RDD](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html).

Author
------
Roberto Bonvallet <rbonvall@gmail.com>

License
-------
Something free and liberal. I'll pick one some day.

