import React from 'react';
import axios from 'axios';
var cors = require('cors');

export default class Test extends React.Component {
  state = {
    posts: []
  };

  componentDidMount() {
    axios.get(`http://localhost:8000/posts/?format=json`,
        cors)
      .then(res => {
        const posts = res.data;
        this.setState({ posts });
      })
      .catch(function(error) {
        console.log(error);
      })
  }

  render() {
    return (
      <ul>
        { this.state.posts.map(posts => <li>{posts.title}</li>)}
      </ul>
    )
  }
}
