import $ from 'jquery';

const Blogmore = ((more_porst_ID = $('#posts')) => {
    $(document).ready(function(){
        $("#more-posts").click(function() {
        var endpoint = '/blog/moreposts/';
        load_page(
            endpoint,
            "#pagination-id",
            "#more-posts",
            "#posts",
        );
        });

        function load_page(
            page_url, paginationfield_id, loadbutton_id, pagediv_id,
        ){
            page = parseInt($(paginationfield_id).val());

            $(loadbutton_id).prop("disabled", true);
            $(loadbutton_id).text("Loading ...");

            $.ajax({
                async: true,
                type: "GET",
                url: page_url,
                data: { page: page },
                error: function() {
                        $(loadbutton_id).replaceWith("<p>error on GET</p>");
                    },
                success: function(data){ // check if there is an additional page
                                        // , disable load button if not
                        $.ajax({
                            async: true,
                            type: "HEAD",
                            url: page_url,
                            data: { page: page + 1 },
                            error: function(data){
                                    $(loadbutton_id).replaceWith("<p>No more data</p>");
                                },
                            success: function(response){
                                    $(loadbutton_id).text("Load more");
                                    $(paginationfield_id).val(page + 1);
                                    $(loadbutton_id).prop("disabled", false);
                                }
                        });
                        $(pagediv_id).append($(data));
                        $(".b-blog--item__more").insertAfter($(".blog-main .b-blog--item:last"));
                    }
            });
        }
    })
})();
 
export default Blogmore;
