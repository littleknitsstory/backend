import React from 'react';
import ReactDOM from 'react-dom';
import '../public/assets/scss/main.scss';



class Hello extends React.Component {
    render(){
        return(
        <div>
            <h1>REACT</h1>
        </div>
        )
    }
}



ReactDOM.render(
    <Hello />
    , document.getElementById('app'));