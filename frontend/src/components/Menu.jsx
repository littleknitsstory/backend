import React, {Component} from 'react';
import { Link, Route } from 'react-router-dom'
import Contact from './Contact';


class Menu extends Component{
    render(){
        return(
            <nav>
                <div className="b-menu">
                    <div className="b-menu-social">
                        <ul>
                            <li><a href="#"><i className="fab fa-vk"></i></a></li>
                            <li><a href="#"><i className="fab fa-facebook-f"></i></a></li>
                            <li><a href="#"><i className="fab fa-instagram"></i></a></li>
                            <li><a href="#"><i className="fab fa-pinterest-p"></i></a></li>
                        </ul>
                    </div>
                    <div className="b-menu-link">
                        <ul>
                            <li><Link to='/'>БЛОГ</Link></li>
                            <li><Link to='/shop'>МАГАЗИН</Link></li>
                            <li><Link to='/autor'>АВТОРЫ</Link></li>
                            <li><Link to='/portfolio'>ПОРТФОЛИО</Link></li>
                            <li><Link to='/contact'>КОНТАКТЫ</Link></li>
                        </ul>
                    </div>
                    <div className="b-menu-bucket">
                        <ul>
                            <li><span><i className="fas fa-cart-plus"></i></span></li>
                            <li><span><i className="fas fa-cart-plus"></i></span></li>
                            <li><span><i className="fas fa-cart-plus"></i></span></li>
                            <li><span><i className="fas fa-cart-plus"></i></span></li>
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}


export default Menu