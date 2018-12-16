import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route , Switch} from 'react-router-dom';
import '../public/assets/scss/main.scss';
import Blog from './components_jsx/Blog';
import Contact from './components_jsx/Contact'


ReactDOM.render((
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={Blog} />
            <Route  path="/contact" component={Contact} />
            <Route  path="/detail" component={Contact} />
        </Switch>

    </BrowserRouter>
), document.getElementById('app'));
