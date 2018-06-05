import React, {Component} from 'react';
import Menu from './Menu'
import Header from './Header'

class Contact extends Component{
    render(){
        return(
            <div>
                <Header />
                <Menu />
                <div>Hello</div>
            </div>
        )
    }
}

export default Contact