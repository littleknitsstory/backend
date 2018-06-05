import React, { Component } from "react";
import Blog_item from "./Blog_item";


class Blog_main extends Component {
  render() {
    return (
            <section>
            <div className="row">
                <div className="blog-main">
                    <Blog_item/>

                    <div className="b-blog--item__more">
                        <button type="button" className="" id="">Больше постов</button>
                    </div>
                </div>
                <div className="sidebar">
                    <div className="b-about">
                        <div className="b-about_title"><h3>ОБ АВТОРЕ</h3></div>
                        <div className="b-about_img">
                            <img src="" alt=""/>
                        </div>
                        <div className="b-about_name"><a href="">Катя Анаприенко</a></div>
                        <div className="b-about_content">
                            Etiam eu molestie eros, commodo hendrerit sapien. Maecenas tempus leo ac nisi iaculis porta. Sed sapien tortor, aliquet a velit ut.
                        </div>
                        <div className="b-about_socia">
                            <a href="#"><i className="fab fa-vk"></i></a>
                            <a href="#"><i className="fab fa-facebook-f"></i></a>
                            <a href="#"><i className="fab fa-instagram"></i></a>
                            <a href="#"><i className="fab fa-telegram-plane"></i></a>
                        </div>
                    </div>
                    <div className="b-subcribe">
                        <div className="b-subcribe_title">Узнайте об интересных и эксклюзивных обновлениях первыми</div>
                        <div className="b-subcribe_form">
                            <form className="form-inline">
                                <input type="email" className="form-control b-subcribe_form__input" id="" placeholder="Email"/>
                                <button type="submit" className="" id="">Подписаться</button>
                            </form>
                        </div>
                    </div>
                    <div className="b-category">
                        <div className="b-category--title"><h3>Категории</h3></div>
                        <div className="b-category--item"><a href="">Декор (1)</a></div>
                        <div className="b-category--item"><a href="">Игрушки (3)</a></div>
                        <div className="b-category--item"><a href="">Ещё категория (19)</a></div>
                        <div className="b-category--item"><a href="">Вязание (2)</a></div>
                        <div className="b-category--item"><a href="">Пряжа (20)</a></div>
                    </div>
                    <div className="b-banner">баннер</div>
                    <div className="b-post-latest">
                    <div className="row">
                        <h3>Последнии посты</h3>
                    </div>
                    <div className="b-post-latest--item">
                        <div className="b-post-latest--item_img">
                            <img src="" alt=""/>
                        </div>
                        <div className="b-post-latest--item_content">
                            <div className="b-post-latest--item_title"><a href="">How to Wrap 15 Gifts In 3 Minutes</a></div>
                            <div className="b-post-latest--item_time">on December 6, 2016</div>
                        </div>
                    </div>
                    <div className="b-post-latest--item">
                        <div className="b-post-latest--item_img">
                            <img src="" alt=""/>
                        </div>
                        <div className="b-post-latest--item_content">
                            <div className="b-post-latest--item_title"><a href="">Как научится вязать закрытыми глазами</a></div>
                            <div className="b-post-latest--item_time">написано Декабрь 6, 2016</div>
                        </div>
                    </div>
                    <div className="b-post-latest--item">
                        <div className="b-post-latest--item_img">
                            <img src="" alt=""/>
                        </div>
                        <div className="b-post-latest--item_content">
                            <div className="b-post-latest--item_title"><a href="">How to Wrap 15 Gifts In 3 Minutes</a></div>
                            <div className="b-post-latest--item_time">on December 6, 2016</div>
                        </div>
                    </div>
                </div>
                </div>
            </div>

    </section>

  )}
}

export default Blog_main