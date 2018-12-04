'use strict';
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack/webpack.scss');

new WebpackDevServer(webpack(config), {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    contentBase: '../../backend/static/builds/',
    historyApiFallback: true,
    headers: {"Access-Control-Allow-Origin": "*"}
}).listen(3000, '0.0.0.0', function (err, result) {
    if (err) {
        console.log(err)
    }
    console.log('Listening at 0.0.0.0:3000')
});
