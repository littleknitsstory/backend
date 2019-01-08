import React, { Component } from "react";
import Background from '../../public/img/header/hb.jpg';

var sectionStyle = {
  backgroundImage: `url(${Background})`
};

class Header extends Component {
  render() {
    return (
            <header>
                <div className="b-header" style={ sectionStyle }>
                    <div className="b-header--title">
                        <span>LITTLE KNITS STORY</span>
                        <p>блог и магазин для вязания</p>
                    </div>
                </div>
            </header>
  )}
}

export default Header
