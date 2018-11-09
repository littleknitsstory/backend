- first time - install [yarn](https://yarnpkg.com/lang/en/) is dependency management

```
# linux
sudo apt-get install yarn 
yarn
# mac
sudo brew install yarn
# compile dependency
yarn
```
- recommended use [bootstrap](https://getbootstrap.com/docs/4.1/components/buttons/)


### FOR STYLE SCSS
- second - write code  
  - html (ex. ```backend/templates/contacts/contacts.html```)
     ```
     {% extends 'base.html' %}
     {% block content %}
     <form action="" style="b-contacts">
       {{ form }}
     </form>
     {% endblock %}
     ```
  - add new scss file (ex. ```frontend/public/assets/scss/components/b-contats.scss``` )
    ```
    .b-contacts{
      background: #1b6d85;
    }
    ```
    - add scss in ```frontend/public/assets/scss/main.scss```
        ```
        @import "components/b-test";
        // add 
        @import "components/b-contats";
        ```

- compile file with [webpack](https://webpack.js.org/)
```
# inside frontend
yarn run build-scss-for-django
```

### FOR JS FILES
- we use js files as components
- create js file in frontend/src/components:
```
# example for frontend/src/components/ContactForm/index.js:
import $ from 'jquery';


const ContactForm = ((formID = $('#ajax-form-contact-form')) => {
  // HERE WRITE JS CODE

})();

export default ContactForm;

```
- include this file in ```frontend/src/build.scss.js```

```
 ...
 import ContactForm from './components/ContactForm';
```

- compile file with [webpack](https://webpack.js.org/)
```
# inside frontend
yarn run build-scss-for-django
```

#### ITS ALL RIGTH WORKING!!!

### questions remained??

- what doing command ```yarn run build-scss-for-django```???

    - this is commant start script in ```frontend/package.json:10```
    ```
      "scripts": {
        ...
        "build-scss-for-django": "webpack --config webpack/webpack.scss.js --progress --colors --mode=development",
       }
    ```
    
    - webpack/webpack.scss.js:
    ```
    ...
   config.entry = {
      main: [ 
      //
      // THIS IS PATH INCLUDE index file (here build.scss.js)
      //
        path.join(__dirname, '../src/build.scss.js')
      ] 
    };
    
    config.output = {
      //
      // THIS IS PATH WHEN SAVE ALL STYLE 
      //
      path: path.join(__dirname, '../../backend/static/builds/'),
      filename: '[name]-[hash].min.js',
    };
    config.plugins = [
      //
      // THIS IS PATH .json file for plugin django-webpack-loader
      //
      new BundleTracker({ filename: '../backend/static/webpack.scss.json' }),
    ];

    ```
    - /src/build.scss.js:
    ```
    import '../public/assets/scss/main.scss';
    import Subcribe from './components/Subcribe';
    import './app'    
    ```




   
    
    
