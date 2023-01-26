$(function() {

    var header = $("#header"),
        logo = $("#header__logo"),
        introH = $("#intro").innerHeight(),
        scrollOffset = $(window).scrollTop();



    /* Smooth scroll */
    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('scroll'),
            blockOffset = $(blockId).offset().top;

        $("#nav a").removeClass("active");
        $this.addClass("active");

        $("html, body").animate({
            scrollTop:  blockOffset
        }, 500);
    });



    /* Collapse */
    $("[data-collapse]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('collapse');

        $this.toggleClass("active");
    });


    /* Slider */
    $("[data-slider]").slick({
        infinite: true,
        fade: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    // $('.trigger').on('click', function() {
    //
    //     $('.description').toggleClass('active')
    //
    // });

    $(".trigger").click(function() {
        if($(this).hasClass("test")) {
            $(this).removeClass("test");
            $(this).html(moreText);
        } else {
            $(this).addClass("test");
            $(this).html(lessText);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });

});
