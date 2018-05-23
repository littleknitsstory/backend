'use strict';
const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const PATHS = {
    'source': path.resolve(__dirname, '../assets/'),
    'output': path.resolve(__dirname, '../src/static/bundles'),
};

const RULES = {
    json: {
        test: /\.json$/,
        loader: 'json-loader'
    },
    html: {
        test: /\.html$/,
        use: 'html-loader',
    },
    fonts: {
        test: /\.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
        loader: 'file-loader?name=fonts/[name].[ext]'
    },
    images: {
        test: /\.(png|jpe?g|gif|ico|svg)$/,
        // loader: 'file-loader?name=assets/[name].[hash].[ext]'
        use: [
            {
                loader: 'file-loader',
                options: {
                    name: '[name].[hash].[ext]',
                    outputPath: 'images/'
                    //     publicPath: 'images/'
                }
            }
        ]
    }
};

module.exports = {
    context: PATHS.source,
    entry: {},
    output: {
        path: PATHS.output,
        filename: "[name]-[hash].js"
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jquery: 'jquery',
            jQuery: 'jquery',
            'window.jquery': 'jquery',
            'window.jQuery': 'jquery',
        }),
    ],
    module: {
        loaders: [
            RULES.json,
            RULES.html,
            RULES.fonts,
            RULES.images,
        ]
    },
    resolve: {
        extensions: ['*', '.js', '.jsx']
    },
};