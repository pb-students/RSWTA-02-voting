Django + TailwindCSS + LiveReload Demo
---

That's a demo app created while following a [tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/#creating-the-polls-app) for the university classes

I've decided to add some frontend styles with TailwindCSS and LiveReload support so that I can easily check the changes without having to reload all by myself.

![image](https://user-images.githubusercontent.com/13330620/111524833-d1b16a80-8754-11eb-9672-4694661ab929.png)
![image](https://user-images.githubusercontent.com/13330620/111524872-dd9d2c80-8754-11eb-8bd3-b9fd4fa71dc3.png)
![image](https://user-images.githubusercontent.com/13330620/111524899-e4c43a80-8754-11eb-8c3b-36945a686877.png)


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
