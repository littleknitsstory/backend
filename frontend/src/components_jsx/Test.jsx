import React from 'react';
import axios from 'axios';

export default class Test extends React.Component {
  state = {
    posts: []
  };

  componentDidMount() {
    axios.get(`http://localhost:8000/posts/?format=json`,
        )
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
      <div>
            { this.state.posts.map(posts =>
       <div className="b-blog--item">
                <div className="b-blog--item__border">
                    <div className="b-blog--item_img">
                        <img src="" alt=""/>
                        <div className="b-blog--item_tag"><a href="#">обучение</a></div>
                    </div>
                    <div className="b-blog--item_title"><h2>{posts.title}</h2></div>
                    <div className="b-blog--item_description">{posts.content}</div>
                    <div className="b-blog--item_button">
                        <button type="button">Подробней</button>
                    </div>
                </div>
            </div>

     )}
     </div>


    )
  }
}
