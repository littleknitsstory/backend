var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
var webpack = require('webpack');
var config = require('./webpack.base.js');

config.entry = {
  main: [
    'webpack-dev-server/client?http://0.0.0.0:3000',
    'webpack/hot/only-dev-server',
    'react-hot-loader/patch',
    path.join(__dirname, '../src/index')
  ]

};
config.mode = 'development';
config.devtool = 'inline-sourcemap';
config.output = {
  path: path.join(__dirname, '../public'),
  filename: 'bundle.js',
  // filename: '[name]-[hash].js',
  publicPath: '/',
};

config.plugins = [
  new webpack.HotModuleReplacementPlugin(),
  new BundleTracker({ filename: './webpack/webpack-stats.dev.json' }),
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
  contentBase: './public',
  historyApiFallback: true,
  host: '0.0.0.0',
  port: 3000

};

module.exports = config;

