import React, { Component } from "react";
import { Link, Router, Route, Switch } from 'react-router-dom'

import Header from './Header';
import Menu from './Menu';
import Blog_header from "./Blog_header";
import Blog_main from "./Blog_main";
import Test from "./Test";


export default class Blog extends Component {
  render() {
    return (
            <div>
                <Header/>
                <Menu/>
                <Blog_header/>
                {/*<Test/>*/}
                <Blog_main/>
            </div>
        )
  }
}

