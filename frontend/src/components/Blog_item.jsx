import React, { Component } from "react";


export default class Blog_item extends Component {
  render() {
    return (
            <div className="b-blog--item">
                <div className="b-blog--item__border">
                    <div className="b-blog--item_img">
                        <img src="" alt=""/>
                        <div className="b-blog--item_tag"><a href="#">обучение</a></div>
                    </div>
                    <div className="b-blog--item_title"><h2>Простые и легкие DIY цветочные горшки</h2></div>
                    <div className="b-blog--item_description">
                        Не следует, однако забывать, что реализация намеченных плановых заданий обеспечивает широкому кругу (специалистов) участие в формировании системы обучения кадров, соответствует насущным потребностям.
                    </div>
                    <div className="b-blog--item_button">
                        <button type="button">Подробней</button>
                    </div>
                </div>
            </div>

  )}
}

