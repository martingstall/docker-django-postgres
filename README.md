# docker-django-postgres

## web components
The web components are located in sample_app/static/src/, with any NPM dependencies being built in sample_app/static/web_modules, thanks to Snowpack. To get set up:

* run `npm install`
* run `npm run prepare`
* any time you add another NPM dependency (i.e. an import) into the app's JS, you'll need to re-run `npm run prepare`
