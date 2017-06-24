![MagiCircles](http://i.imgur.com/67S7coa.png)

MagiCircles
=====

MagiCircles is a web framework to build collections databases and social network websites.

Its core features are:
- Collections: a powerful way to link a database table and its views item/list/add/edit
- A full-featured social network: activities, likes, comments, notifications, ...
- Customizable profiles
- Many pages provided by default: map, wiki, ...
- A default layout made with Bootstrap
- Very few lines of code required to get a full featured website
- Highly customizable to fit your needs
- Translated in many languages

![](http://i.imgur.com/DfNfUYB.png)

- Based on [Django](https://www.djangoproject.com/)
- Uses: [Django-Rest-Framework](http://www.django-rest-framework.org/), [Tinyfy](https://github.com/tinify/tinify-python), [Bootstrap](http://getbootstrap.com/), [jQuery](https://jquery.com/), [Bower](https://bower.io/)
- And more, see `requirements.txt` and `sample_project/bower.json`

[![](http://i.imgur.com/oQbvhxD.png)](http://i.imgur.com/oQbvhxD.png)

It's open source and open for contributions.

If you plan to create your own website using MagiCircles, you might want to know that you won't be able to monetize it, and it's probably easier for you if you join the MagiCircles family.

Join the MagiCircles family
----------------

We have a group of over 150 people who all work together to maintain and grow websites made with MagiCircles.

If you want to start a website with MagiCircles, we recommend you to join us:
- [The author of MagiCircles](http://db0.company) will help you develop it. No matter your level in programming, we'll make sure we get things done together.
- You'll be allowed to ask our teams of artists and designers to help you with the design of your website, as well as future graphic needs once the website starts.
- Our team of translators will translate the website for you.
- You won't need to worry about hosting the website and administrate its server and infrastructure.
- You won't need to worry about covering the server(s) cost.
- If the MagiCircles can afford it, you may be able to organize giveaways and games, which costs will be covered by the MagiCircles family.
- You'll have opportunities to meet great people who might even want to join your staff team to help you grow and maintain your website.

### [→ Join the MagiCircles family ←](https://goo.gl/forms/EDS5mAZ0eevGlpF82)

![](http://i.imgur.com/nsFXA0Z.png)

#### Not interested?

[The author of MagiCircles](http://db0.company) needs to monetize the platforms, pay for the servers and pay for the development time needed to make these websites and this framework available.

For this reason, it is not allowed to monetize your website if you are using MagiCircles yourself, outside of the MagiCircles family. Only [the author of MagiCircles](http://db0.company) is allowed to monetize websites that use MagiCircles, except when given excplicit authorization.

2 MagiCollections are provided in MagiCircles, but disabled by default: `BadgeCollection` and `DonateCollection`. Both are used to monetize the websites, and you are therefore not allowed to enable them if you are not part of the MagiCircles family.

Similarly, it is not allowed to monetize a website that uses MagiCircles using any other method, including but not limited to:
- advertisment on the website itself and any other platforms that depend on the website,
- receiving money donations within the website or using an external platform for the website itself,
- activating advertisments on disqus,
- raising funds from any kind of events or campaign,
- receiving cards or special codes that can be exchanged for money as part of the website,
- receiving money for the website.

# Table of content

1. [Start a new website](#start-a-new-website)
    1. [Requirements](#requirements)
    1. [Quick Start](#quick-start)
    1. [Full starting guide](#full-starting-guide)
    1. [Start coding!](#start-coding)
    1. [Frequent problems](#frequent-problems)
1. [Files tree](#files-tree)
1.  [Website Settings](#website-settings)
1. [Collections](#collections)
    1. [Models](#models)
      	1. [Inherit from MagiModel and provide a name](#inherit-from-itemModel-and-provide-a-name)
	    1. [Have an owner](#have-an-owner)
	    1. [Override `__unicode__`](#override-unicode-)
    1. [MagiCollection](#magicollection)
      	1. [Views](#views)
            1. [All views](#all-views)
            1. [List view](#list-view)
            1. [Item view](#item-view)
            1. [Add view](#add-view)
            1. [Edit view](#edit-view)
        1. [Collectible](#collectible)
        1. [CuteForm](#cuteform)
        1. [Item types](#item-types)
        1. [to_field method](#to-field-method)
    1. [MagiForm](#magiform)
    1. [MagiFilter](#magifilter)
1. [Enabled Pages](#enabled-pages)
1. [Default pages and collections](#default-pages-and-collections)
    1. [Default pages](#default-pages)
    1. [Default collections](#default-collections)
        1. [Collections disabled by default](#collections-disabled-by-default)
    1. [Enable/Disable/Configure default pages and collections](#enabledisableconfigure-default-pages-and-collections)
1. [Nav bar lists](#nav-bar-lists)
1. [API](#api)
1. [Utils](#utils)
    1. [Python](#python)
        1. [Models upload](#models-upload)
        1. [Access MagiCollections](#access-magicollections)
    1. [Templates](#templates)
    1. [Javascript](#javascript)
1. [Recommendations](#recommendations)
    1. [Internal cache for foreign keys in models](#internal-cache-for-foreign-keys-in-models)
    1. [Calling functions in templates](#calling-functions-in-templates)
    1. [Utility functions for models](#utility-functions-for-models)
    1. [Generated Settings](#generated-settings)
    1. [Avoid generating translation terms for terms already available in Django framework](#avoid-generating-translation-terms-for-terms-already-available-in-django-framework)
    1. [Disable activities](#disable-activities)
    1. [Disable activities but keep news for staff members](#disable-activities-but-keep-news-for-staff-members)
1. [Production Environment](#production-environment)
1. [Flaticon](#flaticon)
1. [Translations](#translations)

Start a new website
==========

Requirements
------------

- Debian, Ubuntu, and variants:

  ```shell
  apt-get install libpython-dev libffi-dev python-virtualenv libmysqlclient-dev libssl-dev nodejs npm
  npm install lessc bower
  ```

- Arch:

  ```shell
  pacman -S libffi python-virtualenv libmysqlclient libssl nodejs npm
  npm install lessc bower
  ```

- OS X (install [brew](https://brew.sh/) if you don't have it):

  ```shell
  brew install python node
  sudo pip install virtualenv
  npm install lessc bower
  ```

Quick start
-----------

This section allows you to get a website up and running in a few minutes. If you'd like to get a better understanding of how to set up a new MagiCircles website, skip this section and follow the section ⎡[Full Starting Guide](#full-starting-guide)⎦ instead.

1. Create a GitHub repository and copy the URL:

   ```shell
   GITHUB=git@github.com:SchoolIdolTomodachi/Hello.git
   ```

2. Pick a shortname for your website.

   ```shell
   PROJECTNAME='hello'
   ```

3. Copy the content of the folder called `sample_project` to your project:

```shell
git clone ${GITHUB}
git clone -b MagiCircles2 https://github.com/SchoolIdolTomodachi/MagiCircles.git
GITFOLDER=`echo ${GITHUB} | rev | cut -d/ -f1 | rev | cut -d. -f1`
cp -r MagiCircles/sample_project/* ${GITFOLDER}/
cp -r MagiCircles/sample_project/.bowerrc ${GITFOLDER}/
cp -r MagiCircles/sample_project/.gitignore ${GITFOLDER}/
cd ${GITFOLDER}/
```

4. Rename the files and recursively replace the string `sample` with your shortname:

   ```shell
   mv sample ${PROJECTNAME}
   mv sample_project ${PROJECTNAME}_project
   mv ${PROJECTNAME}/static/img/sample.png ${PROJECTNAME}/static/img/${PROJECTNAME}.png
   for f in `grep -rl sample . | \grep -v '.git/' | \grep -E '.py$|.json$|.bowerrc$|.gitignore$'`; do echo $f; sed -i '' -e "s/sample/${PROJECTNAME}/g" $f; done
   ```

5. Setup your local python working environment, install the dependencies and run your first website:

   ```shell
   virtualenv env
   source env/bin/activate
   pip install -r requirements.txt
   python manage.py makemigrations ${PROJECTNAME}
   python manage.py migrate
   bower install
   python manage.py runserver
   ```
   Open http://localhost:8000/
   
   ![](http://i.imgur.com/8CfckKj.png)

Full starting guide
-------------------

The ⎡[Quick Start](#quick-start)⎦ section above will do all this for you, but feel free to follow this instead if you want to understand how MagiCircles works in more details.

1. Pick a shortname for your website.
 - Example: `frgl` for [fr.gl](http://fr.gl/).
 - Everytime you see "sample" in the following instructions, replace it with this name.

2. Start a django project (the `_project` is important):
   ```shell
   django-admin startproject sample_project
   cd sample_project
   ```

3. Setup your local python working environment:
   ```shell
   virtualenv env
   source env/bin/activate
   ```

4. Create a file called requirements.txt and add MagiCircles as a requirement:
   ```txt
   git+https://github.com/SchoolIdolTomodachi/MagiCircles.git@MagiCircles2
   ```

5. Install the requirements:
   ```shell
   pip install -r requirements.txt
   ```

6. Create the app:
   ```shell
   python manage.py startapp sample
   ```

7. Edit `sample_project/settings.py` to specify your website name, add the following installed apps and middlewares, and some configuration:
   ```python
   SITE = 'sample'
   
   INSTALLED_APPS = (
     ...
     'corsheaders',
     'bootstrapform',
     'bootstrap_form_horizontal',
     'rest_framework',
     'storages',
     'magi',
   )

   MIDDLEWARE_CLASSES = (
     ...
       'django.middleware.locale.LocaleMiddleware',
       'corsheaders.middleware.CorsMiddleware',
       'django.middleware.common.CommonMiddleware',
       'magi.middleware.languageFromPreferences.LanguageFromPreferenceMiddleWare',
       'magi.middleware.httpredirect.HttpRedirectMiddleware',
   )
   
   FAVORITE_CHARACTERS = []
   
   MAX_WIDTH = 1200
   MAX_HEIGHT = 1200
   MIN_WIDTH = 300
   MIN_HEIGHT = 300

   AUTHENTICATION_BACKENDS = ('magi.backends.AuthenticationBackend',)

   DEBUG_PORT = 8000

   from django.utils.translation import ugettext_lazy as _

   LANGUAGES = (
     ('en', _('English')),
     ('es', _('Spanish')),
     ('fr', _('French')),
     ('de', _('German')),
     ('it', _('Italian')),
     ('ru', _('Russian')),
   )

   LANGUAGE_CODE = 'en'

   LOCALE_PATHS = [
     os.path.join(BASE_DIR, 'magi/locale'),
   ]

   STATIC_UPLOADED_FILES_PREFIX = None

   CORS_ORIGIN_ALLOW_ALL = True
   CORS_URLS_REGEX = r'^/api/.*$'

   LOGIN_REDIRECT_URL = '/'
   LOG_EMAIL = 'emails-log@schoolido.lu'
   PASSWORD_EMAIL = 'password@schoolido.lu'
   AWS_SES_RETURN_PATH = 'contact@schoolido.lu'

   try:
       from generated_settings import *
   except ImportError, e:
       pass
   try:
       from local_settings import *
   except ImportError, e:
       pass

   INSTALLED_APPS = list(INSTALLED_APPS)
   INSTALLED_APPS.append(SITE)

   LOCALE_PATHS = list(LOCALE_PATHS)
   LOCALE_PATHS.append(os.path.join(BASE_DIR, SITE, 'locale'))

   if STATIC_UPLOADED_FILES_PREFIX is None:
       STATIC_UPLOADED_FILES_PREFIX = 'magi/static/uploaded/' if DEBUG else 'u/'
   ```

8. Include the URLs in `sample_project/urls.py`:
   ```python
   urlpatterns = patterns('',
     url(r'^', include('magi.urls')),
     ...
   )
   ```

9. Create the file `sample/settings.py` that will describe how you want your website to look like:
   ```python
   from django.conf import settings as django_settings
   from magi.default_settings import DEFAULT_ENABLED_COLLECTIONS, DEFAULT_ENABLED_PAGES
   from sample import models, forms

   SITE_NAME = 'Sample Website'
   SITE_URL = 'http://sample.com/'
   SITE_IMAGE = 'sample.png'
   DISQUS_SHORTNAME = 'sample'
   SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.sample.com/'
   GAME_NAME = 'Sample Game'
   ACCOUNT_MODEL = models.Account
   COLOR = '#4a86e8'
   ```

10. Create a few images:
   - Your logo in `sample/static/img/sample.png`
   - The default avatar for your users in `sample/static/img/avatar.png`
   - An illustration of the game in `sample/static/img/game.png`

11. Create a django model in `sample/models.py` that will contain the info about the users game accounts:
   ```python
   from django.contrib.auth.models import User
   from django.utils.translation import ugettext_lazy as _
   from django.db import models
   from magi.item_model import MagiModel

   class Account(MagiModel):
       collection_name = 'account'
       
       owner = models.ForeignKey(User, related_name='accounts')
       creation = models.DateTimeField(auto_now_add=True)
       level = models.PositiveIntegerField(_("Level"), null=True)

       def __unicode__(self):
           return u'#{} Level {}'.format(self.id, self.level)
   ```
   Note: This model *must* contain an owner and its `related_name` *must* be `accounts`.

   Make this model available in your administration, edit `sample/admin.py`:
   ```python
   from django.contrib import admin
   from sample import models

   admin.site.register(models.Account)
   ```

15. Create the template to display an account in the leaderboard in `sample/templates/items/accountItem.html` (note: owner and owner.preferences in account item have been prefetched in the default queryset):
   ```html
   {% with account=item %}
   <br>
   <div class="well">
     <a href="{{ account.owner.item_url }}">
       <div class="row">
         <div class="col-md-2">{% include 'include/avatar.html' with av_user=account.owner av_size=30 av_image_size=100 %}</div>
         <div class="col-md-8"><h3>{{ account.owner.username }}</h3></div>
         <div class="col-md-2"><h3 class="text-right">{{ account.level }}</h3></div>
       </div>
     </a>
   </div>
   {% endwith %}
   ```

16. Create the template that will display the accounts under the users info in their profiles in `sample/templates/accountsForProfile.html`:
   ```html
   {% for item in profile_user.all_accounts %}
   {% include 'items/accountItem.html' %}
   {% endfor %}
   ```
   In a real website, you would probably want to display the account differently in the context of the profile.

17. Create your LESS main file in `sample/static/less/style.less`:
   ```css
   @import "main.less";
   @import "mixins/buttons.less";
   @import "mixins/a.less";

   @mainColor: #4a86e8;
   @secondaryColor: #f5f07b;

   html {
       .setup-sidebar(@mainColor);
       .magicircles(@mainColor, @secondaryColor);
   }
   ```
   You may customize the content depending on the page you're on using `.current-page` where page corresponds to the page name (example: `current-index`, `current-card_list`, ...).

18. Create your Javascript main file in `sample/static/js/main.js`:
   ```javascript
   // Your functions or code that should load on all pages goes here.
   ```

19. Create your front-end dependencies file in `bower.json`:
   ```json
   {
     "name": "samplewebsite",
     "version": "0.0.0",
     "authors": [
       "db0company <db0company@gmail.com>"
     ],
     "description": "Database and community for Sample Game players.",
     "license": "Simple non code license (SNCL)",
     "dependencies": {
       "Autolinker.js": "0.15.2",
       "CuteForm": "~0.0.3",
       "bootstrap": "~3.3.5",
       "css-hexagon": "0.0.0",
       "github-wiki": "js-github-wiki#*",
       "jquery-visible": "1.2.0",
       "less": "~2.0.0",
       "navbar-variant": "~0.0.0",
       "jquery-easing": "*",
       "jquery-timeago": "timeago#^1.5.4"
     }
   }
   ```
   and the configuration file to specify the folder in `.bowerrc`:
   ```json
   {
       "directory": "sample/static/bower/"
   }
   ```

20. Get the front-end dependencies:
   ```shell
   npm install -g less bower
   bower install
   ```

21. Initialize the models:
   ```shell
   python manage.py makemigrations sample
   python manage.py migrate
   ```

22. Set up your `.gitignore`:
   ```
   env/
   sample_project/local_settings.py
   sample_project/generated_settings.py
   sample/static/bower
   sample/static/css/style.css
   sample/templates/pages/map.html
   sample/static/uploaded/
   collected/
   db.sqlite3
   ```
   Those are in addition to usual python ignored files. You can get a basic `.gitignore` when you create a GitHub repository.

23. Test that the homepage works:
   ```shell
   python manage.py runserver
   ```
   Open [http://localhost:8000/](http://localhost:8000/) in your browser

![](http://i.imgur.com/8CfckKj.png)

Start coding!
------------

1. Initial commit

```
git add .gitignore .bowerrc bower.json manage.py requirements.txt ${PROJECTNAME} ${PROJECTNAME}_project
git commit -m "Getting started with MagiCircles2"
git push
```

2. Create an admin or staff

   All users, including administrators (= superuser) or staff, need to be created using the sign up form in the website: http://localhost:8000/signup/

   After your user has been created, you may change it to super administrator by doing so:

   ```shell
   python manage.py shell
   ```

   ```python
   from magi import models
   username='YOURUSERNAME'

   # Set as super user
   models.User.objects.filter(username=username).update(is_superuser=True, is_staff=True)

   # Or set as staff
   models.User.objects.filter(username=username).update(is_staff=True)
   ```

23. Start setting up your settings, custom pages and collections:
    - See ⎡[Webite Settings](#website-settings)⎦
    - See ⎡[Collections](#collections)⎦
    - See ⎡[Enabled pages](#enabled-pages)⎦

Frequent problems
-----------------

- **I can't install / get errors for some requirements**

  You may ignore the following requirements which are not needed in a development environment:
     - `mysql`: uses sqlite3 in development
     - `less`: compiling to `.css` is only needed in production, development environment will render the less file in the browser
     - `gettext`: only needed to generate translations
     - `boto`, `django-storages`, `django-ses`, `s3`: only used in production when using AWS
     - `djangorestframework`, `django-oauth-toolkit`: only needed if you provide a REST API
     - `geopy`: used to generate the lat/long of users' locations for the map
     - `tinify`: compress the images, only useful in production

- **I can't / don't want to use the port 8000**

  Create a file `sample_project/local_settings.py` with:
  ```python
  DEBUG_PORT = 1234
  ```
  
  Start the server with:
  ```python
  python manage.py runserver 0.0.0.0:1234
  ```

***

Files tree
==========

This is the recommended file tree for your MagiCircles projects. Many of the files and folders listed here might not be needed for some websites.

- `sample/`: main folder that contains your source code
    - `settings.py`: [the settings of your website](#website-settings)
    - `models.py`: [your models](#models)
    - `model_choices.py`: it's recommended to have a separate file for the choices in model fields
    - `magicollections.py`: [your magicollections](#collections)
    - `forms.py`: [your forms](#magiform) (including [filter forms](#magifilter))
    - `views.py`: [your standalone pages](#enabled-pages)
    - `utils.py`: your utility functions
    - `admin.py`: settings of your admin panel (django default)
    - `django_translated.py`: terms translated by django (See ⎡[Avoid generating translation terms for terms already available in Django framework](#avoid-generating-translation-terms-for-terms-already-available-in-django-framework)⎦)
    - `templates/`: your django templates
        - `items/`: templates for [item views](#item-view)
            - `IdolItem.html`: a template for an example collection `Idol`
        - `pages/`: templates for your standalone pages
        - `include/`: partial templates included in other templates
            - `accountsForProfile.html`: included by profile page
    - `static/`:
        - `img/`: your images
            - `avatar.png`: avatar used by default when users don't provide it
            - `sample.png`: your illustration image
            - `sample_logo.png`: the logo on your homepage
            - `sample_logo_ja.png`: the logo for a specific language
            - `name_of_the_game.png`: illustration of the game
            - `favicon.ico`: your favicon
            - `rarity/`: example of the name of a field that contains a choice. this folder is used with cuteform
                - `1.png`: image for the choice (1 corresponds to the value)
                - `2.png`: //
        - `js/`: your javascript sources
            - `main.js`: your main js file, loaded on all pages
        - `less/`: your LESS sources
        - `css/`: CSS compiled from LESS sources goes here
            - `style.less`: your main CSS file
            - `variables.less`: your main variables
            - `mixins/`: your mixins
        - `bower/`: Frontend dependencies get installed here
    - `locale/`: translation files `.po` and `.mo`
    - `management/commands/`: your custom commands
        - `generate_settings.py`: script to generate cached settings, see ⎡[Generated Settings](#generated-settings)⎦
    - `migrations`: your migration files (auto-generated by django)
- `sample_project/`: app deployment settings
    - `settings.py`: django settings
    - `local_settings.py`: your local settings, should not be committed to your repo
    - `generated_settings.py`: generated by your `generate_settings` command
    - `urls.py`: your router for URLS - you shouldn't need to configure it, as MagiCircles will take care of that using your magicollections and enabled pages
    - `wsgi.py`: WSGI config
- `api/`: if you provide a REST API, the sources will be here
- `bower.json`: your frontend requirements
- `.bowerrc`: configuration of frontend requirements installation
- `.gitignore`: the list of files that shouldn't be committed
- `README.md`: description of your repository
- `manage.py`: default django script script to run commands
- `requirements.txt`: your python dependencies

Webite Settings
===============

Your settings file is located in `sample/settings.py`.

Required settings:

| Setting | About |
|---------|-------|
| ACCOUNT_MODEL | Your custom model to handle game accounts (`models.Account`) |
| COLOR | The dominant hex color of the website, must be the same than @mainColor in LESS ("#4a86e8") |
| DISQUS_SHORTNAME | Go to [Disqus](https://disqus.com/admin/create/) to create a new website and provide the shortname of your new website here. It will be used to display comment sections under some of your pages or collections. :warning: Make sure you disable adertisments in your disqus website settings! |
| GAME_NAME | Full name of the game that the website is about ("Sample Game") |
| SITE_IMAGE | Path of the image in `sample/static/img` folder ("sample.png"). This image is used as the main illustration of the website, shared on social media. It is recommended to avoid transparency in this image.  |
| SITE_NAME | Full name of the website (can be different from `SITE` in django settings) ("Sample Website") |
| SITE_STATIC_URL | Full URL of the static files (images, javascript, uploaded files), differs in production and development, ends with a `/` ("//i.sample.com/") |
| SITE_URL | Full URL of the website, ends with a `/` ("http://sample.com/") |

Optional settings:

| Setting | About | Default value |
|---------|-------|---------------|
| ABOUT_PHOTO | Path of the image in `sample/static/img` folder | "engildeby.gif" |
| ACTIVITY_TAGS | List of tuples (raw value, full localizable tag name) for the tags that can be added ao an activity | None |
| BUG_TRACKER_URL | Full URL where people can see issues (doesn't have to be github) | Full URL created from the GITHUB_REPOSITORY value |
| CALL_TO_ACTION | A sentence shown on the default index page to encourage visitors to sign up | _('Join the community!') |
| CONTACT_EMAIL | Main contact email address | Value in django settings `AWS_SES_RETURN_PATH` |
| CONTACT_FACEBOOK | Contact Facebook username or page | "db0company" |
| CONTACT_REDDIT | Contact reddit username | "db0company" |
| CONTRIBUTE_URL | Full URL of the guide (or README) for developers who would like to contribute | [link](https://github.com/SchoolIdolTomodachi/SchoolIdolAPI/wiki/Contribute) |
| DONATE_IMAGE | Path of the image in DONATE_IMAGES_FOLDER | None |
| DONATORS_STATUS_CHOICES | List of tuples (status, full string) for the statuses of donators, statuses must be THANKS, SUPPORTER, LOVER, AMBASSADOR, PRODUCER and DEVOTEE | "Thanks", "Player", "Super Player", "Extreme Player", "Master Player", "Ultimate Player" |
| EMAIL_IMAGE | Path of the image in `sample/static/img` folder ("sample.png") that will appear at the beginning of all the emails. | value of SITE_IMAGE |
| EMPTY_IMAGE | Path of the image for empty values in cute form in `sample/static/img` folder | "empty.png" |
| ENABLED_NAVBAR_LISTS | See ⎡[Navbar Links](#navbar-links)⎦ | |
| ENABLED_PAGES | See ⎡[Enabled pages](#enabled-pages)⎦ | |
| FAVORITE_CHARACTERS | List of tuples (id, full name, image path - must be squared image and full url) for each character that can be set as a favorite on users' profiles, if it's in a database it's recommended to use [Generated Settings](#generated-settings) to save them once in a while | None |
| FAVORITE_CHARACTER_NAME | String that will be localized to specify what's a "character". Must contain `{nth}` (example: "{nth} Favorite Idol") | "{nth} Favorite Character" |
| FAVORITE_CHARACTER_TO_URL | A function that will return the URL to get more info about that character. This function takes a link object with value (full name), raw_value (id), image | lambda _: '#' |
| GAME_DESCRIPTION | A long description of the game. Used on the about game page. | None (just shows game image) |
| GAME_URL | A link to the official homepage of the game. Used on the about game page. | None (just shows game image) |
| GET_GLOBAL_CONTEXT | Function that takes a request and return a context, must call `globalContext` in `magi.utils` | None |
| GITHUB_REPOSITORY | Tuple (Username, repository) for the sources of this website, used in about page | ('SchoolIdolTomodachi', 'MagiCircles') |
| GOOGLE_ANALYTICS | Tracking number for Google Analytics | 'UA-67529921-1' |
| HASHTAGS | List of hashtags when sharing on Twitter + used as keywords for the page (without `#`) | [] |
| JAVASCRIPT_TRANSLATED_TERMS | Terms used in `gettext` function in Javascript, must contain `DEFAULT_JAVASCRIPT_TRANSLATED_TERMS` in `magi.default_settings` | None |
| LATEST NEWS | A list of dictionaries that should contain image, title, url and may contain hide_title, used if you keep the default index page to show a carousel. Recommended to get this from [generated Settings](#generated-settings). | None |
| LAUNCH_DATE | If you want to tease your community before officially opening the website, or just let your staff team test it, you can set a launch date. It will make all the pages and collections only available to staff and make the homepage a countdown before the website opens. Example: `import datetime, pytz datetime.datetime(2017, 04, 9, 12, 0, 0, tzinfo=pytz.UTC)` | None |
| NAVBAR_ORDERING | List of collection or page names in the order you would like them to appear in the nav bar. Missing collection or page name in this list will just appear at the end.  | None (order not guaranteed) |
| ONLY_SHOW_SAME_LANGUAGE _ACTIVITY_BY_DEFAULT _FOR_LANGUAGES  | You may use this instead of `ONLY_SHOW_SAME_LANGUAGE _ACTIVITY_BY_DEFAULT` to specify per language | ['ja', 'zh-hans', 'kr'] |
| ONLY_SHOW_SAME_LANGUAGE _ACTIVITY_BY_DEFAULT | If set to `True`, uers will only see the activities in their language (regardless of authentication), otherwise, they'll see all activities in all languages. Note that users can override this behavior in their settings. | False |
| ON_PREFERENCES_EDITED | Callback after a user's preferences have been changed, takes request (contains updated request.user.preferences) | None |
| ON_USER_EDITED | Callback after a user's username or email has been changed, takes request (contains updated request.user) | None |
| PRELAUNCH_ENABLED_PAGES  | When launch date is set, all the pages in `ENABLED_PAGES` get changed to only be available to staff members, except the pages listed here. | 'login', 'signup', 'prelaunch', 'about', 'about_game', 'changelanguage', 'help' |
| PROFILE_EXTRA_TABS | A dictionary of tab name -> dictionary (name, icon, callback (= js)) to show more tabs on profile (in addition to activities and accounts) | None |
| PROFILE_TABS | Tabs visible in a user's profile page, under the box that contins the avatar, the description and the links. A dictionary with: <ul><li>`name`: localized tab name</li><li>`icon`: String name of a [flaticon](#flaticon) that illustrates the tab</li><li>`callback`: optional, name of javasript function to call to get the content of the tab - takes: <ul><li>user_id</li><li>A callback that you must call and give it the HTML tree to display for this tab and an optional other callback to call after it's been displayed</li></ul></li></ul> | accounts, activities and badges. Will be disabled if you disable their respective collection. |
| SHOW_TOTAL_ACCOUNTS | On profiles, show or hide the total number of accounts before showing the accounts | True |
| SITE_DESCRIPTION | Slogan, catch phrase of the website. May be a callable that doesn't take any argument (`lambda: _('Best database for best game')`) | "The {game name} Database & Community" |
| SITE_LOGO | Path of the image displayed on the homepage. | value of SITE_IMAGE |
| SITE_LOGO_PER_LANGUAGE | The logo displayed on the homepage may need to be different depending on the language. This is a dictionary of language code => path of the image | None |
| SITE_LONG_DESCRIPTION | A long description of what the website does. Used on the about page. May be a callable that doesn't take any argument | A long text |
| SITE_NAV_LOGO | Path of the image displayed instead of the website name in the nav bar | None |
| STATIC_FILES_VERSION | A number or string that you can change when you update the css or js file of your project to force update the cache of your users in production | '1' |
| TOTAL_DONATORS | Total number of donators (you may use magi.tools.totalDonators to save this value in the [generated settings](#generated-settings)) | 2 |
| TRANSLATION_HELP_URL | URL with guide or tools to allow people to contribute to the website's translation | [link](https://github.com/SchoolIdolTomodachi/MagiCircles/wiki/Translate-the-website) |
| TWITTER_HANDLE | Official Twitter account of this website | "schoolidolu" |
| USER_COLORS | List of tuples (raw value, full localizable color name, CSS elements name (`btn-xx`, `panel-xx`, ...), hex code of the color) | None |
| WIKI | Tuple (Username, repository) for the GitHub wiki pages to display the help pages | Value of GITHUB_REPOSITORY |

- Full details of the configuration of the settings in: `magi/settings.py` and `magi/default_settings.py`

Collections
===

![](http://i.imgur.com/9M0K2G3.png)

MagiCircles' most powerful feature is the collections, or "MagiCollections".

Pretty much everything in MagiCircles is represented using a collection.

Collections are the link between a database table and its views. It also handles some logic like routing and permissions.

Collections should be used to represent game elements such as cards, characters, songs, levels, pokémons, etc, or website elements such as users, activities, reports, etc.

It's super easy to create a collection, and they will automatically provide pages to view, list, add and edit items. Views are also available in Ajax to allow loading in a modal.

![Example of collections](http://i.imgur.com/oGPEjiZ.png)

Collections are generally composed of:

- The database: a class that inherits from `MagiModel` that corresponds to django model, with some extra helpers.
  - See ⎡[Models](#models)⎦
- The MagiCollection: a class that inherits from `MagiCollection` that will contain all the configuration.
  - See ⎡[MagiCollection](#magicollection)⎦
- (Optional) The form: one or more classes that inherit from `MagiForm` that correspond to django forms, with some extra checks. Used to add/edit.
  - See ⎡[MagiForm](#magiform)⎦
- (Optional) The filters: class that inherits from `MagiFilter` that correspond to a django form and is used to search / filter results in the list page.
  - See ⎡[MagiFilter](#magifilter)⎦

## Models

A MagiCollection always refers to a django model, but all your models aren't necessarily collections.

Models that don't need to be MagiCollections include models used only in pages (see ⎡[Enabled pages](#enabled-pages)⎦) or within another MagiCollection that has its own model.

All the django models used in collections MUST:

- [Inherit from MagiModel and provide a name](#inherit-from-itemModel-and-provide-a-name)
- [Have an owner](#have-an-owner)
- [Override `__unicode__`](#override-unicode-)

#### Inherit from MagiModel and provide a name

```python
from magi.item_model import MagiModel

class Idol(MagiModel):
    collection_name = 'idol'
    ...
```
  
`collection_name` is used to get the MagiCollection associated with this item. While multiple MagiCollections can use the same model class, the item itself will only be aware of one associated MagiCollection.

Thanks to `MagiModel`, you'll have access to some properties on all your objects, which are required, but might also be useful for you:

- All `MagiModel` provide the following properties (not meant to be overriden):

| Key | Value | Example |
|-----|-------|---------|
| `collection` | Associated MagiCollection object (retrieved using the `collection_name`) | Instance of IdolCollection |
| `collection_title` | MagiCollection setting for localized title | _('Idol') |
| `collection_plural_name` | MagiCollection setting for non-localized plural | For 'idol', it would be  `idols`, for 'activity', it would be `activities` |
| `item_url` | The URL to the ItemView | `/idol/1/Nozomi/` |
| `ajax_item_url` | The URL to the ajax ItemView | `/ajax/idol/1/` |
| `full_item_url` | The URL to the ItemView with the domain | `//sample.com/idol/1/Nozomi/` |
| `http_item_url` | The URL to the ItemView with the domain and `http` (when `//` URLs are not supported, such as in emails or when sharing) | `http://sample.com/idol/1/Nozomi/` |
| `edit_url` | The URL of the EditView | `/idols/edit/1/` |
| `ajax_edit_url` | The URL of the ajax EditView | `/ajax/idols/edit/1/` |
| `report_url` | The URL to report this item | `/idols/report/1/` |
| `image_url` | The full url of the `image` field (if any) | `//i.sample.com/static/uploaded/idols/Nozomi.png` |
| `http_image_url` | The full url of the `image` field (if any) with `http` (when `//` URLs are not supported, such as in emails or when sharing) | `http://i.sample.com/static/uploaded/idols/Nozomi.png` |
| `open_sentence` | Localized sentence to open this item (open the ItemView) | `Open idol` |
| `edit_sentence` | Localized sentence to edit this item, also used to open the page to edit this item (EditView)  | `Edit idol` |
| `delete_sentence` | Localized sentence to delete this item | `Delete idol` |
| `report_sentence` | Localized sentence to report this item, or open the page to report this item | `Report idol` |

`image_url` and `http_image_url` will use the `image` field in your model.

If you have other images in your model, you might want to add `fieldname_url` and `http_fieldname_url` to get similar tools for all your images:

```python
from magi.utils import uploadItem
from magi.item_model import MagiModel, get_image_url, get_http_image_url

class Idol(MagiModel):
    background = models.ImageField(upload_to=uploadItem('i'), null=True, blank=True)

    @property
    def background_url(self):
      return get_image_url(self.background)

    @property
    def http_background_url(self):
      return get_http_image_url(self.background)
```

#### Have an owner

```python
class Idol(MagiModel):
    owner = models.ForeignKey(User, related_name='idols')
```

Because it's very common to associate an item to an `account` and not directly to an `owner`, since `account` already has an owner, you may make your model class inherit from `AccountAsOwnerMagiModel` instead of `MagiModel`:

```python
from magi.item_model import AccountAsOwnerMagiModel

class OwnedCard(AccountAsOwnerMagiModel):
    """
    Will automatically provide a cache for the account and provide `owner` and `owner_id` properties.
    """
    account = models.ForeignKey(Account, related_name='ownedcards')
```

If your model doesn't have a direct owner or account, you may fake it by providing properties for `owner` and `owner_id`:

```python
class Book(MagiModel):
    owner = models.ForeignKey(User, related_name='books')

class Chapter(MagiModel):
    book = models.ForeignKey(Book, related_name='books')

    @property
    def owner(self):
        return self.book.owner

    @property
    def owner_id(self):
        return self.book.owner_id
```

Note: `Account` model MUST contain an actual model field `owner`.

In our example above, book would be retrieved when the propety `owner` is accessed, resulting in extra database queries. To optimize this, you can:
- Set your MagiCollection `queryset` to use `select_related` to get the book:
  ```python
  class ChapterCollection:
      queryset = models.Chapter.objects.select_related('book')
  ```
- Or save a cache of the book in your model (recommended)
    - See ⎡[Internal cache for foreign keys in models](#internal-cache-for-foreign-keys-in-models)⎦

#### Override `__unicode__`

Django models already have a `__unicode__` method, but since MagiCircles uses it extensively, it's highly recommended to override it and not rely on its default value.

```python
class Card(MagiModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
      return self.name
```

For SEO purposes, try to localize it if you can:

```python
from django.utils.translation import get_language
  
def __unicode__(self):
    if get_language() == 'ja':
        return self.japanese_name
    return self.name
```

  If you want to use an internal cache (see ⎡[Internal cache for foreign keys in models](#internal-cache-for-foreign-keys-in-models)⎦) in your unicode function, only do it when the object has actually been created, like so:

```python
def __unicode__(self):
    if self.id:
        return u'{name} - {rarity}'.format(name=self.cached_idol.name, rarity=self.rarity)
    return u'{rarity}'.format(rarity=self.rarity)
```

## MagiCollection

Collections available should be configured in `sample/magicollections.py`. It's a class that inherits from `MagiCollection`.

```python
from magi.magicollections import MagiCollection
from sample import models

class IdolCollection(MagiCollection):
    queryset = models.Idol.objects.all()
```

For each collection, you may also override the fields and methods. When overriding methods, it's recommended to call its `super`.

- Required settings:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| queryset | Queryset to get the items, don't forget to use `select_related` when you always use fields in foreign key (or use a cache in model). | *required* | models.Card.objects.all() |

- Highly recommended settings:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| title | Localized title for one item, visible for website's users  | Capitalized key | _('Card') |
| plural_title | Localized title for multiple items, visible for website's users | Capitalized key + 's' | _('Cards') |

- Other available settings:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| enabled | Is the collection enabled? When not, it won't be initialized at all and won't be available when getting a collection by name. | True | |
| name | Name of the collection, unique | Lowercased name of the class without `collection` | 'card' |
| plural_name | Multiple items string, used in URLs | key + 's' | 'cards' |
| icon | String name of a [flaticon](#flaticon) that illustrates the collection (used in navbar) | None | 'album' |
| image | Path to image that illustrates the collection (used in navbar + when adding/editing items + when share_image not available) | None | 'card.png' |
| share_image | Path to image people can see when they share the pages of this collection on social media, can be a callable that takes (collection, view, item=None). Can be overriden per view. | Value of image | 'sample_screenshot.png' |
| form_class | Form class to add / edit an item. Can be a method (see below). Can be overriden per view. | AutoForm | IdolForm |
| multipart | Are Add/Edit forms multipart (ie contain files upload)? Can be overriden per view. | 
| navbar_link | Should a link to the list view of this collection appear in the nav bar? | True | |
| navbar_link_title | When `navbar_link` is True, title displayed as a button | Value of plural_title | _('Friends') |
| navbar_link_list | Name of the [nav bar list](#nav-bar-lists) in which the link is going to appear | None | 'more' |
| navbar_link_list_divider_before | When `navbar_link_list` is specific, whould display a divider before the button? | False | |
| navbar_link_list_divider_after | When `navbar_link_list` is specific, whould display a divider after the button? | False | |
| reportable | When the `ReportCollection` is enabled and this is set to `True`, items can be reported. Staff will then be able to review reports and ignore, edit the item or delete it if necessary. | True | |
| report_edit_templates | A dictionary of reasons why a reported item should be edited. The key is a short title for the reason, and the value is a fully detailed message that will be sent to the owner when the item gets edited. Both shouldn't be localized. | {} | ```{ 'Illegal content': 'Something you shared in this activity was illegal so it has been edited.' }```|
| report_delete_templates | A dictionary of reasons why a reported item should be deleted. The key is a short title for the reason, and the value is a fully detailed message that will be sent to the owner when the item gets deleted. Both shouldn't be localized. | {} | ```{ 'Illegal content': 'Something you shared in this activity was illegal so it has been edited.' }```|
| report_allow_edit | Should staff members be allowed to edit a reported item? Otherwise, only administrators will be able to. | True | |
| report_allow_edit | Should staff members be allowed to delete a reported item? Otherwise, only administrators will be able to. | True | |
| types | See ⎡[Item Types](#item-types)⎦ | | |
| filter_cuteform | See ⎡[CuteForm](#cuteform)⎦. Can be overriden in ListView, AddView and EditView. | | |

- All collections provide the following properties (not meant to be overriden):

| Key | Value | Example |
|-----|-------|---------|
| add_sentence | Localized sentence you can use for a button to the AddView | 'Add card' |
| edit_sentence | Localized sentence you can use for a button to the EditView | 'Edit card' |


- All collections provide the following tools (not meant to be overriden):

| Name | Description | Parameters | Return value |
|------|-------------|------------|--------------|
| get_list_url | Get the URL of the ListView for this collection | ajax=False | URL (string), example: `/cards/` |
| get_add_url | Get the URL of the AddView for this collection | ajax=False, type=None | URL (string), example: `/cards/add/` or `/cards/add/rare/` (with type = `rare`) |

- Available methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| get_queryset | Queryset used to retrieve the item(s). Can be overriden per view. | queryset, parameters, request | Django queryset | The queryset given as parameters |
| form_class | Form class to add / edit an item. Doesn't have to be a method (see above). Can be overriden per view. | request, context | A form class | AutoForm |
| to_fields | See ⎡[to_fields method](#to-field-method)⎦ |


### Views

![](http://i.imgur.com/SgWuilP.png)

For each of your collections, you may enable, disable or configure views. By default, all views are enabled.

- ⎡[List view](#list-view)⎦: Paginated list of items with filters/search
- ⎡[Item view](#item-view)⎦: A page with a single item, shows comments for this item
- ⎡[Add view](#add-view)⎦: Page with a form to add a new item
- ⎡[Edit view](#edit-view)⎦: Page with a form to edit and delete an item

For each view, you may also override the fields and methods. When overriding methods, it's recommended to call its `super`.

```python
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from magi.magicollections import MagiCollection

class IdolCollection(MagiCollection):
    title = _('Idol')
    
    class ListView(MagiCollection.ListView):
        staff_required = True
        
        def check_permissions(self, request, context):
            super(IdolCollection.ListView, self).check_permissions(request, context)
            if request.user.username == 'bad_staff':
                raise PermissionDenied()
```

If you need some logic behind settings that are not methods you can use `@property`:

```python
from magi.magicollections import MagiCollection

class IdolCollection(MagiCollection):
    class ListView(MagiCollection.ListView):
        @property
        def default_ordering(self):
            return '-level' if hasattr(self.collection.queryset.model, 'level') else '-id'
```

#### All views

- All views share the following settings (can be overriden):

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| enbabled | Whether the view should be available or not. | True | |
| ajax | Is the view available in ajax? (allow to get just the page content without HTML boilerplate and navigation bar) | True | |
| ajax_callback | String name of a Javascript function to call when the view loaded. | None | 'loadCards' |
| js_files | List of javascript files to include, all files are in `static/js` except if it starts with `bower/` | [] | ['cards.js, 'bower/marked/lib/marked'] |
| shortcut_urls | <ul><li>ListView/AddView: List of URLs</li><li>AddView with types: List or (url, type) or list of URLs</li><li>ItemView/EditView: List of (url, pk) or list of URLs</li></ul> | [] | [('me', 1)] |
| multipart | Are Add/Edit forms multipart (ie contain files upload)? Can be specified in collection. | multipart in collection | True |
| authentication_required | **Permissions:** only when the user is authenticated | <ul><li>ListView/ItemView: False</li><li>AddView/EditView: True</li></ul> | |
| logout_required | **Permissions:** only when the user is NOT authenticated | False | |
| staff_required | **Permissions:** only when the user is authenticated AND part of the staff team | False | |
| owner_only | **Permissions:** only for ItemView/EditView, only when the authenticated user is the owner of the item |<ul><li>ItemView: False</li><li>EditView: True</li></ul> | |

- All views provide the following properties (not meant to be overriden):

| Key | Value | Example |
|-----|-------|---------|
| collection | The MagiCollection object associated with this view | CardCollection() |

- All views share the following methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| get_global_context | Function called to pre-fill the context before the view loads (even before checking for permissions) | request | dictionary | `GET_GLOBAL_CONTEXT` specified in settings for the website. |
| share_image | Image displayed when sharing this view on social media (Facebook, Twitter, etc). Full URL. Can be specified in collection. | context, item=None | String URL | `share_image` in MagiCollection |
| extra_context | Allows you to add extra context, typically for your templates. Called after most of the logic for the view has been executed already. [Example](https://gist.github.com/db0company/819ec1900fb207f865be69b92ce62c8e#file-magicirclesexamples-py-L20)  | context | dictionary | Just returns the context |
| get_queryset | Queryset used to retrieve the item(s) | queryset, parameters, request | Django queryset | `get_queryset` in MagiCollection |
| check_permissions | Check if the current user has permissions to load this view | request, context | None, should raise exceptions when the user doesn't have permissions. | Will check permissions depending on the views settings (such as `staff_required`, etc.), and either raise `PermissionDenied` or `HttpRedirectException` |
| check_owner_permissions | Only for ItemView and EditView, will be called after getting the item and check if the current user has permissions to load this view | request, context, item | None, should raise exceptions when the user doesn't have permissions | Will check permissions depending on the view settings (`owner_only`) and either raise `PermissionDenied` or `HttpRedirectException`.

- All views provide the following methods (not meant to be overriden):

| Name | Description | Parameters | Return value |
|------|-------------|------------|--------------|
| has_permissions | Calls `check_permissions` and `check_owner_permissions`, catches exceptions and returns True or False | request, context, item=None | True or False |
| get_page_title | Get the title of the page | None | localized string |

#### List view

![](http://i.imgur.com/p2O8Dh1.png)
![](http://i.imgur.com/E1lrmtc.png)

List view for a staff member will hide all the staff buttons by default and you can show them using the bottom left button.

![](http://i.imgur.com/Y7uVbFb.png)

- List views contain the following settings (can be overriden):

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| filter_form | Django form that will appear on the right side panel and allow people to search / filter. It's recommended to make it inherit from `MagiFilter`. | None (no side bar) | [Example](https://gist.github.com/db0company/819ec1900fb207f865be69b92ce62c8e#file-magicirclesexamples-py-L8) |
| ajax_pagination_callback | The name of a javascript function to call everytime a new page loads (including the first time) | None | "updateCards" (See [Example](https://gist.github.com/db0company/b9fde532eafb333beb57ab7903e69749#file-magicirclesexamples-js-L1)) |
| item_template | Path of the HTML template in `sample/templates/items/` to display the item (without `.html`) | Collection name + "Item" | "cardItem" |
| before_template | Name of a template to include between the title (if shown) and the add buttons (if any) and results (without `.html`) | None | "include/beforeCards" |
| after_template | Name of a template to include at the end of the list, when the last page loads (without `.html`), if you provide something in `extra_context` for this template, first check `if context['is_last_page']: ...` | None | "include/afterCards" |
| no_result_template | Name of a template to show if there's no results to show, otherwise it will just show "No result" in a bootstrap `alert-info` | None | "include/cardsNoResult" |
| per_line | Number of elements displayed per line (1, 2, 3, 4, 6, 12), make sure it's aligned with the page_size or it'll look weird :s | 3 | |
| col_break | Minimum size of the column so when the screen is too small it only shows one per line, options are 'xs' (never breaks), 'sm' (= 768px), 'md' (= 992px), 'lg' (= 1200px)  | 'md' | |
| page_size | Number of items per page | 12 | |
| show_edit_button | Should a button to edit the item be displayed under the item (if the user has permissions to edit)? Set this to `False` is your template already includes a button to edit the item. | True | |
| authentication_required | Should the page be available only for authenticated users? | False | |
| distinct | When retrieving the items from the database, should the query include a `distinct`? ⚠️ Makes the page much slower, only use if you cannot guarantee that items will only appear once. | False | |
| add_button_subtitle | A button to add an item will be displayed on top of the page, with a subtitle. | _('Become a contributor to help us fill the database') | _('Share your adventures!') |
| show_title | Should a title be displayed on top of the page? If set to `True`, the title will be the `plural_title` in the collection. | False | |
| full_width | By default, the page will be in a bootstrap container, which will limit its width to a maximum, depending on the screen size. You may change this to `True` to always get the full width | False | |
| show_relevant_fields_on_ordering | By default, when an `ordering` is specified in the search bar, the specified ordering field will be displayed under each item (see ⎡[to_fields method](#to-field-method)⎦). | True | |
| hide_sidebar | By default, the side bar will be open when you open the page. You may leave it close by default, but keep in mind that it's very unlikely that your users will find it by themselves. | False | |
| filter_cuteform | See ⎡[CuteForm](#cuteform)⎦. Can be specified in collection. | | |
| default_ordering | String name of a field (only one) | '-creation' | 'level' |

See also: [settings available in all views](#all-views).

- List views contain the following methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| foreach_item | Function called for all the elements about to be displayed, that takes the item position, the item and the context ([example](https://gist.github.com/db0company/819ec1900fb207f865be69b92ce62c8e#file-magicirclesexamples-py-L23)). If you can, provide a property inside the model's class instead, to avoid an extra loop. | index, item, context | None | None |
| show_add_button | Should a button be displayed at the beginning to let users add new items (if they have the permission to do so)? | request | Boolean | returns `True` |

See also: [methods available in all views](#all-views).

- List views provide the following methods (not meant to be overriden):

| Name | Description | Parameters | Return value |
|------|-------------|------------|--------------|
| plain_default_ordering | Transforms the `default_ordering` of the list view into a simple string, without the reverse setting and extra options. Example: `'-level,id'` becomes `'level'`. Used as the pre-selected value in the filter form. | None | string |

See also: [methods available in all views](#all-views).

#### Item view


![](http://i.imgur.com/mObTPc4.png)
![](http://i.imgur.com/19bYwFm.png)
![](http://i.imgur.com/REkJzTT.png)

- Item views contain the following settings (can be overriden):

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| template | Path of the HTML template in `sample/templates/items/` to display the item (without `.html`). May be `default` to use the defaut view with the image on top and the list of fields below it. See ⎡[to_fields method](#to_field-method)⎦ for more details about the `default` template. | Collection name + "Item" | "cardItem" |
| top_illustration | If the `default` template is used, it will show either the `image` in the object or its name. You may display something else by specifying the path of a HTML template (full path in template folder), without `.html`. | None | `include/topCard` |
| show_edit_button | Should a button to edit the item be displayed under the item (if the user has permissions to edit)? Set this to `False` is your template already includes a button to edit the item. | True | |
| comments_enabled | Should we display a comment section below the item? | True | |

See also: [settings available in all views](#all-views).

- Item views contain the following methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| get_item | How is the item retrieved using the `pk` (=id) provided in the URL? For example, in the URL `/card/12/super-rare-lily/`, `pk` will be `12` | request, pk (in URL) | a dictionary that will be used with the queryset to get a single item | `{ 'pk': pk }` |
| reverse_url | Allows you to have URLs with just a string and find the item with thout, instead of the id. For example, the default URL of a profile is `/user/1/db0/`, but with this, you can make `/user/db0/` and still be able to retrieve the corresponding user, without knowing its id. | string (text in URL, for example if the URL is `/user/tom/`, this will be `'tom'`) | a dictionary that will be used with the queryset to get a single item | None |

See also: [methods available in all views](#all-views)⎦.

#### Add view

![](http://i.imgur.com/CjYBkCO.png)

- Add views contain the following settings (can be overriden):

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| otherbuttons_template | Template path (without `.html`) for extra buttons at the end of the form | None | "include/cardsExtraButtons" |
| after_template | Name of a template to include after the form | None | "include/afterAddCard" |
| savem2m | Should we call save_m2m to save the manytomany items after saving this model? | False | |
| allow_next | Will ignore redirect_after_add and will redirect to what's specified in 'next' if speficied | True | |
| alert_duplicate | Should we display a warning that asks users to check if it doesn't already exist before adding it? | True | |
| back_to_list_button | Should we display a button to go back to the list view at the end of the form? | True | |
| multipart | Should the HTML form allow multipart (uploaded files)? Can be specified in collection. | False | |
| form_class | Form class to add an item. Can be a method (see below). Can be specified in collection. | AutoForm | IdolForm |
| filter_cuteform | See ⎡[CuteForm](#cuteform)⎦. Can be specified in collection. | | |

See also: [settings available in all views](#all-views).

- Add views contain the following methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| before_save | Function called before the form is saved. Not recommended, overload `save`in your form instead | request, instance, type=None | instance | Just returns the instance |
| after_save | Function called after the form is saved. Not recommended, overload `save`in your form instead | request, instance, type=None | instance | Just returns the instance |
| form_class | Form class to add an item. Doesn't have to be a method (see above). Can be specified in collection. | request, context | A form class | AutoForm |
| redirect_after_add | Where should the user be redirected after the item has been added successfully? | request, item, ajax | URL to redirect to | Redirect to the item view of the item that has been created if the item view is enabled, otherwise to the list view |

See also: [methods available in all views](#all-views).

#### Edit view

![](http://i.imgur.com/oaSXXyj.png)

- Edit views contain the following settings (can be overriden):

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| otherbuttons_template | Template path (without `.html`) for extra buttons at the end of the form | None | "include/cardsExtraButtons" |
| after_template | Name of a template to include after the form | None | "include/afterAddCard" |
| allow_delete | Should we show a button to delete the item as well? | False | |
| savem2m | Should we call save_m2m to save the manytomany items after saving this model? | False | |
| back_to_list_button | Should we display a button to go back to the list view at the end of the form? | True | |
| multipart | Should the HTML form allow multipart (uploaded files)? Can be specified in collection. | False | |
| form_class | Form class to edit an item. Can be a method (see below). Can be specified in collection. | AutoForm | | filter_cuteform | See ⎡[CuteForm](#cuteform)⎦. Can be specified in collection. | | |
IdolForm |

See also: [settings available in all views](#all-views).

- Edit views contain the following methods (can be overriden):

| Name | Description | Parameters | Return value | Default |
|------|-------------|------------|--------------|---------|
| before_save | Function called before the form is saved. Not recommended, overload `save`in your form instead | request, instance, type=None | instance | Just returns the instance |
| after_save | Function called after the form is saved. Not recommended, overload `save`in your form instead | request, instance, type=None | instance | Just returns the instance |
| form_class | Form class to edit an item. Doesn't have to be a method (see above). Can be specified in collection. | request, context | A form class | AutoForm |
| redirect_after_edit | Where should the user be redirected after the item has been edited successfully? | request, item, ajax | URL to redirect to | Redirect to the item view of the item that has been edited if the item view is enabled, otherwise to the list view |
| redirect_after_delete | Where should the user be redirected after the item has been deleted successfully? | request, item, ajax | URL to redirect to | Redirect to the list view |
| get_item | How is the item retrieved using the `pk` (=id) provided in the URL? For example, in the URL `/card/edit/12/`, `pk` will be `12` | request, pk (in URL) | a dictionary that will be used with the queryset to get a single item | `{ 'pk': pk }` |

See also: [methods available in all views](#all-views).

### Collectible

![](http://i.imgur.com/r3FrVK5.png)

:warning: This is a work in progress. The following guide doesn't work yet. Currently, collections have be made collecible manually.

To make a collection collectible, you need to provide a [model](#model). The model should always have either an `owner` or an `account` foreign key, allowing users to collect them.

```python
from magi import MagiModel

class CollectibleCard(AccountAsOwnerMagiModel):
    collection_name = 'collectiblecards'

    account = models.ForeignKey(Account, related_name='collectedcards')
    card = models.ForeignKey(Card, related_name='collectiblecards')
    
    ...
```

Then specify this model in the collection you want to make collectible with that model:

```python
from magi.magicollections import MagiCollection
from sample import models

class CardCollection(MagiCollection):
    collectible = models.CollectibleCard
```

Customize the MagiCollection of the collectible itself:

```python
from magi.magicollections import MagiCollection
from sample import models

class CardCollection(MagiCollection):
    collectible = models.CollectibleCard

    def to_collectible_class(self, CollectibleClass):
        class NewCollectibleClass(CollectibleClass):
            title = _('Owned Cards')
        return NewCollectibleClass
```


### CuteForm

![](http://i.imgur.com/nL7JVGw.png)

todo

### Item types

![](http://i.imgur.com/AUcuMU8.png)

You may display different forms and URLs to add an item depending on "types".

When you use types on a collection, its model must have a `type` (ie we should be able to do `instance.type`), which can be stored in database or returned with `@property`. It'll be used to retrieve the right form when editing.

![](http://i.imgur.com/vNDaGbk.png)

For example, let's say we have 3 types of cards: Normal, Rare and Super Rare and we want to use different forms for those. Our collection will look like that:

```python
ENABLED_COLLECTIONS['card'] = {
  ...
  'add': {
     ...
     types: {
       'normal': { ... },
       'rare': { ... },
       'superrare': { ... },
     },
  },
}
```

For each type, you may specify the following settings in its dictionary:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| form_class | FormClass to add/edit the item, must take request (make it inherit from FormWithRequest), can be a function that takes request, context and collection | *required* | [Example](https://gist.github.com/db0company/819ec1900fb207f865be69b92ce62c8e#file-magicirclesexamples-py-L44) |
| title | Localized title of the type | type (key) | _('Rare') |
| image | Path of an image displayed near the title of the form that illustrates the type | None | "" |

The type will be passed to the formClass when it's initialized, which allows you to reuse the same form class for all your types if you'd like.

### to_field method

`to_field` is a method in collections.

- Where is it called?
    - **ListView:** Will be called when `ordering` is specified to show the field(s) details, with `only_fields` in parameters. For example, if you order the list by level, the level is going to be displayed under the item, because it's very likely that you'll want to compare that between the items.
    - **ItemView:** If you use the template `default`, it will show a table with all the fields returned by this function.
- Can it be overriden?
    - You may override this function, but you should always call its `super`.
- Parameters
    - `item, to_dict=True, only_fields=None, in_list=False, icons={}, images={}`
    - `item` is the item object, an instance of an `MagiModel`
    - `to_dict` will return a dict by default, otherwise a list or pair. Useful if you plan to change the order or insert items at certain positions.
    - `only_fields` if specified will ignore any other field
    - `icons` is a dictionary of the icons associated with the fields
    - `images` is a dictionary of the images associated with the fields
- Return value
    - Returns a dictionary of key = field name, value = dictionary with:
        - verbose_name
        - value
        - type
        - optional: icon, image, link, link_text, ajax_link
    - Available types:
        - text
        - title_text (needs 'title')
        - image
        - bool
        - link (needs 'link_text')
        - image_link (needs 'link', 'link_text')
        - button (needs 'link_text')
        - text_with_link (needs 'link' and 'link_text', will show a 'View all' button)
        - timezone_datetime (useful when showing another timezone, otherwise use text. needs 'timezones' list. can be 'local')
        - long_text
        - html
- Default
    - Will automatically guess what should be displayed from the model fields and `reverse`  in the model if specified.

In ListView, when ordering is specified:

![](http://i.imgur.com/z1ei25k.png)

In ItemView, when template is `default`:

![](http://i.imgur.com/ikMoXCq.png)

## MagiForm

todo

+ mention AutoForm

## MagiFilter


![](http://i.imgur.com/exJJP53.png)

todo

Enabled Pages
===

![](http://i.imgur.com/eWoovuB.png)

Unlike a collection, a page corresponds to a standalone page with its own function.

It's recommended to store the templates for your pages in `sample/templates/pages/`.

To add a new page:

```python
ENABLED_PAGES['statistics'] = {
  'title': _('Statistics'),
  ...
}
```

The key corresponds to both the URL and the name of the function.

The function must be in `sample/views.py`. The function must take a request and the url_variables (if any) and return a rendered HTML page.

All your pages must contain the global context, which you can override to add your own global context settings. It's recommended to use the same globalContext function in your views than the one specified in your [website settings](#website-settings).

```python
from magi.utils import globalContext as magi_globalContext

def globalContext(request):
    context = magi_globalContext(request)
    context['something'] = 'something'
    return context

def statistics(request):
    ...
    context = globalContext(request)
    context['statistics_data'] = ...
    return render(request, 'pages/statistics.html', context)
```

For each page, you may specify the following settings:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| title | Localized title of the page (used in navbar and HTML page title) | *required* (except when ajax=True, then None) | _('Statistics') |
| ajax | Is this page only available in AJAX? (URL starts with `ajax/`) | False | |
| icon | String name of a [flaticon](#flaticon) that illustrates the page (used in navbar) | None | 'about' |
| image | Path to image that illustrates the page (used in navbar) | None | 'statistics.png' |
| custom | Is the function for this view in your project (True) or already in MagiCircles (about, settings, etc)? (False) | True | |
| navbar_link | Should a link to the list view of this collection appear in the nav bar? | True | True |
| navbar_link_list | Name of the [nav bar list](#nav-bar-lists) in which the link is going to appear | None | 'more' |
| url_variables | List of tuples (name of the variable, regexp to match the variable in the URL, function that takes a context and returns the value that should be displayed in the navbar - optional when navbar_link = False) | [] | [('pk', '\d+', lambda context: context['request'].user.id)] |

Default pages and collections
===

Some pages and collections are provided by default.

## Default pages

| URL | Enabled by default | Details |
|-----|--------------------|---------|
| / | No | Index page. Can be used when activities are disabled. |
| /login/ | Yes | Login form, only when users are NOT authenticated. |
| /signup/ | Yes | Signup form, only when users are NOT authenticated. |
| /user/{pk}/{username}/ | Yes | Just an alias to the profile page, will just call `item_view`. Useful to have a link to that view in the navbar. |
| /settings/ | Yes | Allow an authenticated user to edit their profile and preferences. |
| /logout/ | Yes | Will logout the current user and redirect to the homepage. No view. |
| /about/ | Yes | About page with a description of the website, the owners, the staff members and credits. |
| /prelaunch/ | Yes | Useful page when `LAUNCH_DATE` is provided in settings. Will display a countdown. |
| /map/ | Yes | A world map of all the users who provided their location. |
| /help/ | Yes | The homepage of the wiki of the website, with FAQ and guides. |
| /help/{wiki_url}/ | Yes | A specific page in the wiki. |
| /twitter_avatar/{twitter}/ | Yes | A handy URL that will redirect to the Twitter avatar URL. |
Ajax:
| URL | Enabled by default | Details |
|-----|--------------------|---------|
| /ajax/about/ | Yes | Ajax version of the about page, see above. |
| /ajax/about_game/ | Yes | An illustration and a short description of the game. Opens as a popup from a link on the homepage when users are not authenticated. |
| /ajax/deletelink/{pk}/ | Yes | Called from the settings page to delete a link without leaving the page. |
| /ajax/likeactivity/{pk}/ | Yes | Called from the activities to like an activity without leaving the page. |
| /ajax/follow/{username}/ | Yes | Called from the profiles to follow a user without leaving the page. |
| /ajax/changelanguage/ | Yes | Triggered from the dropdown to change the language available on all pages. |
| /ajax/moderatereport/{report}/{action}/ | Yes | In staff page to manage reports, allows staff to moderate multiple reports in a row without leaving the page. |
| /ajax/reportwhatwillbedeleted/{report}/ | Yes | A popup shown when a staff member tries to delete a reported item to warn them of all the other items that will be cascadely deleted. |
| /ajax/successedit/ | Yes | A simple page to use on successful edit when ajax is disabled for an item view. |

- Full details of the configuration of each page in: `magi/default_settings.py`
- Full details of the implementation of each page in `magi/views.py`

## Default collections

| Name | Class | Model | Details |
|------|-------|-------|---------|
| user | UserCollection | User | <ul><li>Reportable.</li><li>ItemView corresponds to the profile.</li><li>AddView is disabled (use signup page instead).</li><li>EditView is staff only, users may edit their profiles using the settings page.</li><li>ListView is enabled but likely to be used mostly when showing followers/following or likes for an activity, in an ajax popup.  |
| activity | ActivityCollection | Activity | <ul><li>Activities posted by the community, with likes and comments.</li><li>Has an empty shortcut that corresponds to the homepage, allowing the homepage to be the list of activities.</li><li> Reportable.</li></ul> |
| account | AccountCollection | `ACCOUNT_MODEL` in settings | <ul><li>Also called "leaderboard", corresponds to the list of accounts.</li><li>That's the page users see to discover other users. It links to the profiles.</li><li>ItemView is enabled but is very likely to be used only in reports view.</li><li>Reportable.</li></ul> |
| notification | NotificationCollection | Notification | <ul><li>Only ListView is enabled.</li><li>Available as a small popup from the nav bar or as a separate page.</li><li>Notifications are generated automatically when something happens that might interest the user.</li></ul> |
| report | ReportCollection | Report | <ul><li>Uses collection types, with types corresponding to reportable collections.</li><li>People who report can see/edit their own reports, but only staff can list all the reports and take actions.</ul> |

- Default collections are in `magi/magicollections.py`

### Collections disabled by default

| Name | Class | Model | Details |
|------|-------|-------|---------|
| donate | DonateCollection | DonationMonth | Page with a link to allow user to donate money to support the development and maintenance of the website. Pages to add / edit months allow staff members to keep track of the budget and show a % of funds + all the donators for that month. |
| badge | BadgeCollection | Badge | Badges can be used to show recognition when a member of the community does something. It's mostly used for donators, but can also be used as prizes when participating in a contest or for annual community rewards. |

These 2 collections allow [the author of MagiCircles](http://db0.company) to monetize the platforms, pay for the server and pay for the development time needed to make these websites available.

For this reason, it is not allowed to enable these 2 collections if you are using MagiCircles yourself. Only [the author of MagiCircles](http://db0.company) is allowed to monetize websites that use MagiCircles, except when given excplicit authorization. [Learn more](#join-the-magicircles-family).

## Enable/Disable/Configure default pages and collections

You may enable or disable them at your convenience, or override their default configurations.

Disable a page in `sample/settings.py`:
```python
ENABLED_PAGES = DEFAULT_ENABLED_PAGES
ENABLED_PAGES['help']['enabled'] = False
```

Disable a collection in `sample/magicollections.py`:
```python
from magi.magicollections import ReportCollection as _ReportCollection

class ReportCollection(_ReportCollection):
    enabled = False
```

Change something in an existing collection:
```python
from magi.magicollections import AccountCollection as _AccountCollection

class AccountCollection(_AccountCollection):
    icon = 'heart'
    
    class ListView(_AccountCollection.ListView):
        show_edit_button = False
```

Nav bar lists
===

![](http://i.imgur.com/5X1V7ef.png)

You might not want all your links to pages and collections to be on the nav bar itself, but in dropdown lists instead.

To achieve that, you may specify a `navbar_link_list` in your page or collection settings. It's a string that corresponds to the name of a list.

By default, your website will already contain 2 lists: `you` and `more`.

You may add more lists in your settings:

```python
from magi.default_settings import DEFAULT_ENABLED_NAVBAR_LISTS

ENABLED_NAVBAR_LISTS = DEFAULT_ENABLED_NAVBAR_LISTS
ENABLED_NAVBAR_LISTS['stuff'] = { ... }
```

The settings of a navbar list may contain:

| Key | Value | Default | Example |
|-----|-------|---------|---------|
| title | Localized name of the list or function that takes the context and return a string | *required* |
| icon | String name of a [flaticon](#flaticon) that illustrates the nav bar list | None | 'fingers' |
| image | Path to image that illustrates the nav bar list | None | 'stuff.png' |

API
===

![](http://i.imgur.com/3ZIP11o.png)

todo

Utils
===

## Python

#### Models upload

```python
from magi.utils import uploadToRandom, uploadItem

class Idol(MagiModel):
    image = models.ImageField(upload_to=uploadItem('i'))
    other_image = models.ImageField(upload_to=uploadToRandom('i'))    
```

- `uploadItem` will use the `__unicode__` function of the model to name the file, in addition to random characters (to make sure browsers load the latest uploaded images when re-written). It is useful for SEO purposes and recommended for the main collections (cards, characters, ...).
- `uploadRandom` will just generate a random string as the file name. It's only recommended when the `__unicode__` of the model is meaningless or for user-submitted content (activities for example).

#### Access MagiCollections

- From anywhere:
  ```python
  from magi.utils import getMagiCollections, getMagiCollection

  print len(getMagiCollections())
  print getMagiCollection('idol').name
  ```
- From an instance of a model (`MagiModel`):
  ```python
  from magi import models
  
  user = models.User.objects.get(id=1)
  print user.collection.name
  ```
  (will call `getMagiCollection` using `user.collection_name`)

Both are not recommended, and you'll usually find other ways to get the information you need than by accessing the collection object.

## Templates

todo

## Javascript

todo

Recommendations
===============

## Internal cache for foreign keys in models

Use an internal cache for fields in forein keys that are accessed often, to avoid extra `JOIN` in your queries (ie `select_related`) which slow down the queries.

Let's say every time we display a card, we also display the name and age of the idol featured in the card:

```python
from magi.utils import AttrDict

class Card(MagiModel):
    ...
    idol = models.ForeignKey(Idol, related_name='cards')
    ...

    # Cache
    _cache_idol_days = 20
    _cache_idol_last_update = models.DateTimeField(null=True)
    _cache_idol_name = models.CharField(max_length=32, null=True)
    _cache_idol_age = models.PositiveIntegerField(null=True)

    def update_cache_idol(self):
        """
        Recommended to use select_related('idol') when calling this method
        """
        self._cache_last_update = timezone.now()
        self._cache_idol_name = self.idol.name
        self._cache_idol_age = self.idol.age

    def force_cache_idol(self):
        self.update_cache_idol()
        self.save()

    @property
    def cached_idol(self):
        if not self._cache_idol_last_update or self._cache_idol_last_update < timezone.now() - datetime.timedelta(days=self._cache_idol_days):
            self.force_cache_idol()
        return AttrDict({
            'pk': self.idol_id,
            'id': self.idol_id,
            'name': self._cache_idol_name,
            'age': self._cache_idol_age,
        })
```

In your views and templates, when you need to use the name or age of the idol in the card, do the following:

```python
print card.cached_idol.name, card.cached_idol.age
```


## Calling functions in templates

While Django provides `templatetags`, it is recommended to avoid having too many `load` inside your template, especially when it's likely to be included multiple times (in a forloop for example), because they slow down the generation of the HTML page.

Instead, try to provide as much as possible of the logic behind your template in your python code, and add variables inside your context.

Example:
- Instead of:
  ```html
  {% load mytags %}
  <div>{% get_percent a b %}</div>
  ```
- Do:
  ```python
  context['percent'] = get_percent(a, b)
  ```
  ```html
  <div>{{ percent }}</div>
  ```

## Utility functions for models

It's very likely that you'll need to do something to the fields of your models, and you won't be using most of them as they are stored in the database. In that case, it's recommended to add properties to your model classes.

Example:
- Instead of:
  ```python
  today = datetime.date.today()
  idols = models.Idol.objects.all()
  for idol in idols:
      idol.age = today.year - idol.birthdate.year - ((today.month, today.day) < (idol.birthdate.month, idol.birthdate.day))
  ```
- Do:
  ```python
  class Idol(MagiModel):
      ...
      birthdate = models.DateField(_('Birthdate'))
      
      @property
      def age(self):
          return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
  ```
  ```html
  {% for idol in idols %}
  <div>{{ idol.age }}</div>
  {% endfor %}
  ```

## Generated Settings

Some values shouldn't be calculated from the database everytime, so it's recommended to write a script in `sample/management/commands/generate_settings.py` that will update the settings and call that script in a cron or a scheduler.

```python
import time
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings as django_settings
from magi.tools import totalDonators
from sample import models

def generate_settings():

        print 'Get total donators'
        total_donators = totalDonators()

        print 'Get the latest news'
        current_events = models.Event.objects.get(end__lte=timezone.now())
        latest_news = [{
            'title': event.name,
            'image': event.image_url,
            'url': event.item_url,
        } for event in current_events]

        print 'Get the characters'
        all_idols = model.Idol.objects.all().order_by('name')
        favorite_characters = [(
            idol.pk,
            idol.name,
	    idol.image_url,
        ) for idol in all_idols]

        print 'Save generated settings'
        s = u'\
import datetime\n\
TOTAL_DONATORS = ' + unicode(total_donators) + u'\n\
LATEST_NEWS = ' + unicode(latest_news) + '\n\
FAVORITE_CHARACTERS = ' + unicode(favorite_characters) + '\n\
GENERATED_DATE = datetime.datetime.fromtimestamp(' + unicode(time.time()) + u')\n\
'
        print s
        with open(django_settings.BASE_DIR + '/' + django_settings.SITE + '_project/generated_settings.py', 'w') as f:
            print >> f, s
        f.close()

class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        generate_settings()
```

And in your `sample/settings.py`, use the generated values:

```python
from django.conf import settings as django_settings

...

TOTAL_DONATORS = django_settings.TOTAL_DONATORS
LATEST_NEWS = django_settings.LATEST_NEWS
FAVORITE_CHARACTERS = django_settings.FAVORITE_CHARACTERS
```

## Avoid generating translation terms for terms already available in Django framework

Every time you add a new term to translate, check if it's not already provided by the Django Framework, to avoid adding more work to our translators when the terms don't need to be transated again.

If it is, add it in or create a file `sample/django_translated.py` like so:

```python
from django.utils.translation import ugettext_lazy as _
from magi.django_translated import t

t.update({
    'Japanese': _('Japanese'),
})
```

When you want to use the term, do:
```python
from sample.django_translated import t

print t['Japanese']
```

When generating the terms, make sure you don't include the terms in this file:

```shell
python manage.py makemessages ... --ignore=sample/django_translated.py
```

See ⎡[Translations](#translations)⎦.

## Disable activities

todo

## Disable activities but keep news for staff members

todo

Production Environment
===

1. Create your production settings file in `sample_project/local_settings.py`:
   ```python
   SECRET_KEY = '#yt2*mvya*ulaxd+6jtr#%ouyco*2%3ngb=u-_$44j^86g0$$3'
   DEBUG = False

   AWS_ACCESS_KEY_ID = 'uTFJXQn9zZc9C93qy7rL'
   AWS_SECRET_ACCESS_KEY = 'XceSYgIhLgB1lDTB7T6IydFtK5SD5ZRfPr84syjD'

   DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
   AWS_STORAGE_BUCKET_NAME = 'i.schoolido.lu'

   EMAIL_BACKEND = 'django_ses.SESBackend'
   AWS_SES_REGION_NAME = 'us-east-1'
   AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
   from boto.s3.connection import OrdinaryCallingFormat
   AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

   BASE_DIR = os.path.dirname(os.path.dirname(__file__))
   STATIC_ROOT = os.path.join(BASE_DIR, 'collected')
   ```

2. Edit your LESS file `sample/static/less/style.less` to use the full paths for dependencies:
   ```css
   @import "../../../env/lib/python2.7/site-packages/magi/static/less/main.less";
   @import "../../../env/lib/python2.7/site-packages/magi/static/less/mixins/buttons.less";
   @import "../../../env/lib/python2.7/site-packages/magi/static/less/mixins/a.less";
   ```

3. Compile the CSS:
   ```shell
   lessc sample/static/less/style.less sample/static/css/style.css
   ```

4. Collect all the static files:
   ```shell
   python manage.py collectstatic
   ```
   Upload the collected files (in `collected`) in your S3 bucket in a `static` folder.

5. Set up a MySQL database and edit your django settings file in `sample_project/local_settings.py`:
   ```python
   DATABASES = {'
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'sampledbname',
           'OPTIONS': {'charset': 'utf8mb4'},
           'USER': 'sampleuser',
           'PASSWORD': 'samplepassword',
           'HOST': 'sample.rds.amazonaws.com',
           'PORT': '3306',
       }
   }
       ```

6. Set up cron jobs

    - Send email for unread notifications, every 2 hours
    - Generate the map with locations of the users, every day at midnight
    - Generate settings, every day at midnight
    - Reload the website with the new generated settings, every day at midnight + 10 minutes

   ```shell
   crontab -e
   ```
   
   ```
   0 */2 * * * /home/ubuntu/SampleWebsite/env/bin/python /home/ubuntu/SampleWebsite/manage.py cron_notifications >> /home/ubuntu/cronjob.log 2>&1
   0 0 * * * /home/ubuntu/SampleWebsite/env/bin/python /home/ubuntu/SampleWebsite/manage.py latlong >> /home/ubuntu/latlong_cronjob.log 2>&1
   0 0 * * * /home/ubuntu/SampleWebsite/env/bin/python /home/ubuntu/SampleWebsite/manage.py generate_settings >> /home/ubuntu/settings_cronjob.log 2>&1
   10 0 * * * root service uwsgi reload
   ```


Translations
============

todo

Flaticon
===

todo

The icons come from [flaticon.com](http://www.flaticon.com/) and are credited in the about page.

To get the list of available icons and their codes, open your website on `/static/css/flaticon.html`.
