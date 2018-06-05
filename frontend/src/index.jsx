import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route , Switch} from 'react-router-dom';
import '../public/assets/scss/main.scss';
import Blog from './components/Blog';
import Contact from './components/Contact'


ReactDOM.render((
    <BrowserRouter>
        <Switch>
            <Route exact path="/" component={Blog} />
            <Route  path="/contact" component={Contact} />
        </Switch>

    </BrowserRouter>
), document.getElementById('app'));