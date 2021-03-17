Django + TailwindCSS + LiveReload Demo
---

That's a demo app created while following a [tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/#creating-the-polls-app) for the university classes

I've decided to add some frontend styles with TailwindCSS and LiveReload support so that I can easily check the changes without having to reload all by myself.

## Install
```shell
git clone https://github.com/wvffle/django-ps4.git
cd django-ps4
yarn install
```
`yarn install` installs all the development dependencies, django, django-livereload-server and migrates the django database

## Development
To start development server run:
```shell
yarn dev
```
It starts the django server, together with livereload server and watches for `polls/templates/**/*.html` changes for windicss to compile `tailwindcss.css`

## Production
The production step is simply for windicss to create a minified version of `tailwindcss.css` file.
```shell
yarn prod
```