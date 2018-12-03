var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.base.js');

config.entry = {
  main: [
      'webpack-dev-server/client?http://0.0.0.0:3000',
      'webpack/hot/only-dev-server',
      path.join(__dirname, '../src/build.scss.js')
  ]
};
config.devtool = 'inline-sourcemap';

config.output = {
    path: path.join(__dirname, '../../backend/static/builds/'),
    // filename: '[name]-[hash].min.js',
    filename: 'bundle.js',
    // publicPath: '../'
};


config.plugins = [
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({ filename: '../backend/static/webpack.scss.json' }),
    // new HtmlWebpackPlugin({
    //   title: 'Hot Module Replacement'
    // }),

    new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('development'),
      BASE_URL: JSON.stringify('http://0.0.0.0:8000/'),
    }
  })
];

config.devServer = {
  inline: true,
  progress: true,
  hot: true,
  contentBase: '../public',
  // contentBase: '../../backend/static/builds/',
  historyApiFallback: true,
  host: '0.0.0.0',
  port: 3000

};


module.exports = config;
