var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.base.js');

config.entry = {
  main: [
    path.join(__dirname, '../src/build.scss.js')
  ]
};

config.output = {
  path: path.join(__dirname, '../../backend/static/builds/'),
  filename: '[name]-[hash].min.js',
  // publicPath: '/static/js/builds/'
};

config.plugins = [
  new BundleTracker({ filename: '../backend/static/webpack.scss.json' }),
];

module.exports = config;
