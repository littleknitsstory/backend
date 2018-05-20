var express = require('express');
// import { createStore } from 'redux';


const server = express();
const port = process.env.PORT || 3000;


function renderFullPage(html, preloadedState) { /* ... */ }

server.listen(port, function(){
    console.log("Server running on port " + port);
});