import React from 'react';
import ReactDOM from 'react-dom';
import '../public/assets/scss/main.scss';

const title = 'My Minimal React llWebpack Babel Setup';

ReactDOM.render(
  <div>{title}</div>,
  document.getElementById('app')
);

module.hot.accept();
