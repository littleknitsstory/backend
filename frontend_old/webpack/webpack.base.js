const webpack = require('webpack');
const path = require('path');
const HtmlWebPackPlugin = require("html-webpack-plugin");

const PATHS = {
    'source': path.resolve(__dirname, '../src/index.js'),
    'output': path.resolve(__dirname, '../src/bundles')
    // 'source': path.resolve(__dirname, '../assets/js'),
    // 'output': path.resolve(__dirname, '../src/bundles')
};

  module.exports = {
    entry: PATHS.source,
    output: {
        path: PATHS.output,
        filename: "bundle.js"
        // filename: "[name]-[hash].js"
    },
   module: {
     rules: [
        {
         test: /\.css$/,
         use: [
           'style-loader',
           'css-loader'
         ]
        },
        {
            test: /\.(sass|scss)$/,
            exclude: /(node_modules|bower_components)/,
            use: [
            'style-loader', 'css-loader', 'sass-loader'
            ]
        },
         //
         // {
         //    test: /\.(scss)$/,
         //    use: [{
         //      loader: 'style-loader', // inject CSS to page
         //    }, {
         //      loader: 'css-loader', // translates CSS into CommonJS modules
         //    }, {
         //      loader: 'postcss-loader', // Run post css actions
         //      options: {
         //        plugins: function () { // post css plugins, can be exported to postcss.config.js
         //          return [
         //            require('precss'),
         //            require('autoprefixer')
         //          ];
         //        }
         //      }
         //    }, {
         //      loader: 'sass-loader' // compiles Sass to CSS
         //    }]
         //  },

        { test: /\.(png|gif|jpg|cur)$/i, loader: 'url-loader', options: { limit: 8192 } },
        { test: /\.woff2(\?v=[0-9]\.[0-9]\.[0-9])?$/i, loader: 'url-loader', options: { limit: 10000, mimetype: 'application/font-woff2' } },
        { test: /\.woff(\?v=[0-9]\.[0-9]\.[0-9])?$/i, loader: 'url-loader', options: { limit: 10000, mimetype: 'application/font-woff' } },
        { test: /\.(ttf|eot|svg|otf)(\?v=[0-9]\.[0-9]\.[0-9])?$/i, loader: 'file-loader' },

        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
              loader: "babel-loader"
        }
      }
     ]
   },
      plugins: [
        new HtmlWebPackPlugin({
            template: '../src/index.html',
            // filename: "./index.html"
          // inject: "body"
    }),

        // new webpack.LoaderOptionsPlugin({ options: { postcss: [precss, autoprefixer] } })
  ]
  };
 // { test: /\.s[a|c]ss$/, use: [{ loader: "style-loader" }, { loader: "css-loader" }, { loader: "sass-loader" }] },
