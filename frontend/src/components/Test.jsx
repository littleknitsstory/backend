import React from 'react';
import axios from 'axios';

let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
  }
};
export default class Test extends React.Component {
  state = {
    posts: []
  };

  componentDidMount() {
    axios.get(`http://localhost:8000/posts/?format=json`,
        axiosConfig)
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
