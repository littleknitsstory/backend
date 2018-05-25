import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import '../public/assets/scss/main.scss';
import App from './components/App';
import Contact from './components/Contact'



ReactDOM.render((
    <BrowserRouter>
        <App />
        <Route  path="/" component={Contact} />
    </BrowserRouter>
), document.getElementById('app'))